#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    maxSum = [0 for _ in range(len(arr))]
    maxSum[0] = arr[0]
    maxSum[1] = max(arr[0], arr[1])
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return maxSum[-1]
    result = maxSum[-1]
    for index in range(2, len(arr)):
        maxSum[index] = max(maxSum[index - 2], maxSum[index - 2] + arr[index], maxSum[index - 1], arr[index])
        result = max(result, maxSum[index])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

