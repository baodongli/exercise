#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    too_chaotic = False
    
    stack = []
    for p in range(len(q)):
        if q[p] - p > 3:
            too_chaotic = True
            break
        else:
            if not stack or q[p] > stack[-1]:
                stack.append(q[p])
            else:
                ahead = []
                while stack and q[p] < stack[-1]:
                    ahead.append(stack.pop())
                    bribes += 1
                stack.append(q[p])
                while ahead:
                    stack.append(ahead.pop())
                # print(stack)  
            
    print(bribes if not too_chaotic else "Too chaotic")

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
