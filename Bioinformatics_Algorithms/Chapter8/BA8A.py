### Implement Farthest first traversal ###

def getData(filename):
    lines = open(filename).readlines()
    k,m = int(lines[0].split()[0]), int(lines[0].split()[1])
    DataPoints = []
    for line in lines[1:]:
        DataPoints.append(tuple(float(line.split()[i]) for i in range(m)))
    return k,DataPoints

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

if __name__ == '__main__':
    k, DataPoints = getData("C:/Users/moveo/Downloads/rosalind_ba8a (2).txt")
    centers = FarthestFirstTraversal(DataPoints,k)
    for center in centers:
        print(' '.join([str(coord) for coord in center]))