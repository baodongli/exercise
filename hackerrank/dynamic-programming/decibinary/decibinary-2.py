#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decibinaryNumbers' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER x as parameter.
#

class DeciBinarySystem:
    def __init__(self, maxValue, num_of_digits):
        self.dbValues = []
        self.maxDecival = maxValue
        self.total = 0
        #self.Populate()
        self.powerof2 = dict()
        self.powerof10 = dict()
        for i in range(20):
            self.powerof2[i] = 2 ** i
            self.powerof10[i] = 10 ** i

        self.num_of_digits = num_of_digits
        self.dbCountTbl = [[0 for _ in range(num_of_digits + 1)] for _ in range(self.maxDecival + 1)]
        self.countBefore = [0 for _ in range(self.maxDecival + 2)]
        self.GenerateDBCountTable()
        self.decibinaries = dict()

    def GenerateRow(self, dv):
        counts = self.dbCountTbl[dv]
        counts[0] = 0
        if dv < 10:
            counts[1] = 1
        else:
            counts[1] = 0
            
        for digit in range(2, self.num_of_digits + 1):
            counts[digit] = counts[digit-1]
            count_back_dv = self.powerof2[digit - 1]
            for back_digit in range(1, 10):
                back_dv = dv - back_digit * count_back_dv
                if back_dv >= 0:
                    counts[digit] += self.dbCountTbl[back_dv][digit-1]
                else:
                    break

    def GenerateDBCountTable(self):
        self.dbCountTbl[0] = [1 for _ in range(self.num_of_digits + 1)]
        self.dbCountTbl[1] = [1 for _ in range(self.num_of_digits + 1)]
        self.dbCountTbl[1][0] = 0
        for dv in range(2, self.maxDecival + 1):
            self.GenerateRow(dv)
        for dv in range(1, self.maxDecival + 2):
            self.countBefore[dv] = self.countBefore[dv - 1] + self.dbCountTbl[dv - 1][-1]
    
    def FindDecibinary(self, index):
        start = 0
        end = self.maxDecival + 1
        dv = 0

        while index > self.countBefore[end]:
            self.maxDecival += 1
            dv = self.maxDecival
            self.dbCountTbl.append([0 for _ in range(self.num_of_digits + 1)])
            self.GenerateRow(dv)
            self.countBefore.append(0)
            self.countBefore[dv] = self.countBefore[dv - 1] + self.dbCountTbl[dv - 1][-1]
            end = self.maxDecival + 1
            self.countBefore[end] = self.countBefore[end - 1] + self.dbCountTbl[end - 1][-1]
        
        #for k, v in enumerate(self.dbCountTbl):
        #    print(k, v)
        #print(self.countBefore)

        while True:
            dv = (start + end) // 2
            if dv == start:
                break
            if index > self.countBefore[dv]:
                start = dv
            elif index <= self.countBefore[dv]:
                end = dv

        # dv is the corresponding decimal value
        dv_index = index - self.countBefore[dv]
        return self.GetDecibinaryValue(dv, dv_index)

    def GetDecibinaryValue(self, dv, dv_index):
        #import pdb; pdb.set_trace()
        if dv == 0:
            return 0

        if (dv, dv_index) in self.decibinaries:
            return self.decibinaries[(dv, dv_index)]

        dv_counts = self.dbCountTbl[dv]
        digit = 0
        start = 0
        end = self.num_of_digits
        while start != end:
            digit = (start + end) // 2
            if dv_index > dv_counts[digit]:
                start = digit + 1
            else:
                end = digit        
        digit = end
        dv_count = dv_index - dv_counts[digit-1]
        count_back_dv = self.powerof2[digit - 1]
        cur_digit = 1
        back_dv = dv - count_back_dv
        while back_dv > 0 and dv_count > self.dbCountTbl[back_dv][digit - 1]:
            dv_count -= self.dbCountTbl[back_dv][digit- 1]
            back_dv -= count_back_dv
            cur_digit += 1
        
        db = (cur_digit) * self.powerof10[digit-1] + self.GetDecibinaryValue(back_dv, dv_count)
        self.decibinaries[(dv, dv_index)] = db
        return db

dbSystem = DeciBinarySystem(1000, 19)
found = dict()
def decibinaryNumbers(x):
    # Write your code here
    if x not in found:
        found[x] = (dbSystem.FindDecibinary(x))
    return found[x]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = decibinaryNumbers(x)

        fptr.write(str(result) + '\n')

    fptr.close()
