### Pairwise global alignment ###

from Bio import Entrez, SeqIO, pairwise2
''' alignment functions description

1. global or local
2. character code (first: match parameter, second: gap penalty parameter)
    2.1. match parameter description
    x     No parameters. Identical characters have score of 1, else 0.
    m     A match score is the score of identical chars, else mismatch score.
    d     A dictionary returns the score of any pair of characters.
    c     A callback function returns scores.

    2.2 gap penalty parameter description
    x     No gap penalties.
    s     Same open and extend gap penalties for both sequences.
    d     The sequences have different open and extend gap penalties.
    c     A callback function returns the gap penalties.

ex) globalxx, globalmx, globalms, ...
'''


Entrez.email = "hmb0407@gmail.com"
handle = Entrez.efetch(db="nucleotide", id=["JX317645.1 FJ817486.1"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])
# scores for match=5, mismatch=-4 (ACGT of DNAFULL), gap opening penalty=-10, gap extension penalty=-1
