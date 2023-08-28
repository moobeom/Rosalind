### Find a topological order of DAG ###

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

sample_graph = {1:[2],2:[3],4:[2],5:[3]}
#print(TopoSort(sample_graph))

file = open('C:/Users/anqja/Downloads/rosalind_ba5n (5).txt','r')
lines =file.readlines()
test_graph = {}
for line in lines:
    vertices = line.strip().split(' -> ')
    key,values = vertices[0], vertices[1].split(',')
    test_graph[key] = values
order = TopoSort(test_graph)

answer = ''
for vertex in order:
    answer += vertex + ', '
print(answer[:-2])