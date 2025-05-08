#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    triplesum = 0
    # duplicates must be removed
    na = sorted(set(a))
    nb = sorted(set(b))
    nc = sorted(set(c))
    ia = 0
    ic = 0
    for bval in nb:
        while ia < len(na) and na[ia] <= bval:
            ia += 1
        while ic < len(nc) and nc[ic] <= bval:
            ic += 1
        triplesum += ia * ic
    return triplesum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
