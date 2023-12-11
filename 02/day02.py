#! /bin/env python3

"""
This file is part of solutions for my advent of code 2023 (https://github.com/mdtrooper/advent-of-code-2023-python).
Copyright (c) 2023 Miguel de Dios Matias (tres.14159@gmail.com)

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 
"""

# File with the plays
# https://adventofcode.com/2023/day/2/input

def getCubes(hand):
    r = {}
    for cubes in hand.split(','):
        num, color = cubes.strip().split(' ')
        if color == 'green':
            r['g'] = int(num)
        if color == 'blue':
            r['b'] = int(num)
        if color == 'red':
            r['r'] = int(num)
    return r

def lines2Plays(lines):
    playsDirty = {int(play.split(':')[0].replace('Game', '')): play.split(':')[1] for play in lines if len(play) > 0}
    plays = {key: [getCubes(value) for value in value.split(';')] for key, value in playsDirty.items()}
    return plays

def day02(lines, limit_r, limit_g, limit_b):
    plays = lines2Plays(lines)
    
    # Check posible games
    posibles = {key: len([p for p in value if p.get('r', 0) > limit_r or p.get('g', 0) > limit_g or p.get('b', 0) > limit_b]) == 0 for key, value in plays.items()}
    print(posibles)
    print()
    return sum([key for key, value in posibles.items() if value])

def day02Part02(lines):
    plays = lines2Plays(lines)
    count = 0
    for _, p in plays.items():
        maxR = maxG = maxB = 0
        for i in p:
            maxR = max(maxR, i.get('r', 0))
            maxG = max(maxG, i.get('g', 0))
            maxB = max(maxB, i.get('b', 0))
        count += (maxR * maxG * maxB)
    return count

def main():
    lines = open('/tmp/input').read().split('\n')
    code = day02(lines, 12, 13, 14)
    print(f'The code for part01 is {code}')
    code = day02Part02(lines)
    print(f'The code for part01 is {code}')

if __name__ == '__main__':
    main()
