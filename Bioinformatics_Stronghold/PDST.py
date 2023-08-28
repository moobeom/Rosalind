### Creating a distance matrix ###
from Bio import SeqIO

def HammingDistance(p,q):
    count = 0
    for i in range(min(len(p),len(q))):
        if p[i] != q[i]:
            count += 1
    return count

def DistanceMatrix(strings):
    n = len(strings)
    D = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i > j:
                D[i][j] = D[j][i]
            elif i < j:
                D[i][j] = HammingDistance(strings[i],strings[j]) / len(strings[i])
    return D


strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_pdst.txt","fasta")]
matrix = DistanceMatrix(strings)
answer = ''
for row in matrix:
    for i in range(len(row)):
        if i < len(row)-1:
            answer += str(row[i]) + ' '
        else:
            answer += str(row[i]) + '\n'
print(answer)