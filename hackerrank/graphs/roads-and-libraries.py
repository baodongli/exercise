#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
class Node:
    def __init__(self, num):
        self.num = num
        self.visited = False
        self.edges = []
    
    def addEdge(self, neighbor):
        self.edges.append(neighbor)
    
    def markVisited(self):
        self.visited = True
    
    def isVisited(self):
        return self.visited
        
    def getEdges(self):
        return self.edges

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib < c_road:
        return c_lib * n

    rlg = dict()
    
    for city in cities:
        if city[0] not in rlg:
            rlg[city[0]] = Node(city[0])
        if city[1] not in rlg:
            rlg[city[1]] = Node(city[1])
        rlg[city[0]].addEdge(rlg[city[1]])
        rlg[city[1]].addEdge(rlg[city[0]])
    
    min_cost = 0
    for c in range(1, n+1):
        if c not in rlg:
            min_cost += c_lib
            continue
        if rlg[c].isVisited():
            continue     
        region = [rlg[c]]
        rlg[c].markVisited()
        num_of_roads = 0
        num_of_nodes = 0
        while region:
            node = region.pop()
            num_of_nodes += 1
            for nei_city in node.getEdges():
                if not nei_city.isVisited():
                    nei_city.markVisited()
                    region.append(nei_city)
                    num_of_roads += 1
        cost = c_lib + num_of_roads * c_road
        min_cost += cost
        
    return min_cost
                
        

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
