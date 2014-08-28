# -*- coding: utf-8 -*-
from datetime import date

from consoletable.table import Table

data = [
    ("Date", "Group", "Value1", "Value2"),
    (date(2014, 5, 11), "A", 4, 1.5),
    (date(2014, 5, 12), "A", 3, 2.5),
    (date(2014, 5, 12), "A", 1, 1.5),
    (date(2014, 5, 14), "A", 6, 3.7),
    (date(2014, 5, 14), "A", 1, 7),
    (date(2014, 5, 11), "B", 2, 6.7),
    (date(2014, 5, 11), "B", 1, 0),
    (date(2014, 5, 11), "B", 1, 2.7),
    (date(2014, 5, 14), "B", 1, 1.2),
    (date(2014, 5, 12), "C", 4, 2.7),
    (date(2014, 5, 12), "C", 8, 0.7),
    (date(2014, 5, 13), "C", 1, 0),
    (date(2014, 5, 13), "C", 2, 3.3),
    (date(2014, 5, 14), "C", 1, 6.3),
]

print Table(data)
print Table(data, x=1, value=3)
print Table(data, x=1, value=3).pretty(padding=" | ", header_char="=")
