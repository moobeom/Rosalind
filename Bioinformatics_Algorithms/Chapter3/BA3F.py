### Find an Eulerian cycle in a graph ###

def EulerianCycle(graph):
    edges = edgeFind(graph)
    n = nodesCount(graph)
    adj = adjMaker(n,edges)

    start, path = 0, []
    dfs(start,n,adj,path)
    answer = tuple(reversed(path))
    return answer

def edgeFind(graph):
    graph = open(graph, 'r')
    lines = graph.readlines()
    edges = []
    for line in lines:
        nodes = line.split('->')
        if ',' in nodes[1]:
            values = nodes[1].split(',')
            for value in values:
                edges.append([int(nodes[0]),int(value)])
        else:
            edges.append([int(nodes[0]),int(nodes[1])])
    return edges

def nodesCount(graph):
    graph = open(graph, 'r')
    lines = graph.readlines()
    n = 0
    for line in lines:
        n += 1
    return n

def adjMaker(n,edges):
    adj = [[0] * (n) for element in range(n)]
    for edge in edges:
        adj[edge[0]][edge[1]] = 1
    return adj

def startFind(start,n,adj):
    for i in range(n):
        count = 0
        for j in range(n):
            count += adj[i][j]
        if start == 0 and count > 0:
            start = i

def dfs(node,n,adj,path):
    for next in range(n):
        if adj[node][next] > 0:
            adj[node][next] -= 1
            dfs(next,n,adj,path)
    path.append(node)

graph = 'C:/Users/anqja/Downloads/rosalind_ba3f.txt'
cycle = EulerianCycle(graph)
cycle2 = []
for node in cycle:
    cycle2.append(str(node))


answer = '->'.join(cycle2)
print(answer)