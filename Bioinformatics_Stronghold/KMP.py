### Speed up motif finding ###
from Bio import SeqIO

def MakeFailureArray(pattern):
    F = [0] * len(pattern)
    i,j = 1,0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            F[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = F[j-1]
        else:
            i += 1
    return F

pattern = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_kmp (1).txt","fasta").seq)
print(' '.join(str(num) for num in MakeFailureArray(pattern)))
