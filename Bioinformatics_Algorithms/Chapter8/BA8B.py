### Compute the squared error distortion ###

def getData(filename):
    lines = open(filename).readlines()
    k,m = int(lines[0].split()[0]), int(lines[0].split()[1])
    division = [line for line in lines[1:] if '-' in line][0]
    temp,Centers,DataPoints,j = [],[],[],0
    for line in lines[1:]:
        if line != division:
            coords = [float(i) for i in line.split()]
            temp.append(tuple(coords))
            j += 1
        else:
            Centers = temp
            DataPoints = [tuple([float(coords) for coords in line.split()]) for line in lines[j+2:]]
            break
    return k,m,Centers,DataPoints

def SquaredDistance(DataPoints,Centers):
    D = []
    for i in range(len(DataPoints)):
        d = []
        for j in range(len(Centers)):
            s = 0
            for k in range(len(DataPoints[0])):
                s += (DataPoints[i][k] - Centers[j][k]) ** 2
            d.append(s)
        D.append(min(d))
    return D

def Distortion(Data,Centers):
    return round(sum(SquaredDistance(Data,Centers)) / len(Data),3)

k,m,Centers,DataPoints = getData("C:/Users/anqja/Downloads/rosalind_ba8b (1).txt")
print(Distortion(DataPoints,Centers))