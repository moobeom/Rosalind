### Edit distance ###
from Bio import SeqIO


def EditDistance(v,w):
    v, w = 'O'+v, 'X'+w
    s = [[0 for j in range(len(w))] for i in range(len(v))]
    for i in range(len(v)):
        s[i][0] = i
    for j in range(len(w)):
        s[0][j] = j
    for i in range(len(v) -1):
        for j in range(len(w) -1):
            if v[i+1] == w[j+1]:
                s[i+1][j+1] = s[i][j]
            else:
                s[i+1][j+1] = 1 + min(s[i][j], s[i+1][j], s[i][j+1])
    return s[-1][-1]


strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_edit.txt","fasta")]
print(EditDistance(strings[0],strings[1]))