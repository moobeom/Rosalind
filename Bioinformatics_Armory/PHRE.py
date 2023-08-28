### Read quality distribution ###
from Bio import SeqIO

threshold = 26  # remove the first line in the input file
count = 0
for record in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_phre.txt","fastq"):
    phred = record.letter_annotations["phred_quality"]
    if sum(phred) / len(phred) < threshold:
        count += 1
print(count)