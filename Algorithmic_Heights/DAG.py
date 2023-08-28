### Testing acyclicity ###
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

def isAcyclic(G):
    for v in G:
        path = []
        DFS(G,v,path)
        path = [v] + path[::-1]
        if path[0] == path[-1]:
            return -1
    return 1

def DFS(G,s,path,visited=None):
    if not visited:
        visited = set()
    while s not in visited:
        visited.add(s)
        for w in G[s]:
            if w in G:
                DFS(G,w,path,visited)
            path.append(w)

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_dag.txt")
for i in range(k):
    n,m,edges = graphs[i][0], graphs[i][1], graphs[i][2]
    adj = defaultdict(list)
    for (u,v) in edges:
        adj[u-1].append(v-1)  # directed edge
    print(isAcyclic(adj))