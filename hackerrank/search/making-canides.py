#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#
def minimumPasses(m, w, p, n):
    # Write your code here
    candies = 0
    npasses = 0
    min_passes = (n + m * w -1) // (m * w)
    if p > n:
        return min_passes
    while candies < n:
        npasses_no_buys = max((p - candies + m * w - 1) // (m * w), 1)
        
        # The concept of minimum passes is important
        # In some cases, buying to increase production for one pass
        # would increase the final number of passes.
        npasses += npasses_no_buys
        if npasses > min_passes:
            return min_passes
        candies += npasses_no_buys * m * w
        
        # determines how many stuff can be purchased if needed
        # Adding it to the smaller between workers and machines
        # can maximize the production (m * w). 
        num_of_buys = candies // p
        if num_of_buys > 0:
            remaining = 0
            if w > m:
                diff = w - m
                if diff < num_of_buys:
                    remaining = num_of_buys - diff
                    m = m + diff
                else:
                    m = m + num_of_buys
            else:
                diff = m - w
                if diff < num_of_buys:
                    remaining = num_of_buys - diff
                    w = w + diff
                else:
                    w = w + num_of_buys
            m += remaining // 2
            w += remaining - remaining // 2
            candies -= num_of_buys * p
            min_passes = min(npasses + (n-candies + w * m - 1) // (m*w), min_passes)

    return npasses



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
