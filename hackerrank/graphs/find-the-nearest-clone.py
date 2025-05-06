#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodek.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    neighbors = [[] for node in range(graph_nodes)]
    for index, node in enumerate(graph_from):
        neighbors[node - 1].append(graph_to[index] - 1)    
        neighbors[graph_to[index] - 1].append(node - 1)    
    shortest_len = -1
    visited = set()
    for node, color in enumerate(ids):
        if color == val:
            # conduct BFS
            # starting from node
            if node in visited:
                continue
            visited.add(node)
            bfs_queue = deque([(nei, 1) for nei in neighbors[node]])
            while bfs_queue:
                next_node, depth = bfs_queue.popleft()
                if ids[next_node] == val:
                    if shortest_len == -1:
                        shortest_len = depth
                    else:
                        shortest_len = min(shortest_len, depth)
                    break
                visited.add(next_node)
                for neighbor in neighbors[next_node]:
                    if neighbor not in visited:
                        bfs_queue.append((neighbor, depth + 1))
                    
    return shortest_len
                    
                    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
