### Perfect matching and RNA secondary structures ###
from Bio import SeqIO
from math import factorial

string = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_pmch.txt","fasta").seq)
print(factorial(string.count('A')) * factorial(string.count('C')))