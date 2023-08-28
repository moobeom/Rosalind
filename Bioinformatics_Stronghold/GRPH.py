### Overlap graphs ###
from Bio import SeqIO

def getData(filename):
    stringDict = {string.id: str(string.seq) for string in SeqIO.parse(filename,"fasta")}
    return stringDict

def Overlap(stringDict,k):
    adj = []
    for s in stringDict:
        for t in stringDict:
            if stringDict[s] != stringDict[t]:
                if str(stringDict[s])[-k:] == str(stringDict[t])[:k]:
                    adj.append([s,t])
    return adj



strings = getData("C:/Users/anqja/Downloads/rosalind_grph.txt")
for overlaps in Overlap(strings,3):
    print(' '.join([str(id) for id in overlaps]))
