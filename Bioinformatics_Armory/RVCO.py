### Complementing a strand of DNA ###
from Bio import SeqIO
from Bio.Seq import Seq

count = 0
strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_rvco.txt","fasta")]
rc_strings = [str(Seq(string).reverse_complement()) for string in strings]
for i in range(len(strings)):
    if strings[i] == rc_strings[i]:
        count += 1
print(count)