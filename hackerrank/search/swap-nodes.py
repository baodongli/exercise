#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def buildTreeFromIndexes(indexes):
    nodes = dict()
    nodes[1] = root = Node(1, None, None)
    for node_id, (left, right) in enumerate(indexes):
        node = node_id + 1
        if left > 0:
            nodes[node].left = nodes[left] = Node(left, None, None)
        if right > 0:
            nodes[node].right = nodes[right] = Node(right, None, None)
        
    ''' Another way to build the tree with a queue
    root = Node(1, None, None)
    nodes = deque([root])

    for index in indexes:
        node = nodes.popleft()
        if index[0] != -1:
            node.left = Node(index[0], None, None)
            nodes.append(node.left)

        if index[1] != -1:
            node.right = Node(index[1], None, None)
            nodes.append(node.right)
    '''
    return root
    
def inOrderTraversal(root, depth):
    if not root:
        return []
    ans = []
    stack = []
    current = root

    cur_depth = 1
    while stack or current:
        while current:
            if cur_depth % depth == 0:
                current.left, current.right = current.right, current.left
            cur_depth += 1
            stack.append((current, cur_depth))
            current = current.left

        current, cur_depth = stack.pop()
        ans.append(current.value)
        current = current.right

    return ans


def swapNodes(indexes, queries):
    # Write your code here
    root = buildTreeFromIndexes(indexes)
    result = []
    for depth in queries:
        result.append(inOrderTraversal(root, depth))
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
