# -*- coding: utf-8 -*-


class Cell(object):
    """
    A single cell of a row that will be displayed as an integer.
    """
    def __init__(self, value):
        self._value = value

    def __str__(self):
        if self._value is None:
            return "-"
        return "{:,.2f}".format(self._value)

    @property
    def value(self):
        return self._value


class Float(Cell):
    """
    A cell that will be displayed as a float.
    """
    # TODO Set precision
    def __str__(self):
        if self._value is None:
            return "-"
        return "${:,.2f}".format(self._value)


class USD(Cell):
    """
    A cell that will be displayed as a US Dollar.
    """
    def __str__(self):
        if self._value is None:
            return "-"
        return "${:,.2f}".format(self._value)
