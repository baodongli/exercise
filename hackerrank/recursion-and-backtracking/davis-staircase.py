#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def _stepPerms(n, memo):
    if n in memo:
        return memo[n]
    if n < 0:
        memo[n] = 0
        return 0
    if n == 0:
        memo[0] = 1
        return 1
    steps = _stepPerms(n-1, memo) + _stepPerms(n-2, memo) + _stepPerms(n-3, memo)
    memo[n] = steps
    return steps

def stepPerms(n):
    # Write your code here
    memo = dict()
    return _stepPerms(n, memo)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

