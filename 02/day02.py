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

def main():
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
    playsLines = open('/tmp/input').read().split('\n')
    playsDirty = {int(play.split(':')[0].replace('Game', '')): play.split(':')[1] for play in playsLines if len(play) > 0}
    plays = {key: [getCubes(value) for value in value.split(';')] for key, value in playsDirty.items()}
    
    
    # Check posible games
    r = 12
    g = 13
    b = 14
    for game, p in plays.items():
        posibles = {key: len([p for p in value if p.get('r', 0) < r and p.get('g', 0) < g and p.get('b', 0) < b]) > 0 for key, value in plays.items()}
    print(f'The code is {sum([key for key, value in posibles.items() if value])}')

if __name__ == '__main__':
    main()
