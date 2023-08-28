### Transition and transversion ###
from Bio import SeqIO

def getData(filename):
    strings = [str(string.seq) for string in SeqIO.parse(filename,"fasta")]
    return strings

def TsTv(s,t):
    Ts, Tv = [('A','G'),('G','A'),('C','T'),('T','C')], [('A','C'),('C','A'),('G','T'),('T','G'),('A','T'),('T','A'),('G','C'),('C','G')]
    ts, tv = 0, 0
    for i in range(len(s)):
        if (s[i],t[i]) in Ts:
            ts += 1
        elif (s[i],t[i]) in Tv:
            tv += 1
    return ts/tv

strings = getData("C:/Users/anqja/Downloads/rosalind_tran.txt")
print(TsTv(strings[0],strings[1]))