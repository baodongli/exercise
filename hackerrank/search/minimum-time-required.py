#!/bin/python3

import math
import os
import random
import re
import sys

def getCount(dayCounts, days):
    count = 0
    for ndays, nmachines in dayCounts.items():
        count += (days // ndays) * nmachines
    return count
        
# Complete the minTime function below.
def minTime(machines, goal):
    dayCounts = dict()
    maxDays = 0
    minDays = math.inf
    for m in machines:
        dayCounts[m] = dayCounts.get(m, 0) + 1
        maxDays = max(maxDays, m)
        minDays = min(minDays, m)
    low_days = goal // len(machines) * minDays
    high_days = (goal + len(machines) - 1) // len(machines) * maxDays
    
    #print(minDays, maxDays, goal)
    #print(low_days, high_days)
    while low_days != high_days:
        mid = (low_days + high_days) // 2
        count = getCount(dayCounts, mid)
        #print(dayCounts, mid, count)
        if count >= goal:
            high_days = mid
        elif count < goal:
            low_days = mid + 1
    return high_days    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
