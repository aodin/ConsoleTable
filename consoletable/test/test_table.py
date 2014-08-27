# -*- coding: utf-8 -*-
import unittest
import datetime

from consoletable.table import Table


example = [
    ("Date", "Group", "Value"),
    (datetime.date(2014, 5, 11), "A", 4),
    (datetime.date(2014, 5, 12), "A", 3),
    (datetime.date(2014, 5, 12), "A", 1),
    (datetime.date(2014, 5, 14), "A", 6),
    (datetime.date(2014, 5, 14), "A", 1),
    (datetime.date(2014, 5, 11), "B", 2),
    (datetime.date(2014, 5, 11), "B", 1),
    (datetime.date(2014, 5, 11), "B", 1),
    (datetime.date(2014, 5, 14), "B", 1),
    (datetime.date(2014, 5, 12), "C", 4),
    (datetime.date(2014, 5, 12), "C", 8),
    (datetime.date(2014, 5, 13), "C", 1),
    (datetime.date(2014, 5, 13), "C", 2),
    (datetime.date(2014, 5, 14), "C", 1),
]

class TestTable(unittest.TestCase):

    def setUp(self):
        pass

    def test_list(self):
        p = Table(example)
        self.assertEqual(p.n, 3)

        print p
        

if __name__ == '__main__':
    unittest.main()