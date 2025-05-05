#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    # Write your code here
    '''
    starting_pos = (d + len(a)) % (len(a))
    count = 0
    rota = []
    while count < len(a):
        rota.append(a[starting_pos])
        starting_pos = (starting_pos + 1) % (len(a))
        count += 1
    '''
    rota = []
    for i in range(len(a)):
        rota.append(a[(d + len(a) + i) % len(a)])
    return rota

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
