#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#
    
def possible_moves(grid, cell, visited):
    x, y = cell
    for move in range(x - 1, -1, -1):
        if grid[move][y] == 'X':
            break
        elif visited.get((move, y), False):
            continue
        else:
            yield (move, y) 
    for move in range(x + 1, len(grid)):
        if grid[move][y] == 'X':
            break
        elif visited.get((move, y), False):
            continue
        else:
            yield (move, y) 
    for move in range(y - 1, -1, -1):
        if grid[x][move] == 'X':
            break
        elif visited.get((x, move), False):
            continue
        else:
            yield (x, move) 
            
    for move in range(y + 1, len(grid[0])):
        if grid[x][move] == 'X':
            break
        elif visited.get((x, move), False):
            continue
        else:
            yield (x, move)
    
def minimumMoves(grid, startX, startY, goalX, goalY):
    sk = deque()
    visited = {}
    sk.append(((startX, startY), 0))
    current_cell = None
    minsteps = 10 ** 9
    while sk:
        current_cell, steps = sk.popleft()
        for move in possible_moves(grid, current_cell, visited):
            if move == (goalX, goalY):
                minsteps = min(steps + 1, minsteps)
            else:
                sk.append((move, steps + 1))
                visited[move] = True
    return minsteps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()

