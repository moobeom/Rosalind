### Degree array ###

def getData(filename):
    lines = open(filename).readlines()
    n,m = lines[0].rstrip().split(' ')
    edges = [line.rstrip().split(' ') for line in lines[1:]]
    return int(n),int(m),[(int(u),int(v)) for (u,v) in edges]

def Degree(n,D):
    adj = [[0 for j in range(n)] for i in range(n)]
    for (u,v) in D:
        adj[u-1][v-1] += 1
        adj[v-1][u-1] += 1
    return adj

n,m,edges = getData("C:/Users/anqja/Downloads/rosalind_deg.txt")
adjMatrix = Degree(n,edges)
answer = ''
for i in range(n):
    answer += str(sum(adjMatrix[i])) + ' '
print(answer)