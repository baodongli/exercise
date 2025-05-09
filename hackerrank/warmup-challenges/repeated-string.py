#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count = 0
    lesser = min(len(s), n)
    for ch in range(lesser):
        if s[ch] == 'a':
            count += 1
    if n < len(s):
        return count
    
    num_of_s = n // len(s)
    rem = n % len(s)
    count *= num_of_s
    for i in range(rem):
        if s[i] == 'a':
            count += 1
    return count
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
