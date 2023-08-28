### Compute distances between leaves ###

def DataToGraph(filename):
    n = int(open(filename,'r').readline().rstrip())
    lines = open(filename,'r').readlines()[1:]
    edgeDict = {}
    for line in lines:
        nodepair, weight = line.split(':')[0].split('->'), int(line.split(':')[1].rstrip())
        p,s = int(nodepair[0]), int(nodepair[1])
        edgeDict[(p,s)] = weight
    return n,edgeDict

def DistanceMatrix(n,graph):
    edges = list(graph.keys())
    t = max([max(edge) for edge in edges])
    adj = [[0 for j in range(t+1)] for i in range(t+1)]
    for edge in edges:
        adj[edge[0]][edge[1]] += 1

    matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j:
                matrix[i][j] = matrix[j][i]
            else:
                path = bfs(adj,i,j)
                weight = 0
                for k in range(len(path)-1):
                    weight += graph[(path[k],path[k+1])]
                matrix[i][j] = weight
    return matrix

def bfs(adj,s,e):
    n = len(adj)
    visit = [[False for j in range(n)] for i in range(n)]
    queue = [s]
    while e not in queue:
        for k in range(len(queue)):
            i = queue[0]
            queue.remove(i)
            for j in range(n):
                if adj[i][j] > 0:
                    if visit[j][i] is False:
                        visit[i][j] = True
                        queue.append(j)
    path = [e]
    while s not in path:
        backtrack = path[-1]
        for i in range(n):
            if visit[i][backtrack] is True:
                path.append(i)
    return list(reversed(path))


n,graph = DataToGraph("C:/Users/anqja/Downloads/rosalind_ba7a.txt")
matrix = DistanceMatrix(n,graph)
answer = ''
for row in matrix:
    for i in range(len(row)):
        if i < len(row)-1:
            answer += str(row[i]) + ' '
        else:
            answer += str(row[i]) + '\n'
print(answer)