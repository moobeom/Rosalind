### Implement AdditivePhylogeny ###

def DataToMatrix(filename):
    lines = open(filename, 'r').readlines()
    matrix = []
    for line in lines:
        distances = line.rstrip().split(' ')
        matrix.append([int(d) for d in distances])
    return matrix

def Limb(D,j):
    leafpairs = [(i,k) for i in range(len(D)) for k in range(len(D)) if i != j and k != j and i != k and i < k]
    return min((D[i][j] + D[j][k] - D[i][k]) // 2 for (i,k) in leafpairs)

def FindTriplet(D,j):
    for i in range(len(D)):
        for k in range(len(D)):
            if i < j and k < j and i != k and D[i][k] == D[i][j] + D[j][k]:
                return i,k

def NewNode(tree,n,i,j,d):
    edges = list(tree.keys())
    m = max([max(edge) for edge in edges])
    if n > m:
        new_node = n
    else:
        new_node = m+1
    adj = [[0 for j in range(m+1)] for i in range(m+1)]
    for edge in edges:
        adj[edge[0]][edge[1]] += 1
        adj[edge[1]][edge[0]] += 1
    path = bfs(adj,i,j)
    near_i,near_j, k = path[0], path[-1], 0
    while d > 0:
        if tree[(path[k],path[k+1])] > d:
            near_i, near_j = path[k], path[k+1]
        elif tree[(path[k],path[k+1])] == d:
            new_node = near_i = path[k]
            near_j = path[k+1]
        d -= tree[(path[k],path[k+1])]
        k += 1
    d += tree[(path[path.index(near_i)],path[path.index(near_i)+1])]
    return new_node,near_i,near_j,d

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

def AdditivePhylogeny(D,n,nn):      # nn: initial number of leaves
    T = {}
    if n == 2:
        T[(0,1)] = D[0][1]
        return T
    limblength = Limb(D,n-1)
    for j in range(1,n):
        D[j-1][n-1] -= limblength
        D[n-1][j-1] = D[j-1][n-1]
    (i,k) = FindTriplet(D,n-1)
    x = D[i][n-1]
    D = [d[:(n-1)] for d in D][:(n-1)]
    T = AdditivePhylogeny(D,n-1,nn)
    v,i,k,x = NewNode(T,nn,i,k,x)
    if v != i:
        T[(i,v)], T[(v,k)] = x, T[(i,k)]-x
        del T[(i,k)]
    T[(v,n-1)] = limblength
    return T


D_sample = DataToMatrix("C:/Users/anqja/Downloads/rosalind_ba7c.txt")
tree = AdditivePhylogeny(D_sample,24,24)
t = max(max(b) for b in tree)
edges = []
for i in range(t+1):
    for nodepair in tree:
        if i == nodepair[0]:
            edges.append('{}->{}:{}'.format(i,nodepair[1],tree[nodepair]))
        elif i == nodepair[1]:
            edges.append('{}->{}:{}'.format(i,nodepair[0], tree[nodepair]))

for edge in edges:
    print(edge)