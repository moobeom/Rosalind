### Implement the Llyod algorithm for k-means clustering ###

def getData(filename):
    lines = open(filename).readlines()
    k,m = int(lines[0].split()[0]), int(lines[0].split()[1])
    DataPoints = [tuple([float(coords) for coords in line.split()]) for line in lines[1:]]
    return k,m,DataPoints

def Distance(p,q):
    d = 0
    for i in range(len(p)):
        d += (p[i] - q[i]) ** 2
    return d ** 0.5

def Clustering(DataPoints,Centers):
    clusters = [[center] for center in Centers]
    for datapoint in DataPoints:
        Dists = [Distance(datapoint,center) for center in Centers]
        index = list(Dists).index(min(Dists))
        clusters[index].append(datapoint)
    return clusters

def COG(DataPoints):
    n,m = len(DataPoints), len(DataPoints[0])
    g = []
    for i in range(m):
        s = 0
        for j in range(n):
            s += DataPoints[j][i]
        g.append(s/n)
    return tuple(g)

def Llyod(Data,k):
    CenterSet = [set(Data[:k]),set()]
    while CenterSet[-2] != CenterSet[-1]:
        if CenterSet[-1] == set():
            clusters = Clustering(Data,CenterSet[-2])
            CenterSet[-1] = set([COG(cluster) for cluster in clusters])
        else:
            clusters = Clustering(Data, CenterSet[-1])
            CenterSet.append(set([COG(cluster) for cluster in clusters]))
    return CenterSet[-1]
k,m,DataPoints = getData("C:/Users/anqja/Downloads/rosalind_ba8c.txt")
centers = Llyod(DataPoints,k)
for center in centers:
    coords = [round(coord,3) for coord in center]
    print(' '.join(str(coord) for coord in coords))