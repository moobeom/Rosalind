### Ordering strings of varying length lexicographically ###
from itertools import product

alphabets = 'LAUBTNJCDWI'
k = 3
SymbolValues = {' ':0}
kmers = []
for i in range(len(alphabets)):
    SymbolValues[alphabets[i]] = i+1
for i in range(k):
    kmers.append([kmer + ' ' * (k-i-1) for kmer in [''.join(chars) for chars in product(*((i + 1) * (alphabets,)))]])

kmerDict = dict()
for kmerList in kmers:
    for kmer in kmerList:
        value = 0
        for i in range(k):
            value += SymbolValues[kmer[i]] * 16 ** (k-i)        # at most 12 symbols which makes hexadecimal notation available
        kmerDict[kmer] = value

sortedKmers = [str(kmer[0]).rstrip() for kmer in sorted(kmerDict.items(), key=lambda x:x[1])]     # sort the dictionary in an increasing order
for kmer in sortedKmers:
    print(kmer)