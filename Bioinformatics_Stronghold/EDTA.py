### Edit distance alignment ###
from Bio import SeqIO

def OptimalAlign(v,w):
    v, w = 'O'+v, 'X'+w
    n,m = len(v),len(w)
    s,backtrack = [[0 for j in range(m)] for i in range(n)], [["" for j in range(m)] for i in range(n)]
    for i in range(n):
        s[i][0] = i
        backtrack[i][0] = "down"
    for j in range(m):
        s[0][j] = j
        backtrack[0][j] = "right"
    for i in range(n-1):
        for j in range(m-1):
            if v[i+1] == w[j+1]:
                s[i+1][j+1] = s[i][j]
                backtrack[i+1][j+1] = "diagonal"
            else:
                s[i+1][j+1] = 1 + min(s[i][j], s[i + 1][j], s[i][j + 1])
                if s[i+1][j+1] == s[i][j+1] + 1:
                    backtrack[i+1][j+1] = "down"
                elif s[i+1][j+1] == s[i+1][j] + 1:
                    backtrack[i+1][j+1] = "right"
                elif s[i+1][j+1] == s[i][j] + 1:
                    backtrack[i+1][j+1] = "diagonal"
    return backtrack, s[-1][-1]

def OutputAlignment(backtrack,v,w,i,j):
    if i == 0 and j == 0:
        return ("","")
    elif i == 0 and j > 0:
        return ("-",w[j-1])
    elif i > 0 and j == 0:
        return (v[i-1],"-")
    elif backtrack[i][j] == "down":
        return OutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return OutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return OutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])


strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_edta.txt","fasta")]
backtrack,score = OptimalAlign(strings[0],strings[1])
alignment = OutputAlignment(backtrack,strings[0],strings[1],len(strings[0]),len(strings[1]))
aligned_v,aligned_w = "",""
for i in range(len(alignment)//2):
    aligned_v += alignment[2*i]
    aligned_w += alignment[2*i+1]
print(score)
print(aligned_v)
print(aligned_w)