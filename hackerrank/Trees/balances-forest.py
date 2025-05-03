#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedForest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. 2D_INTEGER_ARRAY edges
#
class Node:
    def __init__(self, num, parent=0, sumval=0):
        self.num = num
        self.sumval = sumval
        self.parent = parent
        self.childs = []
        
    def addSum(self, w):
        self.sumval += w
    
    def addChild(self, child):
        self.childs.append(child)
    
    def setParent(self, parent):
        self.parent = parent

    def __repr__(self):
        return(f'num = {self.num} sumval = {self.sumval} childs = {self.childs} parent = {self.parent}\n')

def balancedForest(c, edges):
    # Write your code here
    forest = dict()
    total_sum = 0
    sorted_edges = []
    for e in edges:
        parent = forest.get(e[0], None)
        child = forest.get(e[1], None)
        
        parent_num = e[0]
        child_num = e[1]

        if parent and child and parent.parent != 0 and child.parent != 0:
            stack = [child_num]
            
            cur_parent = child.parent
            while cur_parent != 0:
                stack.append(cur_parent)
                cur_parent = forest[cur_parent].parent

            while stack:
                cur_parent = stack.pop()
                if stack:
                    cur_child = stack[-1]
                    pnode = forest[cur_parent]
                    cnode = forest[cur_child]
                    pnode.setParent(cur_child)
                    pnode.childs.remove(cur_child)
                    pnode.sumval -= cnode.sumval
                    cnode.addSum(pnode.sumval)
                    cnode.addChild(cur_parent)
                    
            child.parent = 0
        
        if child and child.parent != 0:
            child, parent = parent, child
            child_num, parent_num = parent_num, child_num
        sorted_edges.append((parent_num, child_num))
        
        subtree_sum = c[child_num-1]
        if not child:
            child = Node(child_num, parent_num, sumval=c[child_num-1])
            forest[child_num] = child
            total_sum += c[child_num-1]
        else:
            subtree_sum = child.sumval
            child.setParent(parent_num)
            
        if not parent:
            parent = Node(parent_num, sumval=c[parent_num-1]+subtree_sum)
            forest[parent_num] = parent
            total_sum += c[parent_num-1]
            parent.addChild(child_num)
        else:
            parent.addChild(child_num)
            while parent:
                parent.addSum(subtree_sum)
                parent = forest.get(parent.parent, None)

    def findSubtreeWithSum(node, cut_child, child, sumval, total):
        stack = [(node, child)]
        while stack:
            cur_node, cur_child = stack.pop()
            for c in cur_node.childs:
                if c != cut_child:
                    rem_sum = total - forest[c].sumval
                    
                    if forest[c].sumval == sumval or rem_sum == sumval:
                        return True
                    if forest[c].sumval < sumval:
                        continue
                
                    if c != cur_child:
                        stack.append((forest[c], 0))
                
            if cur_child != 0 and cur_node.parent != 0:
                stack.append((forest[cur_node.parent], cur_node.num))
        return False
            
    def findAnotherCut(node, child, less_weight, sumval):
        cur_node = node
        while cur_node:
            cur_node.sumval -= less_weight
            cur_node = forest.get(cur_node.parent, None)
        found = findSubtreeWithSum(node, child, child, sumval, total_sum - less_weight)
        cur_node = node
        while cur_node:
            cur_node.sumval += less_weight
            cur_node = forest.get(cur_node.parent, None)
        return found
        
    minval = math.inf
    visited = set()
    for e in sorted_edges:
        child = forest[e[1]]
        parent = forest[e[0]]
        if child.sumval in visited:
            continue
        visited.add(child.sumval)
        # Is it possible to add to the child side?
        if (total_sum - child.sumval) % 2 == 0:
            possible_sum = (total_sum - child.sumval) // 2
            if possible_sum >= child.sumval:
                if findAnotherCut(parent, child.num, child.sumval, possible_sum):
                    minval = min(minval, possible_sum - child.sumval)
                
        # Is it possbile to add to the parent side?
        if 3 * child.sumval > total_sum:
            addVal = 3 * child.sumval - total_sum
            if addVal == child.sumval or \
               findAnotherCut(parent, child.num, child.sumval, child.sumval):
                minval = min(minval, addVal)
    if minval != math.inf:
        return minval
    return -1            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()

