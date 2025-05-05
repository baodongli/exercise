#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# Keeping state with one iteration
def candies(n, arr):
    # Write your code here
    if len(arr) <= 1:
        return 1

    if arr[1] > arr[0]:
        up_count = 2
        down_count = 0
        state = 'up'
        candies = 3
    elif arr[1] < arr[0]:
        down_count = 2
        up_count = 0
        state = 'down'
        candies = 3
    else:
        up_count = 1
        down_count = 0
        state = 'even'
        candies = 2

    for idx in range(2, len(arr)):
        if arr[idx] > arr[idx - 1]:
            if state != 'up':
                up_count = 1
                state = 'up'
            up_count += 1
            candies += up_count
        elif arr[idx] == arr[idx - 1]:
            candies += 1
            state = 'even'
            up_count = 1
        else:
            if state != 'down':
                down_count = 1
                state = 'down'
            else:
                down_count += 1
            candies += down_count
            if idx + 1 >= len(arr) or arr[idx + 1] >= arr[idx]:
                if up_count > 0 and down_count + 1  > up_count:
                    candies += down_count + 1  - up_count

    return candies

'''
# Neat but requires two iterations
def candies(n, arr):
    # Write your code here
    total_candy = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            total_candy[i] = total_candy[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            total_candy[i] = max(total_candy[i], total_candy[i + 1] + 1)
    
    # The result is the sum of all total_candy
    return sum(total_candy)
'''                          
                  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
