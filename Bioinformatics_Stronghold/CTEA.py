### Counting optimal alignments ###
from Bio import SeqIO

def CountOptimalAligns(v,w):
    v, w = 'O'+v, 'X'+w
    n,m = len(v),len(w)
    s,c = [[0 for j in range(m)] for i in range(n)], [[0 for j in range(m)] for i in range(n)]      # scores and counts
    for i in range(n):
        s[i][0] = i
        c[i][0] = 1
    for j in range(m):
        s[0][j] = j
        c[0][j] = 1
    for i in range(n-1):
        for j in range(m-1):
            if v[i+1] == w[j+1]:
                s[i+1][j+1] = s[i][j]
                c[i+1][j+1] = c[i][j]
            else:
                s[i+1][j+1] = 1 + min(s[i][j], s[i+1][j], s[i][j+1])
            if s[i+1][j+1] == s[i][j+1] + 1:
                c[i+1][j+1] += c[i][j+1]
            if s[i+1][j+1] == s[i+1][j] + 1:
                c[i+1][j+1] += c[i+1][j+1]
            if s[i+1][j+1] == s[i][j] + 1:
                c[i+1][j+1] += c[i][j]
    return c[-1][-1]

strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_ctea.txt","fasta")]
print(CountOptimalAligns(strings[0],strings[1]) % (2 ** 21 -1))
