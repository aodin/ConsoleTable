# -*- coding: utf-8 -*-
import unittest

from consoletable.parser import Parser


example = [
    ("2014-05-11","A",4),
    ("2014-05-12","A",3),
    ("2014-05-12","A",1),
    ("2014-05-14","A",6),
    ("2014-05-14","A",1),
    ("2014-05-11","B",2),
    ("2014-05-11","B",1),
    ("2014-05-11","B",1),
    ("2014-05-14","B",1),
    ("2014-05-12","C",4),
    ("2014-05-12","C",8),
    ("2014-05-13","C",1),
    ("2014-05-13","C",2),
    ("2014-05-14","C",1),
]

class TestParser(unittest.TestCase):

    def setUp(self):
        pass

    def test_list(self):
        p = Parser(example)
        self.assertTrue(p)


if __name__ == '__main__':
    unittest.main()