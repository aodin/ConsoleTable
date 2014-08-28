# -*- coding: utf-8 -*-
import unittest
from datetime import date

from consoletable.table import Table


example_list = [
    ("Date", "Group", "Value", "Other"),
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

class TestTable(unittest.TestCase):

    def setUp(self):
        pass

    def test_list(self):
        # Use default settings
        p = Table(example_list)
        self.assertEqual(p.n, 4)

        # Index values should have been aggregated
        self.assertEqual(len(p.index), 8)
        self.assertEqual(p.index[date(2014, 5, 14), "B"], 1)
        self.assertEqual(p.index[date(2014, 5, 12), "C"], 12)


        # Allow a different value to be set
        other = Table(example_list, value=3)
        self.assertEqual(other.n, 4)
        self.assertEqual(len(other.index), 8)
        self.assertTrue(abs(other.index[date(2014, 5, 12), "C"] - 3.4) < 0.001)
        self.assertTrue(abs(other.index[date(2014, 5, 14), "B"] - 1.2) < 0.001)

        # Test without a header
        headerless = example_list[1:]
        h = Table(headerless, header=False)
        self.assertEqual(p.n, 4)
        self.assertEqual(len(p.index), 8)

        # The string output of the next three tables should all be equal
        # Invert the category axes
        p1 = Table(example_list, x=1)
        s1 = str(p1)

        p2 = Table(example_list, x=1, y=0)
        s2 = str(p2)
        self.assertEqual(s1, s2)

        p3 = Table(example_list, x=1, y=0, value=2)
        s3 = str(p3)
        self.assertEqual(s2, s3)
        

if __name__ == '__main__':
    unittest.main()
