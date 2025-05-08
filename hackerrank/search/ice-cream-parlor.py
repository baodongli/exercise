#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    costmap = dict()
    for id, c in enumerate(cost):
        if c not in costmap:
            costmap[c] = []
        costmap[c].append(id + 1)
    for c in sorted(costmap.keys()):
        if money > c and (money-c) in costmap:
            if c == money-c:
                if len(costmap[c]) >= 2:
                    print(costmap[c][0], costmap[c][1])
                    break
            else:
                id1 = min(costmap[c][0], costmap[money-c][0])
                id2 = max(costmap[c][0], costmap[money-c][0])
                print(id1, id2)
                break

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
