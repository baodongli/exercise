#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    i = 0
    swap = 0
    while i < len(a):
        j = 0
        while j < len(a) - i - 1:
            if a[j] > a[j+1]:
                swap += 1
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1

    print("Array is sorted in %d swaps." % swap)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[len(a)-1])
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
