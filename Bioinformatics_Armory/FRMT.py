### Data formats ###
from Bio import Entrez,SeqIO

Entrez.email = "hmb0407@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["JX462669 NM_001246828 NM_001082732 JX914595 JX469991 NM_001015511 JQ762396 NM_001135551"], rettype="fasta")
records = list(SeqIO.parse(handle,"fasta")) #we get the list of SeqIO objects in FASTA format

min, min_len = 0, len(records[0].seq)
for i in range(1,len(records)):
    if len(records[i].seq) < min_len:
        min, min_len = i, records[i].seq
print('>{}'.format(records[min].description))
print(records[min].seq)
