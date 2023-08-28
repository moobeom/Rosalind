### General sink ###
from collections import defaultdict
from queue import Queue

def getData(filename):
    lines = open(filename).readlines()
    k = int(lines[0].rstrip())
    div = []
    for i in range(k):
        if len(div) == 0:
            div.append(lines.index('\n'))
        else:
            div.append(lines[div[-1]+1:].index('\n') + div[-1]+1)
    graphs = []
    for i in range(k):
        V,E = int(lines[div[i]+1].split()[0]), int(lines[div[i]+1].split()[1])
        graph = lines[div[i]+2:div[i]+2+E]
        edges = [tuple([int(v) for v in edge.split()]) for edge in graph]
        graphs.append([V,E,edges])
    return k,graphs

def BFS(graph,s):
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
    return D

def isSink(graph):
    vertices = sorted(list(graph.keys()))
    for v in graph:
        if sorted(list(BFS(graph,v).keys())) == vertices:
            return v
    return -1


k,graphs = getData("C:/Users/anqja/Downloads/rosalind_gs (1).txt")
answer = []
for i in range(k):
    n,m,edges = graphs[i][0], graphs[i][1], graphs[i][2]
    adj = defaultdict(list)
    for (u,v) in edges:
        if u not in adj:
            adj[u] = [v]
        else:
            adj[u].append(v)
    for v in [v for u, v in edges]:
        if v not in adj:
            adj[v] = []
    answer.append(isSink(adj))
print(' '.join(str(r) for r in answer))