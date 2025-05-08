#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    matrix = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

    for row_i in range(len(s1)):
        for col_i in range(len(s2)):
            if s1[row_i] == s2[col_i]:
                matrix[row_i + 1][col_i + 1] = matrix[row_i][col_i] + 1
            else:
                matrix[row_i + 1][col_i + 1] = \
                    max(matrix[row_i + 1][col_i], matrix[row_i][col_i + 1])

    return matrix[len(s1)][len(s2)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
