### Implement hierarchical clustering ###

def DataToMatrix(filename):
    lines = open(filename, 'r').readlines()
    n = int(lines[0])
    matrix = []
    for line in lines[1:]:
        distances = line.rstrip().split(' ')
        matrix.append([float(d) for d in distances])
    return n, matrix

def Closest(D,C):
    m,x,y = float('Inf'),0,0
    for i in range(len(D)):
        for j in range(len(D)):
            if i < j and D[i][j] < m:
                m,x,y = D[i][j],i,j
    return C[x],C[y]

def NodeFind(T,c_x):
    for node in T:
        if T[node] == c_x:
            return node

def Connect(adj,new_node,x,y):
    for i in range(new_node):
        if i == x or i == y:
            adj[i].append(1)
        else:
            adj[i].append(0)
    adj += [[1 if i == x or i == y else 0 for i in range(new_node+1)]]
    return adj

def APD(D,c_x,c_y):     # average of pairwise distances
    d = 0
    for x in c_x:
        for y in c_y:
            d += D[x][y]
    return d / (len(c_x) * len(c_y))

def D_remove(D,x,y):
    D_new = []
    for i in range(len(D)):
        if i != x and i != y:
            row = []
            for j in range(len(D)):
                if j != x and j != y:
                    row.append(D[i][j])
            D_new.append(row)
    return D_new

def D_add(D,DD,C,c_x,c_y):
    for i in range(len(D)):
        c_v = C[i]
        d = ((APD(DD,c_v,c_x) * len(c_x)) + (APD(DD,c_v,c_y) * len(c_y))) / (len(c_x) + len(c_y))   # D_avg
        # d = min(min([DD[x][v] for x in c_x for v in c_v]), min([DD[y][v] for y in c_y for v in c_v])) # D_min
        D[i].append(d)
    D += [[D[i][-1] if i < len(D) else 0 for i in range(len(D)+1)]]
    return D

def UPGMA(D,D_ori,n):
    clusters = [[i] for i in range(n)]
    T,adj = {i:clusters[i] for i in range(n)}, [[0 for j in range(n)] for i in range(n)]
    result = []
    while len(clusters) > 1:
        c_i,c_j = Closest(D,clusters)
        T[len(T)] = c_new = [node for node in c_i] + [node for node in c_j]
        Connect(adj,NodeFind(T,c_new),NodeFind(T,c_i),NodeFind(T,c_j))
        D = D_remove(D,clusters.index(c_i),clusters.index(c_j))
        clusters.remove(c_i) or clusters.remove(c_j)
        D_add(D,D_ori,clusters,c_i,c_j)
        clusters.append(c_new)
        result.append(c_new)
    root = NodeFind(T,clusters[-1])
    return result

n,D_sample = DataToMatrix("C:/Users/anqja/Downloads/rosalind_ba8e (1).txt")
clusters = UPGMA(D_sample,D_sample,n)
for cluster in clusters:
    print(' '.join(str(c+1) for c in cluster))