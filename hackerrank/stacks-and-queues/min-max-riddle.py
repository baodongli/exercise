#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    max_win = [0 for i in range(len(arr))]
    arr = arr.copy() + [-1]
    stack = []
    for i in range(len(arr)):
        prev_i = i    
        while len(stack) > 0 and stack[-1][1] >= arr[i]:
            prev_i, value = stack.pop()
            window = i - prev_i - 1
            max_win[window] = max(max_win[window], value)
        stack.append((prev_i, arr[i]))
    for n in range(len(max_win)-2,0,-1):
        max_win[n] = max(max_win[n], max_win[n+1])
    return max_win
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
