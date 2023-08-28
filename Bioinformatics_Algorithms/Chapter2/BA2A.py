### Implement motif enumeration ###
import itertools as it

def HammingDistance(p,q):
    l = min(len(p),len(q))
    count = 0
    for i in range(l):
        if p[i] != q[i]:
            count += 1
    return count

def Neighbors(pattern,d):
    neighborhood = []
    k = len(pattern)

    base = 'ACGT'
    kmerList = [''.join(chars) for chars in it.product(*(k * (base,)))]
    for kmer in kmerList:
        if HammingDistance(pattern,kmer) <= d:
            neighborhood.append(kmer)
    return neighborhood


def MotifEnumeration(dna,k,d):
    patterns = set()
    firstString = dna[0]
    l,n = len(firstString), len(dna)

    for i in range(l-k+1):
        pattern = firstString[i:i+k]
        patternList = Neighbors(pattern,d)


        for sub_pattern in patternList:
            count = 0
            for j in range(1,n):
                for a in range(l-k+1):
                    substring = dna[j][a:a+k]
                    if HammingDistance(sub_pattern,substring) <= d:
                        count += 1
                        break
            if count == n-1:
                patterns.add(sub_pattern)

    return patterns

data = ['GTTGTGTCCCTCGATCCAGAGGGGC',
'TAACCCACCCGTGCCGGGGGGTATT',
'ACGACGGGGGCGTGAGGTTATCCGA',
'GGGGAATAACACTTATGTTAGCCCG',
'TCGAAGTAATGGCCTGGGGTCATCC',
'GCACAAATCGTGCTATTGCGGGGGC',
'GGGGCTAACAGTGCTAAGCGCTGAC',
'GCCCGGACCACAGAGGGGGAACTAT',
'CGTACTTAAAGGGGTCTCATAGACC',
'GGGGAGCGGTTCTCCCAAACGTGCC']
k = 5
d = 1
#print(MotifEnumeration(data,k,d))

answer = ''
for ans in MotifEnumeration(data,k,d):
    answer += ans + ' '

answer = answer[:-1]
print(answer)