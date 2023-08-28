### Maximizing the gap symbols of an optimal alignment ###
from Bio import SeqIO

def MaxGapAlignment(v,w):
    v, w = 'O'+v, 'X'+w
    s = [[0 for j in range(len(w))] for i in range(len(v))]
    for i in range(len(v)-1):
        for j in range(len(w)-1):
            if v[i+1] == w[j+1]:
                s[i+1][j+1] = s[i][j] + 1
            else:
                s[i+1][j+1] = max(s[i+1][j], s[i][j+1])
    return len(v) - 1 + len(w) - 1 - 2 * s[-1][-1]

strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_mgap.txt","fasta")]
print(MaxGapAlignment(strings[0],strings[1]))
