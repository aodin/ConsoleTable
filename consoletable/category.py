# -*- coding: utf-8 -*-
import datetime


class Category(object):
    """
    A category for an axis.
    """
    def __init__(self, label=""):
        self._label = label

    def parse(self, value):
        """
        Parse the given value as a simple text category.
        """
        return value


class DateCategory(Category):
    """
    A category for an axis that represents a date.
    """
    def __init__(self, label="", format="%Y-%m-%d"):
        self._format = format
        super(DateCategory, self).__init__(label=label)

    def parse(self, value):
        """
        Parse the given value as a date with the current format string.
        """
        try:
            return datetime.datetime.strptime(value, self._format)
        except ValueError:
            return None

