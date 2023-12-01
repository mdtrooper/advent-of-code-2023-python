#! /bin/env python3

"""
This file is part of solutions for my advent of code 2023 (https://github.com/mdtrooper/advent-of-code-2023-python).
Copyright (c) 2023 Miguel de Dios Matias (tres.14159@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

# https://adventofcode.com/2023/day/1

# python3 -m unittest day01_test.py
# or
# python3 day01_test.py
#
# or manually "hot reload"
#    watch -n 1 python3 day01_test.py

import unittest
from day01 import day01

class TestDay01(unittest.TestCase):
    def test_example_data(self):
        data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(day01(data), 142)

if __name__ == '__main__':
    unittest.main()
