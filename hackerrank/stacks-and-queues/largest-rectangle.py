#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Write your code here
    sk = []
    index = 0
    largest = 0
    while index < len(h) or sk:
        if (not sk) or (index < len(h) and (h[index] >= h[sk[-1]])):
            sk.append(index)
            index += 1
        else:
            top_index = sk.pop()
            area = h[top_index] * ((index - sk[-1] - 1) if sk else index)
            largest = max(largest, area)
    
    return largest
        
   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
