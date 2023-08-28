### Base quality distribution ###
from Bio import SeqIO

q = 22      # quality threshold
phred_sum, num = [], 0
for record in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_bphr (1).txt","fastq"):
    phreds = record.letter_annotations["phred_quality"]
    if phred_sum == []:
        phred_sum = sum(phred_sum,phreds)
    else:
        phred_sum = [x + y for x,y in zip(phreds,phred_sum)]
    num += 1
count = 0
for s in phred_sum:
    if s / num < q:
        count += 1
print(count)
