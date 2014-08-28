# -*- coding: utf-8 -*-


class Parser(object):
    """
    Parser accepts an iterable of lists or dicts and attempts to parse it.
    """
    def __init__(self, data):
        # Data must be an iterable
        self.data = iter(data)
