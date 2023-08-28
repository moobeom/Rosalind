### Base filtration by quality ###
from Bio import SeqIO

def TrimFASTQ(record,threshold):
    phreds = record.letter_annotations["phred_quality"]
    global i,j
    # leading
    for i in range(len(phreds)):
        if phreds[i] >= threshold:
            break
    # trailing
    for j in range(len(phreds)-1,-1,-1):
        if phreds[j] >= threshold:
            break
    return record[i:j+1].format("fastq").rstrip()


q = 18      # quality cut-off value
for record in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_bfil (3).txt","fastq"):
    print(TrimFASTQ(record,q))