#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    costs = sorted(c, reverse=True)
    total_costs = 0
    for i, c in enumerate(costs):
        fno = i // k
        if fno >= 1:
            total_costs += (fno + 1) * c
        else:
            total_costs += c
    return total_costs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
