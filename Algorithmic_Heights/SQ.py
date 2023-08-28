### Square in a graph ###
from collections import defaultdict

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

def FindSquare(graph):
    for v in graph:
        path = DFS(graph,v)
        if v in adj[path[-1]]:
            path.append(v)
        if len(path) == 5:
            return 1
    return -1

def DFS(G,s,path=None,visited=None):
    if not path:
        path = []
    if not visited:
        visited = set()
    while s not in visited:
        visited.add(s)
        path.append(s)
        for w in G[s]:
            if w in G:
                DFS(G,w,path,visited)
    return path

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_sq_sample.txt")
for i in range(k):
    n,m,edges = graphs[i][0], graphs[i][1], graphs[i][2]
    adj = defaultdict(list)
    for (u,v) in edges:
        adj[u].append(v)
        adj[v].append(u)
    print(FindSquare(adj))