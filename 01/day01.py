#! /bin/env python3

"""
This file is part of solutions for my advent of code 2023 (https://github.com/mdtrooper/advent-of-code-2023-python).
Copyright (c) 2023 Miguel de Dios Matias (tres.14159@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

# https://adventofcode.com/2023/day/1

def day01(data):
    num_in_chars = [[c for c in line if c.isdigit()] for line in data]
    s = 0
    for group in num_in_chars:
        if group == num_in_chars[-1]:
            group = group * 2
        if (len(group) > 2):
            num = int(''.join([group[0], group[-1]]))
        else:
            num = int(''.join(group))
        print(num, end=', ')
        s += num
    print(f"\nSUM: {s}")
    return s
