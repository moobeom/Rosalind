### Implement Farthest first traversal ###

def getData(filename):
    lines = open(filename).readlines()
    k,m = int(lines[0].split()[0]), int(lines[0].split()[1])
    DataPoints = []
    for line in lines[1:]:
        (x,y) = [i for i in line.split()]
        DataPoints.append((float(x),float(y)))
    return k,m,DataPoints

def Distance(DataPoints,Centers):
    D = []
    for i in range(len(DataPoints)):
        d = []
        for j in range(len(Centers)):
            d.append((((DataPoints[i][0] - Centers[j][0]) ** 2) + ((DataPoints[i][1] - Centers[j][1]) ** 2)) ** 0.5)
        D.append(min(d))
    return D
def FarthestFirstTraversal(Data,k):
    Centers = {Data[0]}
    while len(Centers) < k:
        d = Distance(Data,list(Centers))
        Datapoint = Data[d.index(max(d))]
        Centers.add(Datapoint)
    return Centers

k,m,DataPoints = getData("C:/Users/anqja/Downloads/rosalind_ba8a.txt")
centers = FarthestFirstTraversal(DataPoints,k)
for center in centers:
    print('{} {}'.format(center[0],center[1]))