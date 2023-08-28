###  Finding a shared motif ###
from Bio import SeqIO

def getData(filename):
    stringDict = {string.id: str(string.seq) for string in SeqIO.parse(filename,"fasta")}
    return stringDict


def LCSM(strings):
    s = min(strings,key=len)
    targets = [string for string in strings if string != s]
    for j in range(len(s), 1, -1):
        for i in range(len(s)-j+1):
            substring = s[i : i+j]
            count = 0
            for t in targets:
                if substring in t:
                    count += 1
                else:
                    break
            if count == len(targets):
                return substring



strings = getData("C:/Users/anqja/Downloads/rosalind_lcsm (1).txt")
print(LCSM(list(strings.values())))