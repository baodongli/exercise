#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def findMedian(counter, d):
    count = 0
    median = 0

    if d%2 != 0:
        for i in range(len(counter)):
            count += counter[i]
            if count > d//2:
                median = i
                break
    else:
        first = 0
        second = 0
        for i, _ in enumerate(counter):
            count += counter[i]
            if first == 0 and count >= d//2:
                first = i
            if second == 0 and count >= d//2 + 1:
                second = i
                break
        median = (first+second) / 2
    return median


def activityNotifications(expenditure, d):
    count = 0
    counter = [0]*201
    
    # This is counter sorting since the data is between 0 .. 200 inclusively.
    for exp in range(d):
        counter[expenditure[exp]] += 1

    for i in range(d, len(expenditure)):
        new = expenditure[i]
        old = expenditure[i-d]
        median = findMedian(counter, d)
        
        if new >= 2*median:
            count += 1
            
        counter[old] -= 1
        counter[new] += 1
        
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
