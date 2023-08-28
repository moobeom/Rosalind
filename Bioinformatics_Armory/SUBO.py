### Suboptimal local alignment ###
from Bio import SeqIO

def HammingDistance(p,q):
    return sum([x != y for x,y in zip(p,q)])

def PatternOccurrence(string,pattern):
    count = 0
    for i in range(len(string)-len(pattern)+1):
        if HammingDistance(string[i:i+len(pattern)],pattern) <= 3:
            count += 1
    return count


strings = [str(string.seq) for string in SeqIO.parse("C:/Users/anqja/Downloads/rosalind_subo_sample.txt","fasta")]
# suboptimal local alignment tool site: "https://www.ebi.ac.uk/Tools/psa/lalign/"
laligned_v = 'GACTCCTTTGTTTGCCTTAAATAGATACATATTTA---------CTCTT---------GACTCTTTTGTTGGCCTTAAATAGATACATATTTG'
laligned_w = 'GACTCCTTTGTTTGCCTTAAATAGATACATATTCAACAAGTGTGCACTTAGCCTTGCCGACTCCTTTGTTTGCCTTAAATAGATACATATTTG'
pattern = 'GACTCCTTTGTTTGCCTTAAATAGATACATATTTA'    # need an algorithm to find a pattern
print(PatternOccurrence(laligned_v,pattern), PatternOccurrence(laligned_w,pattern))
