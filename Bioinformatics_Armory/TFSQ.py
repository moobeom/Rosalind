### FASTQ format introduction ###
from Bio import SeqIO

with open("C:/Users/anqja/Downloads/rosalind_tfsq.txt", "r") as input_handle,open("C:/Users/anqja/Downloads/rosalind_tfsq_fasta.txt", "w") as output_handle:
    sequences = SeqIO.parse(input_handle, "fastq")
    fastq2fasta = SeqIO.write(sequences, output_handle, "fasta")