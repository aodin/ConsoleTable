# -*- coding: utf-8 -*-
from collections import defaultdict


class Parser(object):
    """
    Parser accepts an iterable of lists or dicts and attempts to parse it.
    """
    def __init__(self, data):
        # Data must be an iterable
        self.data = iter(data)


class CSVParser(object):
    """
    Convert a CSV file to a data iterator. Cast types where specified.
    """
    def __init__(self, filename=None, formats=None):
        self._index = defaultdict(float)

        if filename:
            # Parse the given file according to the file ending
            pass
