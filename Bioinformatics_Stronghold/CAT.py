### Catalan numbers and RNA secondary structure ###
from Bio import SeqIO

CatDict = {}        # memoization
def Catalan(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    if seq in CatDict:
        return CatDict[seq]

    res = 0
    for i in range(1,len(seq),2):
        if (seq[0] == 'A' and seq[i] == 'U') or (seq[0] == 'U' and seq[i] == 'A') or \
                (seq[0] == 'C' and seq[i] == 'G') or (seq[0] == 'G' and seq[i] == 'C'):
            res += Catalan(seq[1:i]) * Catalan(seq[i+1:])  # left and right side of base pair between first and i-th base in the sequence
    CatDict[seq] = res
    return CatDict[seq]

string = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_cat (1).txt","fasta").seq)
print(Catalan(string) % 1000000)
