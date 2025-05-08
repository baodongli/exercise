#!/bin/python3
import bisect
import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

        
def maximumSum(a, m):
    # Write your code here
    
    # Find the next larger mod than mval out of 
    # those calculated so far.
    # The sum between the two items results in the largest
    # mod between all the subarays from [0 .. this item]
    # The resulting mod between the two items can be calculated
    # as mval - next_larger_mval + m
    def findNextMod(mval, prev_mods):
        index = bisect.bisect_left(prev_mods, mval)
        if index != len(prev_mods):
            if prev_mods[index] != mval:
                next = prev_mods[index]
                prev_mods.insert(index, mval)
                return next
            if index + 1 < len(prev_mods):
                return prev_mods[index+1]
        else:
            prev_mods.insert(index, mval)
        return m
    
    maxmod = 0
    sum = 0
    prev_mods = []
    for i in range(len(a)):
        sum += a[i]
        cur_mod = sum % m
        nextmod = findNextMod(cur_mod, prev_mods)
        maxmod = max(maxmod, cur_mod, a[i] % m, cur_mod - nextmod + m)

    return maxmod



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
