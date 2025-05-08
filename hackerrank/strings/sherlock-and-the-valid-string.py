#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    occurence = {}
    for ch in s:
        occurence[ch] = occurence.get(ch, 0) + 1
    
    # for each occurrence count, how many characters are there.
    ch_times = {}
    for k, v in occurence.items():
        ch_times[v] = ch_times.get(v, 0) + 1   
    
    # more than 3 characters, each of them appear different number of times
    if len(ch_times) > 2:
        return "NO"
    # all the characters appear the same number of times.
    if len(ch_times) == 1:
        return "YES"
    
    # the occurrence count
    oc = list(ch_times.keys())
    # the number of characters
    num_ch = list(ch_times.values())
    
    # if one of the character appears only once, all the other appear the same number of times
    if oc[0] == 1 and num_ch[0] == 1:
        return "YES"
    if oc[1] == 1 and num_ch[1] == 1:
        return "YES"
    
    # if one of the characters appear more than once,
    # and its occurrence count is only 1 from all the other characters
    if num_ch[0] == 1 and oc[0] - oc[1] == 1:
        return "YES"
    if num_ch[1] == 1 and oc[1] - oc[0] == 1:
        return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
