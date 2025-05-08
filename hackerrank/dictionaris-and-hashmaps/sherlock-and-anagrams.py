#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def getCount(count):
    return (count * (count - 1)) // 2


def sherlockAndAnagrams(s):
    # Write your code here
    sub_strs = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs = "".join(sorted(s[i:j+1]))
            sub_strs[subs] = sub_strs.get(subs, 0) + 1
    count = 0
    for cnt in sub_strs.values():
        count += getCount(cnt)

    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
