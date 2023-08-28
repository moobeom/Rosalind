### Overlap alignment ###
from Bio import SeqIO
import sys
sys.setrecursionlimit(10**7)

def OverlapAlign(v,w):
    n, m = len(v), len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = 0
        backtrack[i][0] = "down"
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] -2
        backtrack[0][j] = "right"
    for i in range(1,n+1):
        for j in range(1,m+1):
            match = 0
            if v[i-1] == w[j-1]:
                match += 1
            else:
                match += -2
            s[i][j] = max(s[i-1][j] -2, s[i][j-1] -2, s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j] -2:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1] -2:
                backtrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "diagonal"
    s_max,w_sink = max(s[-1]),0
    for j in range(m-1,-1,-1):
        if s[-1][j] == s_max:
            w_sink = j
            break
    return backtrack,s[-1][w_sink],w_sink

def OutputAlignment(backtrack,v,w,i,j):
    if i == 0 or j == 0:
        return ("","")
    elif backtrack[i][j] == "down":
        return OutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return OutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return OutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_oap.txt","fasta")]
backtrack,alignment_score,w_sink = OverlapAlign(strings[0],strings[1])
alignment = OutputAlignment(backtrack,strings[0],strings[1],len(strings[0]),w_sink)
aligned_v,aligned_w = "",""
for i in range(len(alignment)//2):
    aligned_v += alignment[2*i]
    aligned_w += alignment[2*i+1]
print(alignment_score)
print(aligned_v)
print(aligned_w)