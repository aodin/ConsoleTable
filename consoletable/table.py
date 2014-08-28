# -*- coding: utf-8 -*-
from collections import defaultdict, OrderedDict
import datetime

from consoletable.parser import Parser
from consoletable.category import Category, DateCategory
from consoletable.cell import Cell, Float


class Table(object):
    """
    Table is called directly to parse and output data. It includes all the
    categories and cells to create a pretty printed table.
    Any exceptions are simply raised.
    """
    # Types for category axes
    category_types = {
        datetime.date: DateCategory,
        str: Category,
        unicode: Category,
    }

    # Types for values
    cell_types = {
        float: Float,
        int: Cell,
    }

    def __init__(self, data, header=True, x=None, y=None, value=None):
        """
        Create a new table from a python iterable.

        Arguments:
        data -- the iterable to be parsed

        Keyword arguments:
        header -- when `True` the first row will be interpreted as a header
        x -- the index of the x variable
        y -- the index of the y variable
        value -- the index of the value to be aggregated
        """
        self.index = defaultdict(float)

        # TODO Additional parsers
        self.data = Parser(data).data

        # The columns must be equal for every row
        self.n = None

        if header:
            # Set aside the header
            self.header = self.data.next()
            self.n = len(self.header)
        else:
            self.header = None

        # Order is important for determining default order
        self.categories = OrderedDict() # col -> category
        self.cells = OrderedDict()

        # Save all categories used in both axes
        self.xs = set()
        self.ys = set()

        # Iterate through the data
        for row in self.data:
            if self.n and len(row) != self.n:
                raise Exception("Expected {} columns, have {}".format(self.n, len(row)))
            elif not self.n:
                self.n = len(row)

            if not self.categories:
                self.set_types(row, self.header)
                self.set_keys(x=x, y=y, value=value)

            # Build the index using the categories and aggregating the value
            key = tuple([row[c] for c in self.cat_keys])
            self.xs.add(key[0])
            self.ys.add(key[1])
            self.index[key] += row[self.value_key]


    def set_types(self, row, header=None):
        """
        Determine types of each column.
        """
        # TODO Determine if list or dict
        for col, value in enumerate(row):
            t = type(value)
            category = self.category_types.get(t)
            if category:
                self.categories[col] = category
                continue

            cell = self.cell_types.get(t)
            if cell:
                self.cells[col] = cell

            # TODO error on unmatched rows?

        if len(self.categories) < 2:
            raise Exception("Insufficient number of categories found: {}", len(self.categories))

        if len(self.cells) < 1:
            raise Exception("Insufficient number of cells found: {}", len(self.cells))


    def set_keys(self, x=None, y=None, value=None):
        """
        Determine the indexes of the axes and the value to be aggregated.
        If no keyword arguments are provided, it will process them in order.
        Sets a tuple of axes (x, y) at self.keys
        """
        if x is not None and y is not None:
            # Use the specified x and y indexes
            self.cat_keys = (x, y)
        elif x is not None:
            # Use the specified x and the first non-x category as y
            first_col = None
            for col, category in enumerate(self.categories):
                if col != y:
                    first_col = col
                    break
            self.cat_keys = (x, first_col)
        elif y is not None:
            # Use the specified y and the first non-y category as x
            first_col = None
            for col, category in enumerate(self.categories):
                if col != x:
                    first_col = col
                    break
            self.cat_keys = (first_col, y)
        else:
            # Use the first two categories
            self.cat_keys = tuple(self.categories.keys()[:2])

        self.value_key = value if value else self.cells.keys()[0]
            

    def __str__(self):
        """
        String output with default settings.
        """
        return self.pretty()

    def pretty(self, padding="  ", header_char='-', joiner="\n", category_template="{:<%d}", value_template="{:>%d}"):
        """
        Pretty-printed string output of the table.

        Kewyword arguments:
        padding -- string used for padding between columns
        header_char -- adds a break with the given character between the header
                       and table data
        joiner -- string used to join table rows
        category_template -- the initial template that should be used for
                             category columns.
        value_template -- the initial template that should be used for
                          value columns.
        """
        # Save the max size of each column
        # TODO Try to fit in 80 columns
        sizes = defaultdict(int)

        cell_type = self.cells.values()[0]

        # TODO categories can provide customized sorting
        sorted_xs = sorted(self.xs)
        sorted_ys = sorted(self.ys)

        rows = []
        for y in sorted_ys:
            # Determine the size of y axis labels
            output_len = len(str(y))
            if output_len > sizes['y']:
                sizes['y'] = output_len

            row = []
            for col, x in enumerate(sorted_xs):
                # Use get() because None is important during output
                cell = cell_type(self.index.get((x, y)))
                
                # Determine the size of the cell string output
                output_len = len(str(cell))
                if output_len > sizes[col]:
                    sizes[col] = output_len

                # Add the cell to the row
                row.append(cell)

            # Add the row to the table
            rows.append(row)

        # Add headers and categories
        t_out = [""] # Start with an empty row
        y_format_string = category_template % (sizes.get('y', 0))
        r_out = [y_format_string.format("")]

        for col, cell in enumerate(sorted_xs):
            output_len = len(str(cell))
            if output_len > sizes[col]:
                sizes[col] = output_len
            format_string = value_template % (sizes.get(col, 0))
            r_out.append(format_string.format(str(cell)))

        header_out = padding.join(r_out)
        t_out.append(header_out)

        if header_char:
            # Add a break
            t_out.append(header_char * len(header_out))

        # Add category and values for each row
        for i, y in enumerate(sorted_ys):
            r_out = [y_format_string.format(str(y))]
            for col, cell in enumerate(rows[i]):
                format_string = value_template % (sizes.get(col, 0))
                r_out.append(format_string.format(cell))
            t_out.append(padding.join(r_out))

        return joiner.join(t_out)
