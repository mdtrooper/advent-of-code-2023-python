#! /bin/env python3

"""
This file is part of solutions for my advent of code 2023 (https://github.com/mdtrooper/advent-of-code-2023-python).
Copyright (c) 2023 Miguel de Dios Matias (tres.14159@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

# https://adventofcode.com/2023/day/1

def day01(data, part_exercice=1):
    # Part 2
    if part_exercice == 2: 
        numbers_english = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for (i, line) in enumerate(data):
            # (position, digit, word)
            while True:
                changes = [(i, digit, word) for (i, digit, word) in [(line.find(word), digit, word) for (digit, word) in enumerate(numbers_english)] if i != -1]
                changes.sort(key= lambda item: item[0])
                if len(changes) == 0:
                    break
                line = line.replace(changes[0][2], f'{changes[0][1] + 1}')
            data[i] = line
    
    # Part 1
    print()
    num_in_chars = [[c for c in line if c.isdigit()] for line in data]
    s = 0
    for group in num_in_chars:
        if (len(group) == 0):
            num = 0
        if (len(group) == 1):
            num = int(group[0]) * 11
        elif (len(group) > 2):
            num = int(''.join([group[0], group[-1]]))
        else:
            num = int(''.join(group))
        print(num, end=', ')
        s += num
    print()
    print(f"SUM: {s}")
    return s
