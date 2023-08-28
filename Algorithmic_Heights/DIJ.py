### Dijkstra's algorithm ###

def getData(filename):
    lines = open(filename).readlines()
    n,m = int(lines[0].split()[0]),int(lines[0].split()[1])
    graph = dict()
    for line in lines[1:]:
        u,v,w = [i for i in line.split()]
        if int(u) not in graph:
            graph[int(u)] = [(int(v),int(w))]
        else:
            graph[int(u)].append((int(v),int(w)))
    return n,m,graph

def Dijkstra(G,s):      # s : source
    DistDict = dict()       # since vertex is not labelled consecutively, addressed with dictionary
    for u in G:
        DistDict[u] = float('inf')
    for v,w in sum(list(G.values()),[]):
        DistDict[v] = float('inf')
    DistDict[s] = 0
    unvisited = set(DistDict)
    while unvisited:
        u = None
        for node in unvisited:
            if u is None or DistDict[node] < DistDict[u]:
                u = node
        unvisited.remove(u)
        if u in G:
            for v,w in G[u]:
                if DistDict[u] + w < DistDict[v]:
                    DistDict[v] = DistDict[u] + w
    return DistDict

n,m,graph = getData("C:/Users/anqja/Downloads/rosalind_dij (4).txt")
D = Dijkstra(graph,1)
answer = ''
for i in range(1,n+1):
    if i in sorted(D):
        if D[i] == float('inf'):
            answer += str(-1) + ' '
        else:
            answer += str(D[i]) + ' '
    else:
        answer += str(-1) + ' '
print(answer)