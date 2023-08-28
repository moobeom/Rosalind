### Breadth-first search ###

def getData(filename):
    lines = open(filename).readlines()
    n,m = lines[0].rstrip().split(' ')
    edges = [line.rstrip().split(' ') for line in lines[1:]]
    return int(n),int(m),[(int(u),int(v)) for (u,v) in edges]

def Bfs(adj,s,e):
    n = len(adj)
    visit = [[False for j in range(n)] for i in range(n)]
    queue = [s]
    while e not in queue:
        if not queue:   # not reachable to 'e'
            return None
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

n,m,edges = getData("C:/Users/anqja/Downloads/rosalind_bfs.txt")
adj = [[0 for j in range(n)] for i in range(n)]
for (u,v) in edges:
    adj[u-1][v-1] += 1
temp = []
for i in range(n):
    path = Bfs(adj,0,i)
    if path is None:
        temp.append(-1)
    else:
        temp.append(len(path)-1)
answer = ''
for length in temp:
    answer += str(length) + ' '
print(answer)