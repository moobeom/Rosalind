### Implement the Neighbor Joining algorithm ###

def DataToMatrix(filename):
    lines = open(filename, 'r').readlines()
    matrix = []
    for line in lines:
        distances = line.rstrip().split('\t')
        matrix.append([int(d) for d in distances])
    return matrix

def Transform(D,n):
    DD = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                DD[i][j] = (n-2) * D[i][j] - TotalDistance(D,i) - TotalDistance(D,j)
    return DD

def TotalDistance(D,x):
    return sum(D[x])

def D_add(D,x,y):
    for k in range(len(D)):
        D[k].append(0.5 * (D[k][x] + D[k][y] - D[x][y]))
    D += [[D[k][-1] if k < len(D) else 0 for k in range(len(D)+1)]]
    return D

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

def NeighborJoining(D,n,nodes=None,limbs=None):    # nn: initial number of leaves
    if nodes is None:
        nodes = [i for i in range(n)]
    if limbs is None:
        limbs = []
    T ={}
    if n == 2:
        T[(nodes[0],nodes[1])] = D[0][1]
        T[(nodes[1],nodes[0])] = D[1][0]
        return T
    DD = Transform(D,n)
    (i,j) = [(i,j) for i in range(n) for j in range(n) if DD[i][j] == min(min(d) for d in DD)][0]   # earliest matching
    delta = (TotalDistance(D,i) - TotalDistance(D,j)) / (n-2)
    limblength_i, limblength_j = 0.5 * (D[i][j] + delta), 0.5 * (D[i][j] - delta)
    m = max(nodes) + 1
    nodes.append(m)
    D_add(D,i,j)
    limbs.append((nodes[i],nodes[j]))
    nodes.remove(nodes[i]) or nodes.remove(nodes[j-1])
    D = D_remove(D,i,j)
    T = NeighborJoining(D,n-1,nodes,limbs)
    (i,j) = limbs[len(limbs)+2-n]
    T[(m,i)], T[(m,j)] = limblength_i, limblength_j
    T[(i,m)], T[(j,m)] = limblength_i, limblength_j
    return T

#D_sample = DataToMatrix("C:/Users/anqja/Downloads/rosalind_ba7e_sample3.txt")
D_test = DataToMatrix("C:/Users/anqja/Downloads/rosalind_ba7e.txt")
tree = NeighborJoining(D_test,32)
for edge in sorted(tree):
    print('{}->{}:{:.3f}'.format(edge[0],edge[1],tree[edge]))