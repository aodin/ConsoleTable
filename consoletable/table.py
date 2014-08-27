# -*- coding: utf-8 -*-
from collections import defaultdict, OrderedDict
import datetime

from consoletable.parser import Parser, CSVParser
from consoletable.category import Category, DateCategory
from consoletable.cell import Cell, Float


class Table(object):
    """
    Table is the parent 
    """
    # Parsers for various filenames
    parsers = {
        "csv": CSVParser,
    }

    category_types = {
        datetime.date: DateCategory,
        str: Category,
        unicode: Category,
    }

    cell_types = {
        float: Float,
        int: Cell,
    }

    def __init__(self, data, formats=None, header=True, index=None):
        self.index = defaultdict(float)

        # If data is a string, treat it as a filename
        if type(data) is str:
            # Parse the given file according to the file ending
            pass
        else:
            self.data = Parser(data).data

        # The columns must be equal for every row
        self.n = None

        # Set aside the header
        if header:
            self.header = self.data.next()
            self.n = len(self.header)

        self.categories = OrderedDict() # col -> category
        self.cells = OrderedDict()

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

            # Build the index using the first two categories and aggregating
            # the first value
            key = tuple([row[c] for c in self.categories.keys()[:2]])
            self.xs.add(key[0])
            self.ys.add(key[1])
            self.index[key] += row[self.cells.keys()[0]]


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


    def __str__(self):
        # Save the max size of each column
        # TODO Try to fit in 80 columns
        sizes = defaultdict(int)

        cell_type = self.cells.values()[0]

        # TODO categories can provide sorting
        rows = []
        for y in self.ys:
            row = []
            for col, x in enumerate(self.xs):
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

        # Add headers
        t_out = [""] # Start with an empty row
        r_out = []
        for col, cell in enumerate(self.xs):
            output_len = len(str(cell))
            if output_len > sizes[col]:
                sizes[col] = output_len
            format_string = "{:>%d}" % (sizes.get(col, 0))
            r_out.append(format_string.format(str(cell)))
            # TODO Set the padding string
        t_out.append(' '.join(r_out))

        for row in rows:
            r_out = [] 
            for col, cell in enumerate(row):
                format_string = "{:>%d}" % (sizes.get(col, 0))
                r_out.append(format_string.format(cell))

            # TODO Set the padding string
            t_out.append(' '.join(r_out))

        return '\n'.join(t_out)


    def determine_parser(filename):
        pass
