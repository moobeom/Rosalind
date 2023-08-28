### Topological sorting ###

def getData(filename):
    lines = open(filename).readlines()
    V, E = int(lines[0].split()[0]), int(lines[0].split()[1])
    graph = lines[1:1+E]
    edges = [tuple([int(v) for v in edge.split()]) for edge in graph]
    G = {}
    for u,v in edges:
        if u not in G:
            G[u] = [v]
        else:
            G[u].append(v)
    return V,E,G

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


n,m,graph = getData("C:/Users/anqja/Downloads/rosalind_ts.txt")
print(' '.join(str(i) for i in TopoSort(graph)))