### Shortest paths in DAG ###

def getData(filename):
    lines = open(filename).readlines()
    n,m = int(lines[0].split()[0]),int(lines[0].split()[1])
    graph = dict()
    for line in lines[1:]:
        u,v,w = [i for i in line.split()]
        graph[(int(u),int(v))] = int(w)
    vertices = list(set([u for u,v in graph] + [v for u,v in graph]))
    return n,m,vertices,graph

def EdgeDict(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
    return graph

def TopoSort(graph):        # graph[predecessor] = successor (predecessor -> successor)
    P,S = set(list(graph.keys())), set()
    for v in P:
        for u in graph[v]:
            S.add(u)
    V = sorted(set(list(P) + list(S)))

    T,Q,In = [],set(),{}
    for v in V:
        In[v] = 0
    for v in S:
        for u in P:
            if v in graph[u]:
                In[v] += 1
    for v in V:
        if In[v] == 0:
            Q.add(v)

    while len(Q) > 0:
        for v in sorted(Q):
            Q.remove(v)
            T.append(v)
            for u in S:
                try:
                    if u in graph[v]:
                        In[u] -= 1
                        if In[u] == 0:
                            Q.add(u)
                except KeyError:        # vertices without predecessors
                    continue
    return T

def BellmanFord(V,E,s):   # s: source
    distDict = {}
    for v in V:
        if v == s:
            distDict[v] = 0
        else:
            distDict[v] = float('inf')
    for u in V:
        for v in [edge[1] for edge in E if u == edge[0]]:
            w = E[(u, v)]
            if distDict[u] + w < distDict[v]:
                distDict[v] = distDict[u] + w
    return distDict

n,m,vertices,edges = getData("C:/Users/anqja/Downloads/rosalind_sdag (1).txt")
sorted_vertices = TopoSort(EdgeDict(list(edges)))
distances = BellmanFord(sorted_vertices,edges,1)
answer = ''
for v in vertices:
    if distances[v] != float('inf'):
        answer += str(distances[v]) + ' '
    else:
        answer += 'x' + ' '
print(answer)