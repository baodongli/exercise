#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    i = 1
    count = 0
    last = 0
    repeat = 1
    while i < n:
        
        def repeat_count(n):
            sum = 0
            for i in range(1, n+1):
                sum += i
            return sum

        if s[i] == s[last]:
            repeat += 1
        else:
            count += repeat_count(repeat)
            for j in range(1, i + 1):
                if i+j < n and i-j >= 0 and s[i+j] == s[last] and s[i + j] == s[i - j]:
                    count += 1
                else:
                    break
            repeat = 1;
            last = i
        i += 1
    return count + repeat_count(repeat)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
