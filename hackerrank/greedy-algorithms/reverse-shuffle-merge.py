#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys

#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    # Write your code here
    #num of chars that remain to be traversed
    remain_chars = Counter(s)
    #num of chars that have to be included
    used_chars = {key:remain_chars[key]// 2 for key in remain_chars.keys()}

    res = []
    def can_use(char):
        return used_chars[char] > 0
        
    def can_pop(char):
        return remain_chars[char] > used_chars[char]
        
    for char in reversed(s):
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] += 1
            used_chars[char] -= 1
            res.append(char)
        remain_chars[char] -= 1
    return "".join(res)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
