### Negative weight cycle ###
from collections import defaultdict

def getData(filename):
    lines = open(filename).readlines()
    k = int(lines[0].rstrip())
    i = 1
    graphs = []
    while i < len(lines):
        V,E = int(lines[i].split()[0]), int(lines[i].split()[1])
        graph = lines[i+1 : i+1+E]
        edges = [tuple([int(v) for v in edge.split()]) for edge in graph]
        graphs.append([V,E,edges])
        i += 1+E
    return k, graphs

def hasNegCycle(V,E,s=None):   # s: source
    if not s:
        s = 1
    distDict = {}
    for v in V:
        if v == s:
            distDict[v] = 0
        else:
            distDict[v] = float('inf')
    for i in range(len(V)-1):
        for u,v in E:
            w = E[(u,v)]
            if distDict[u] + w < distDict[v]:
                distDict[v] = distDict[u] + w
    for u,v in E:
        w = E[(u,v)]
        if distDict[u] + w < distDict[v]:       # contains a negative weight
            return 1
    return -1

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_nwc (1).txt")
answer = []
for i in range(k):
    n,m,edges = graphs[i][0], graphs[i][1], graphs[i][2]
    graph = dict()
    for (u,v,w) in edges:
        graph[(u,v)] = w
    vertices = list(set([u for u,v in graph] + [v for u,v in graph]))
    answer.append(hasNegCycle(vertices,graph))

print(' '.join(str(v) for v in answer))