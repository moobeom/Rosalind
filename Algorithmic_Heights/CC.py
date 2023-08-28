### Connected components ###
from collections import defaultdict
from queue import Queue

def getData(filename):
    lines = open(filename).readlines()
    n,m = lines[0].rstrip().split(' ')
    edges = [line.rstrip().split(' ') for line in lines[1:]]
    return int(n),int(m),[(int(u),int(v)) for (u,v) in edges]

def BFS(graph,s,t):
    if s == t:
        return 0
    Q = Queue()
    visited = set()
    D = {s:0}   # distance
    Q.put(s)
    visited.add(s)
    while not Q.empty():
        v = Q.get()
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                Q.put(neighbor)
                D[neighbor] = D[v] + 1
                if neighbor == t:
                    return D[t]
    return -1

n,m,edges = getData("C:/Users/anqja/Downloads/rosalind_cc (2).txt")
adj = defaultdict(list)
for (u,v) in edges:
    adj[u-1].append(v-1)    # undirected edge
    adj[v-1].append(u-1)

nodes,c = [i for i in range(n)], 0
while len(nodes) > 0:
    temp = [BFS(adj,nodes[0],i) for i in range(n)]
    connection = [i for i in range(len(temp)) if temp[i] > -1]
    nodes = [node for node in nodes if node not in connection]
    c += 1
print(c)