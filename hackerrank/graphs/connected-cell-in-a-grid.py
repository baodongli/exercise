#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    # Write your code here
    visited = defaultdict(bool)
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])
    max_region_size = 0
    for row in range(num_of_rows):
        for column in range(num_of_cols):
            if not visited[(row, column)] and grid[row][column] == 1:
                visited[(row, column)] = True
                region = [(row, column)]
                region_size = 1
                while region:
                    row, column = region.pop()
                    neighbor_cells = [(row-1, column),
                                      (row-1, column-1),
                                      (row-1, column+1),
                                      (row+1, column),
                                      (row+1, column+1),
                                      (row+1, column-1),
                                      (row, column-1),
                                      (row, column+1)]
                                      
                    for r, c in neighbor_cells:
                        if r >= 0 and r < num_of_rows and c >= 0 and c < num_of_cols:
                            if not visited[(r, c)] and grid[r][c] == 1:
                                region_size += 1
                                region.append((r, c))
                                visited[(r, c)] = True
                max_region_size = max(max_region_size, region_size)
    return max_region_size  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
