### Constructing a string spelled by a gapped genome path ###
import itertools as it
from BA3J import StringReconstruction

lines = open('C:/Users/anqja/Downloads/rosalind_ba3l_sample.txt').readlines()
k,d = [int(x) for x in lines[0].split()]
gapped_patterns = []
for line in lines[1:]:
    gapped_patterns.append(line)
print(StringReconstruction(d,gapped_patterns))
