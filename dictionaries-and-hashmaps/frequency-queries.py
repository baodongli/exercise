#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    value_freq = {}
    freq_value_count = {}
    answers = []
    for (op, value) in queries:
        if op == 1:
            if value in value_freq and value_freq[value] > 0:
                freq = value_freq[value]
                freq_value_count[freq] -= 1
            value_freq[value] = value_freq.get(value, 0) + 1
            freq = value_freq[value]
            freq_value_count[freq] = freq_value_count.get(freq, 0) + 1
        elif op == 2:
            if value in value_freq and value_freq[value] > 0:
                freq = value_freq[value]
                freq_value_count[freq] -= 1
                value_freq[value] -= 1

                freq_value_count[value_freq[value]] = freq_value_count.get(value_freq[value], 0) + 1
        elif op == 3:
            answers.append(1 if freq_value_count.get(value, 0) > 0 else 0)

    return answers




    return answers

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
