### 2-Satisfiability ###

from collections import defaultdict

def getData(filename):
    lines = open(filename).readlines()
    k = int(lines[0].rstrip())
    i = 2
    graphs = []
    while i < len(lines):
        n,m = int(lines[i].split()[0]), int(lines[i].split()[1])
        clauses = lines[i+1 : i+1+m]
        clauses = [tuple([int(i) for i in clause.split()]) for clause in clauses]
        graph = defaultdict(list)
        for x, y in clauses:
            graph[-x].append(y)
            graph[-y].append(x)
        graphs.append([n,m,graph])
        i += 2 + m
    return k, graphs

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

def is2Sat(sccs):
    assignment = {}
    for scc in sccs:
        for comp in scc:
            if -comp in scc:
                return False
            if abs(comp) not in assignment:
                assignment[abs(comp)] = -comp
    return assignment

k,graphs = getData("C:/Users/anqja/Downloads/rosalind_2sat.txt")
for i in range(k):
    n,m,graph = graphs[i][0], graphs[i][1], graphs[i][2]
    result = is2Sat(SCC(graph))
    if result is not False:
        answer = str(1) + ' '
        sats = [result[comp] for comp in sorted(list(result))]
        answer += ' '.join(str(sat) for sat in sats)
        print(answer)
    else:
        print(0)