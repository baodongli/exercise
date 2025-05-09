#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jque = deque([(0, 0)])
    min_jumps = math.inf
    while jque:
        cloud, jumps = jque.popleft()
        if cloud == len(c) - 1:
            min_jumps = min(min_jumps, jumps)
        if cloud + 1 < len(c) and c[cloud + 1] == 0:
            jque.append((cloud + 1, jumps + 1))
        if cloud + 2 < len(c) and c[cloud + 2] == 0:
            jque.append((cloud + 2, jumps + 1))
    
    return min_jumps
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
