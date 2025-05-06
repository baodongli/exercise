#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
def countInversions(arr):
    # Write your code here
    stack = [arr[0]]
    index = 1
    swaps = 0
    while index < len(arr):
        value = arr[index]
        bindex = index
        while stack and value < stack[-1]:
            arr[bindex] = stack.pop()
            swaps += 1
            bindex -= 1
        stack.append(value)
        index = bindex + 1
    return swaps
'''

def merge(array, sorted1, sorted2):
    result = array
    i = j = r = 0
    swap = 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] <= sorted2[j]:
            result[r] = sorted1[i]
            i += 1
#            if r != i:
#                swap += 1         
        else:
            result[r] = sorted2[j]
            swap += len(sorted1) - i
            j += 1
        r += 1
    while i < len(sorted1):
        result[r] = sorted1[i]
        i += 1
        r += 1
    while j < len(sorted2):
        result[r] = sorted2[j]
        j += 1
        r += 1
            
    return swap
        
def mergeSort(arr):
    if len(arr) > 1:
        mid = (len(arr)) // 2
        left = arr[:mid]
        right = arr[mid:]
        swapleft = mergeSort(left)
        swapright = mergeSort(right)
        swap = merge(arr, left, right)
        return swapleft + swapright + swap
    return 0
    

def countInversions(arr):
    return mergeSort(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
