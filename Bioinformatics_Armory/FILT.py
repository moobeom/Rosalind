### Read filtration by quality ###
from Bio import SeqIO

q,p = 20, 57        # quality threshold, percentage of bases
count = 0
for record in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_filt.txt","fastq"):
    phreds = record.letter_annotations["phred_quality"]
    if len([s for s in phreds if s >= q]) / len(phreds) * 100 >= p:
        count += 1
print(count)