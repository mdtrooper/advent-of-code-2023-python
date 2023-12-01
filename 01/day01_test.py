#! /bin/env python3

# python3 -m unittest day01_test.py
# or
# python3 day01_test.py

import unittest
from day01 import day01

class TestDay01(unittest.TestCase):
    def test_example_data(self):
        data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(day01(data), 142)

if __name__ == '__main__':
    unittest.main()
