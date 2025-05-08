#!/bin/python3

import math
import os
import random
import re
import sys

'''
class Person:
    def __init__(self, id):
        self.id = id
        self.friends = set([id])

# Complete the maxCircle function below.
def maxCircle(queries):
    people = dict()
    ans = []
    largest_group_size = 0
    for (p1, p2) in queries:
        P1 = people.get(p1, None)
        P2 = people.get(p2, None)
        if P1 is None:
            P1 = people[p1] = Person(p1)
        if P2 is None:
            P2 = people[p2] = Person(p2)
            
        if P1.friends is not P2.friends:
            if len(P1.friends) < len(P2.friends):
                P1, P2 = P2, P1
            
            P1.friends.update(P2.friends)
            for f in P2.friends:
                people[f].friends = P1.friends
            P2.friends = P1.friends
        largest_group_size = max(largest_group_size, len(P1.friends))
        ans.append(largest_group_size)
    return ans
'''

# The following method doesn't require a lot of storage for sets
# It actually builds trees and 
# always update the size at the top of the tree
class Person:
    def __init__(self, id):
        self.id = id
        self.size = 1
        self.parent = self
    
    def findRoot(self, people):
        root = self
        while root.parent != root:
            root = root.parent
        return root
            

def maxCircle(queries):
    people = dict()
    ans = []
    largest_group_size = 0
    for (p1, p2) in queries:
        P1 = people.get(p1, None)
        P2 = people.get(p2, None)
        if P1 is None:
            P1 = people[p1] = Person(p1)
        if P2 is None:
            P2 = people[p2] = Person(p2)
        P1 = P1.findRoot(people)    
        P2 = P2.findRoot(people)
        if P1 is not P2:
            if P1.size < P2.size:
                P1, P2 = P2, P1
            P2.parent = P1
            P1.size += P2.size
        largest_group_size = max(largest_group_size, P1.size)
        ans.append(largest_group_size)
    return ans
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
