### Compute limb lengths in a tree ###

def DataToMatrix(filename):
    lines = open(filename, 'r').readlines()
    matrix = []
    for line in lines:
        distances = line.split(' ')
        matrix.append([int(d) for d in distances])
    return matrix

def LimbLength(n,j,D):
    leafpairs = [(i,k) for i in range(n) for k in range(n) if i != j and k != j and i != k and i < k]
    return min((D[i][j] + D[j][k] - D[i][k]) // 2 for (i,k) in leafpairs)

n_test,j_test,D_test = 25,9,DataToMatrix("C:/Users/anqja/Downloads/rosalind_ba7b (1).txt")
print(LimbLength(n_test,j_test,D_test))