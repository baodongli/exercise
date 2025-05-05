#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    if len(arr) == 1:
        return 0
    swaps = 0
    index = 0
    while index < len(arr):
        v = arr[index]
        if v != index + 1:
            swaps += 1
            arr[index] = arr[v - 1]
            arr[v - 1] = v
        else:
            index += 1        
            
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
