### Hamiltonian path in DAG ###
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

def Hamilton(edges,graph):
    topo_graph = TopoSort(graph)
    path = []
    for i in range(len(topo_graph)):
        if i == len(topo_graph) - 1:
            path.append(topo_graph[i])
        elif (topo_graph[i], topo_graph[i+1]) in edges:
            path.append(topo_graph[i])
        else:
            return None
    return path

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_hdag.txt")
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

    if not Hamilton(edges,adj):
        print(-1)
    else:
        print(1,' '.join(str(i) for i in Hamilton(edges,adj)))