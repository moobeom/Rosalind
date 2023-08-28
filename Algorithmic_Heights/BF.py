### Bellman-Ford algorithm ###

def getData(filename):
    lines = open(filename).readlines()
    n,m = int(lines[0].split()[0]),int(lines[0].split()[1])
    graph = dict()
    for line in lines[1:]:
        u,v,w = [i for i in line.split()]
        graph[(int(u),int(v))] = int(w)
    vertices = list(set([u for u,v in graph] + [v for u,v in graph]))
    return n,m,vertices,graph

def BellmanFord(V,E,s):   # s: source
    distDict = {}
    for v in V:
        if v == s:
            distDict[v] = 0
        else:
            distDict[v] = float('inf')
    for i in range(len(V)-1):
        for u,v in E:
            w = E[(u,v)]
            if distDict[u] + w < distDict[v]:
                distDict[v] = distDict[u] + w
    for u,v in E:
        w = E[(u,v)]
        if distDict[u] + w < distDict[v]:
            raise ValueError("Graph contains a negative-weight cycle")
    return distDict


n,m,vertices,edges = getData("C:/Users/anqja/Downloads/rosalind_bf (2).txt")
distances = BellmanFord(vertices,edges,1)
answer = ''
for v in vertices:
    if distances[v] != float('inf'):
        answer += str(distances[v]) + ' '
    else:
        answer += 'x' + ' '
print(answer)