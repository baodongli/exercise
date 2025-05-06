#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#
def poisonousPlants(p):
    mday,s = 0, []
    for i in p:
        if not(s) or i <= s[0][0]:
            s=[[i,0]]
        elif i > s[-1][0]:
            s.append([i,1])
        else:
            d = 1
            while s and i <= s[-1][0]:
                d = max(d, s.pop()[1]+1)
            s.append([i,d])
        mday = max(mday,s[-1][1])

    return mday
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

