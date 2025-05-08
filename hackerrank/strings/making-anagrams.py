#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    a_count = {}
    b_count = {}
    for c in a:
        a_count[c] = a_count.get(c, 0) + 1
    for c in b:
        b_count[c] = b_count.get(c, 0) + 1
    
    k1 = set(a_count.keys())
    k2 = set(b_count.keys())
    
    intersect_k = k1.intersection(k2)
    
    xor_k = k1 ^ k2
    
    deletes = 0
    for k in xor_k:
        deletes += a_count.get(k, 0) + b_count.get(k, 0)
        
    for k in intersect_k:
        deletes += abs(a_count[k] - b_count[k])
        
    return deletes   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
