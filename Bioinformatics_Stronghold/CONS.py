### Consensus and profile ###
from Bio import SeqIO

def getData(filename):
    stringDict = {string.id: str(string.seq) for string in SeqIO.parse(filename,"fasta")}
    return stringDict

def makeProfile(strings):
    profile = []
    for i in range(len(strings[0])):
        symbolCounts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for string in strings:
            symbolCounts[string[i]] += 1
        profile.append(symbolCounts)
    consensus = ''
    for counts in profile:
        consensus += max(counts,key=counts.get)
    return profile,consensus


strings = list(getData("C:/Users/anqja/Downloads/rosalind_cons.txt").values())
profile,consensus = makeProfile(strings)
print(consensus)
symbols = ['A','C','G','T']
for i in range(len(symbols)):
    print(symbols[i] + ':' + ' ' +' '.join([str(counts[symbols[i]]) for counts in profile]))