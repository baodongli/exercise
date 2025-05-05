#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0 for i in range(n + 1)]
    max_v = 0
    '''
    for q in queries:
        for index in range(q[0] - 1, q[1]):
            arr[index] += q[2]
            max_v = max(max_v, arr[index])
    '''
    for q in queries:
        arr[q[0] - 1] += q[2]
        arr[q[1]] -= q[2]
    
    sum = 0    
    for v in arr:
        sum += v
        max_v = max(max_v, sum)
    return max_v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

