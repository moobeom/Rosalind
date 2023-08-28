### Computing GC Contents ###
from Bio import SeqIO

def getData(filename):
    stringDict = {string.id: str(string.seq) for string in SeqIO.parse(filename,"fasta")}
    return stringDict

def GCcount(string):
    gc = string.count("G") + string.count("C")
    return gc / len(string)


DNAdata = getData("C:/Users/anqja/Downloads/rosalind_gc.txt")
max_string, max_gc = '',0
for string in DNAdata:
    gc = GCcount(DNAdata[string])
    if gc > max_gc:
        max_string, max_gc = string, gc
print(max_string)
print(max_gc*100)