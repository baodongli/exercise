#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    print(s)
    sk = list()
    sk.append(s[0])
    for c in s[1:]:
        if c == '{' or c == '(' or c == '[':
            sk.append(c)
        elif c == '}':
            if len(sk) == 0 or sk[len(sk) - 1] != '{':
                return "NO"
            sk.pop()
        elif c == ')':
            if len(sk) == 0 or sk[len(sk) - 1] != '(':
                return "NO";
            sk.pop()
        elif c == ']':
            if len(sk) == 0 or sk[len(sk) - 1] != '[':
                return "NO";
            sk.pop()
            
    if len(sk) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
