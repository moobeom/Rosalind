### K-mer composition ###
from Bio import SeqIO
from itertools import product

string = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_kmer.txt","fasta").seq)
kmerDict = {kmer: 0 for kmer in [''.join(chars) for chars in product(*(4*('ACGT',)))]}
for i in range(len(string)-3):
    kmerDict[string[i:i+4]] += 1
print(' '.join(str(num) for num in list(kmerDict.values())))