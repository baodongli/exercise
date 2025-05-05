#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def _abbreviation(a, b, apos, bpos, result):
    if (apos, bpos) in result:
        return result[(apos, bpos)]
    if bpos == len(b):
        # when there are still upper-case chars left in 'a'
        # return False to backtrack
        # It's possible that 'a' and 'b' still match later.
        for ch in a[apos:]:
            if ch.isupper():
                result[(apos, bpos)] = False
                return False
        result[(apos, bpos)] = True
        return True
    if len(a) - apos < len(b) - bpos:
        result[(apos, bpos)] = False
        return False

    #import pdb; pdb.set_trace()
    for pos in range(apos, len(a)):
        if a[pos].upper() == b[bpos]:
            match = _abbreviation(a, b, pos + 1, bpos + 1, result)
            if match:
                result[(apos, bpos)] = True
                return True
            else:
                if a[pos].isupper():
                    result[(apos, bpos)] = False
                    return False
                    
        elif a[pos].isupper():
            result[(apos, bpos)] = False
            return False
    result[(apos, bpos)] = False
    return False

def abbreviation(a, b):
    return "YES" if _abbreviation(a, b, 0, 0, {}) else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
