### Finding a protein motif ###
import urllib.request
from Bio import SeqIO

def getData(filename):
    lines = open(filename).readlines()
    ids,strings = [id.rstrip() for id in lines], []
    for id in ids:
        urllib.request.urlretrieve("http://www.uniprot.org/uniprot/" + id + ".fasta", "protein.fa")
        string = SeqIO.read("protein.fa","fasta")
        strings.append(str(string.seq))
    return ids,strings

def MotifFind(string):
    locs = []
    for i in range(len(string)):
        if string[i] == 'N' and string[i+1] != 'P' and string[i+2] in ['S','T'] and string[i+3] != 'P':
            locs.append(i+1)
    return locs

ids,strings = getData("C:/Users/anqja/Downloads/rosalind_mprt.txt")
for i in range(len(ids)):
    locations = MotifFind(strings[i])
    if locations != []:
        print(ids[i])
        print(' '.join([str(loc) for loc in locations]))