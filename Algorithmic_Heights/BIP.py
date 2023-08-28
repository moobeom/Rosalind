### Testing bipartiteness ###
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

def isBipartite(G):
    ColorDict = {}
    for key in G:
        ColorDict[key] = -1

    def DFS(v,color):
        ColorDict[v] = color
        for w in G[v]:
            if ColorDict[w] == color:
                return False
            if ColorDict[w] == -1 and DFS(w,1-color) is False:
                return False
        return True

    for v in G:
        if ColorDict[v] == -1 and DFS(v,0) is False:
            return -1
    return 1

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_bip (4).txt")
for i in range(k):
    n,m,edges = graphs[i][0], graphs[i][1], graphs[i][2]
    adj = defaultdict(list)
    for (u,v) in edges:
        adj[u-1].append(v-1)  # undirected edge
        adj[v-1].append(u-1)
    print(isBipartite(adj))