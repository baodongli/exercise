#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    num_count = {}
    second_count = {}
    count = 0
    for v in arr:
        num_count[v] = num_count.get(v, 0) + 1
        if not v % r:
            second_count[v] = second_count.get(v, 0) + num_count.get(v // r, 0)
        if not v % (r * r):
            count += second_count.get(v // r, 0)
        
    # when ratio is 1, it's a combination of 3
    if r == 1:
        count = 0
        for cnt in num_count.values():
            count += (cnt) * (cnt - 1) * (cnt - 2) // 6
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
