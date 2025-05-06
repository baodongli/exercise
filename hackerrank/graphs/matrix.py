#!/bin/python3

import math
import os
import random
#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY roads
#  2. INTEGER_ARRAY machines
#

'''
def minTime(roads, machines):
    # Write your code here
    neighbors = dict()
    costs = dict()
    for r in roads:
        c1, c2, cost = r
        if c1 not in neighbors:
            neighbors[c1] = []
        if c2 not in neighbors:
            neighbors[c2] = []
        neighbors[c1].append(c2)
        costs[(c1, c2)] = cost
        neighbors[c2].append(c1)
        costs[(c2, c1)] = cost
        
    visited = set()
    found = set()
    destroys = set()
    def dsf(prev, lowest_cost, lowest_city_pairs):
        city = prev[-1]
        if city in visited:
            return
        visited.add(city)
        for neighbor in neighbors[city]:
            if neighbor not in visited:
                current_lowest_cost = lowest_cost
                current_lowest_city_pairs = lowest_city_pairs
                if costs[(city, neighbor)] < current_lowest_cost:
                    current_lowest_cost = costs[(city, neighbor)]
                    current_lowest_city_pairs = (min(city, neighbor), max(city, neighbor))
                if neighbor in machines:
                    destroys.add(current_lowest_city_pairs)
                    found.add((min(city, neighbor), max(city, neighbor)))
                dsf(prev + [neighbor], current_lowest_cost, current_lowest_city_pairs)
            
    max_paths = len(machines) * (len(machines) - 1) // 2
    for m in machines:
        if len(found) < max_paths:
            visited = set()
            dsf([m], math.inf, (0, 0))
            
    destroy_cost = 0
    for d in destroys:
        destroy_cost += costs[d]
    
    #print(destroy_cost)
    return destroy_cost
'''
class Set:
    def __init__(self, city, machine):
        self.cities = set([city])
        self.machine = machine

def minTime(roads, machines):
    total = 0
    mach = set(machines)
    city_to_set = dict()
    for c1, c2, t in sorted(roads, key=lambda x: x[2], reverse=True):
        # add new sets for the cities if they don't have one yet
        city_to_set[c1] = city_to_set.get(c1, Set(c1, c1 in mach))
        city_to_set[c2] = city_to_set.get(c2, Set(c2, c2 in mach))
        # get the sets
        s1, s2 = city_to_set[c1], city_to_set[c2]
        # if already in the same set, skip
        if s1 == s2:
            continue
        # if they both containe machines, add to total
        if s1.machine and s2.machine:
            total += t
            continue
        # 1 or less are machines, so merge the sets
        s1.cities.update(s2.cities)
        # update if combined set contains machines
        s1.machine = s1.machine or s2.machine
        # update the city to set mapping
        for c in s2.cities:
            city_to_set[c] = s1

    return total
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input().strip())
        machines.append(machines_item)

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
