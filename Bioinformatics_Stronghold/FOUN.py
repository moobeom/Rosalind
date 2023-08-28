### The founder effect and genetic drift ###
from math import log10,factorial

def Comb(n,r):
    return factorial(n) / (factorial(r) * factorial(n-r))

lines = open("C:/Users/anqja/Downloads/rosalind_foun_sample.txt").readlines()
N, m = [int(x) for x in lines[0].split()]
R = [int(x) for x in lines[1].split()]
M = [[0 for j in range(len(R))] for i in range(m)]

for index in range(len(R)):
    q = 1 - R[index] / (2*N)
    p_arr = [Comb(2*N,j) * q ** j * (1-q) ** (2*N - j) for j in range(1, 2*N+1)]
    M[0][index] = log10(p_arr[0])

    for gen in range(1,m-1):
        new_p_arr = []
        for j in range(1,2*N+1):
            temp = [Comb(2*N,j) * (n / (2*N)) ** j * (1 - n / (2*N)) ** (2*N - j) for n in range(1, 2*N+1)]
            new_p_arr.append(sum(temp[j] * p_arr[j] for j in range(len(temp))))
        p_arr = new_p_arr
        M[gen][index] = log10(p_arr[0])
    temp = [(1 - (n / (2*N))) ** (2*N) for n in range(0, 2*N+1)]
    M[m-1][index] = log10(sum(temp[i] * p_arr[i] for i in range(len(temp))))

print(M)