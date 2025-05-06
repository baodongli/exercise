#!/bin/python3

import functools
import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
def comp(a, b):
    if a[1] == 1 and b[1] == 1:
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1
        else:
            return 0
    if a[1] == 1 and b[1] == 0:
        return 1
    if a[1] == 0 and b[1] == 1:
        return -1
    return 0
        

                    
def luckBalance(k, contests):
    # Write your code here
    conts = sorted(contests, key=functools.cmp_to_key(comp), reverse=True)
                
    max_luck = 0
    for c in conts[:k]:
        l, t = c
        max_luck += l
    for c in conts[k:]:
        l, t = c
        if t == 0:
            max_luck += l
        else:
            max_luck -= l
    return max_luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
