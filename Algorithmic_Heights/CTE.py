### Shortest cycle through a given edge ###
from collections import defaultdict

def getData(filename):
    lines = open(filename).readlines()
    k = int(lines[0].rstrip())
    i = 1
    graphs = []
    while i < len(lines):
        V, E = int(lines[i].split()[0]), int(lines[i].split()[1])
        graph = lines[i+1:i+1+E]
        edges = [tuple([int(v) for v in edge.split()]) for edge in graph]
        graphs.append([V,E,edges])
        i += 1+E
    return k,graphs

def ShortestCycle(graph,s):
    shortest = float('inf')
    DistDict = {v: float('inf') for v in graph if v != s}
    DistDict[s] = 0
    Q = [(0,s)]
    while Q:        # Dijkstra's algorithm
        d,u = min(Q)
        Q.remove((d,u))
        if d > DistDict[u]:
            continue
        for v,w in graph[u]:
            if v == s:
                shortest = min(shortest, DistDict[u] + w + DistDict[v])
            elif DistDict[v] > DistDict[u] + w:
                DistDict[v] = DistDict[u] + w
                Q.append((DistDict[v],v))
    if shortest != float('inf'):
        return shortest
    return -1


k,graphs = getData("C:/Users/anqja/Downloads/rosalind_cte (2).txt")
cycle_lens = []
for i in range(k):
    n,m,edgeweights = graphs[i][0], graphs[i][1], graphs[i][2]
    adj = defaultdict(list)
    for (u,v,w) in edgeweights:
        adj[u].append((v,w))
    for v in [v for u,v,w in edgeweights]:
        if v not in adj:
            adj[v] = []
    cycle_lens.append(ShortestCycle(adj,edgeweights[0][1]))

print(' '.join([str(l) for l in cycle_lens]))