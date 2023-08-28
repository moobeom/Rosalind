### Find a spliced motif ###
from Bio import SeqIO

def FindMotifIndex(string,motif):
    idxList = [-1]
    for symbol in motif:
        idx = string.index(symbol)
        while idxList[-1] > idx:
            idx += string[idx+1:].index(symbol) + 1
        idxList.append(idx+1)
    return idxList[1:]

strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_sseq.txt","fasta")]
print(' '.join([str(num) for num in FindMotifIndex(strings[0],strings[1])]))
