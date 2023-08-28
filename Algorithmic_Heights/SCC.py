### Strongly connected graph ###
from collections import defaultdict


def getData(filename):
    lines = open(filename).readlines()
    V, E = int(lines[0].split()[0]), int(lines[0].split()[1])
    graph = lines[1:1 + E]
    edges = [tuple([int(v) for v in edge.split()]) for edge in graph]
    return V,E,edges

def SCC(graph):
    stack = []
    parent = {}
    visited = set()
    result = []

    def StrongConnect(v):
        visited.add(v)
        stack.append(v)
        parent[v] = len(stack) - 1      # assign a unique number (index) for each node

        # recursively construct a DFS path and find the parent node in the path
        for w in graph[v]:
            if w not in visited:
                StrongConnect(w)
                parent[v] = min(parent[v], parent[w])
            elif w in stack:
                parent[v] = min(parent[v], stack.index(w))

        # if the node is a root node, create a new strongly connected component
        if parent[v] == stack.index(v):
            component = []
            while True:
                w = stack.pop()
                component.append(w)
                if w == v:
                    break
            result.append(component)
    for v in graph:
        if v not in visited:
            StrongConnect(v)
    return result

n,m,edges = getData("C:/Users/anqja/Downloads/rosalind_scc (1).txt")
adj = defaultdict(list)
for (u,v) in edges:
    if u not in adj:
        adj[u] = [v]
    else:
        adj[u].append(v)
for v in [v for u,v in edges]:
    if v not in adj:
        adj[v] = []
print((len(SCC(adj)) + (n-len(adj))))