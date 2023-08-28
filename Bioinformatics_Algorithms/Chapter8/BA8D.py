### Implement the soft k-means clustering algorithm ###
from math import exp

def getData(filename):
    lines = open(filename).readlines()
    k,m = int(lines[0].split()[0]), int(lines[0].split()[1])
    beta = float(lines[1])
    DataPoints = [tuple([float(coords) for coords in line.split()]) for line in lines[2:]]
    return k,m,beta,DataPoints

def Distance(p,q):
    d = 0
    for i in range(len(p)):
        d += (p[i] - q[i]) ** 2
    return d ** 0.5

def E_Step(DataPoints,Centers,beta):
    HM = []
    for datapoint in DataPoints:
        hm = [exp(-1*beta*Distance(datapoint,center)) for center in Centers]
        HM.append([d/sum(hm)for d in hm])
    return HM

def M_Step(DataPoints,HiddenMatrix):
    n,m,k = len(DataPoints), len(DataPoints[0]), len(HiddenMatrix[0])
    Centers = []
    for i in range(k):
        sumHM = sum([hm[i] for hm in HiddenMatrix])
        WCOG = [(sum([HiddenMatrix[j][i]*DataPoints[j][jj] for j in range(n)]) / sumHM) for jj in range(m)]
        Centers.append(tuple(WCOG))
    return Centers

def SoftkmeansClustering(Data,k,beta,n):
    Centers = Data[:k]
    for i in range(n):
        HiddenMatrix = E_Step(Data,Centers,beta)
        Centers = M_Step(Data,HiddenMatrix)
    return Centers

k,m,beta,DataPoints = getData("C:/Users/anqja/Downloads/rosalind_ba8d.txt")
centers = SoftkmeansClustering(DataPoints,k,beta,n=100)
for center in centers:
    coords = [round(coord,3) for coord in center]
    print(' '.join(str(coord) for coord in coords))