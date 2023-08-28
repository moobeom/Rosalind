### Protein translation ###
from Bio.Seq import translate

lines = open("C:/Users/anqja/Downloads/rosalind_ptra_sample.txt").readlines()
string, peptide = lines[0].rstrip(), lines[1].rstrip()
codon_table_indices = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23]
for i in codon_table_indices:
    if translate(string,table=i,to_stop=True) == peptide:
        print(i)
        break