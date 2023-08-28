### Finding a shared spliced motif ###
from Bio import SeqIO
import sys
sys.setrecursionlimit(10**7)

def LCSBackTrack(v,w):
    s,backTrack = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)], [["" for j in range(len(w)+1)] for i in range(len(v)+1)]
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match += 1
            s[i][j] = max(s[i-1][j] , s[i][j-1] , s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j]:
                backTrack[i][j] = "down"
            elif s[i][j] == s[i][j-1]:
                backTrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + match:
                backTrack[i][j] = "diagonal"
    return backTrack

def OutputLCS(backTrack,v,i,j):
    if i == 0 or j == 0:
        return ""
    if backTrack[i][j] == "down":
        return OutputLCS(backTrack,v,i-1,j)
    elif backTrack[i][j] == "right":
        return OutputLCS(backTrack,v,i,j-1)
    else:
        return OutputLCS(backTrack,v,i-1,j-1) + v[i-1]


strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_lcsq.txt","fasta")]
print(OutputLCS(LCSBackTrack(strings[0],strings[1]),strings[0],len(strings[0]),len(strings[1])))