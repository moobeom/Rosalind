from Bio import Entrez
Entrez.email = "hmb0407@gmail.com"
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism]')
record = Entrez.read(handle)
print(record["Count"])