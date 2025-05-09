#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    sea_level = 0
    under_sea_level = False
    for s in range(steps):
        if path[s] == 'U':
            sea_level += 1
            if sea_level == 0 and under_sea_level:
                valleys += 1
                under_sea_level = False
        elif path[s] == 'D':
            sea_level -= 1
            if sea_level < 0:
                under_sea_level = True
    return valleys
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
