from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.neighbors = [[] for _ in range(num_of_nodes)]

    def connect(self, node1, node2):
        self.neighbors[node1].append(node2)
        self.neighbors[node2].append(node1)

    def find_all_distances(self, start_node):
        visited = set()
        inqueue = defaultdict(bool)
        distances = [-1 for _ in range(self.num_of_nodes)]
        bft_que = deque([(start_node, 0)])
        while bft_que:
            next_node, depth = bft_que.popleft()
            if next_node not in visited and distances[next_node] == -1:
                distances[next_node] = 6 * depth
            visited.add(next_node)
            for neighbor in self.neighbors[next_node]:
                if neighbor not in visited and not inqueue[neighbor]:
#                    print(neighbor)
                    bft_que.append((neighbor, depth+1))
                    inqueue[neighbor] = True
        output = ''
        for node in range(self.num_of_nodes):
            if node != start_node:
                output += f'{distances[node]} '
        print(output[0:-1])

        
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
