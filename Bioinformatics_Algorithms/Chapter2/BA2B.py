### Find a median string ###
import itertools as it
from BA2A import HammingDistance

def MedianString(dna,k):
    distance = 100      # default
    median = ''

    base = 'ACGT'
    kmerList = [''.join(chars) for chars in it.product(*(k * (base,)))]

    for pattern in kmerList:
        if distance > Distance(pattern,dna):
            distance = Distance(pattern,dna)
            median = pattern
    return median

def Distance(pattern,dna):
    global_min = 0
    for string in dna:
        k,l = len(pattern),len(string)
        minList = []
        for i in range(l-k+1):
            substring = string[i:i+k]
            minList.append(HammingDistance(pattern,substring))

        local_min = min(minList)
        global_min += local_min
    return global_min


k = 6
dna = ['CTTGCACTTATGGGTGTTAGGGCAGTCAGGACGTGCTCTACA','GAAGGAGACTACCGCCGCATGGTCCACCTTGACCAGCCGTGC','CTAGTTATAATAATTGCCACGTGCCTGGATTAATTTGGGACG','ACTTACTTGCGTTCGTGCCACTAGGTTAGATCCGCAGCCGGG','GAGGATTCGTGCGCCGCTTTCACATGAGTCAATGGCAGCCGT',
'TCTATCTTCAAAATGCACGCTCTCAAGATTAATGGTTCGTGC',
'AGAAGTGAAAACATTGAACCGATGTCGTGCATGCCTCCAGTA',
'TGACTCCCGTGCCTCGCAGTTCTCGCGAAGGTTGTGTTTACA',
'CGTTGATCGTGCCCCTTTAACCCCTAACAGCGATTACGGGAT',
'GTCAGTGTTCGCTTGAGAATGCAAGGCCGACCGTGCGTGAAG']
print(MedianString(dna,k))