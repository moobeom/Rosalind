### Enumerating k-mers lexicographically ###
import itertools as it

alphabets,k = 'ABCDE', 4
kmerList = [''.join(chars) for chars in it.product(*(k*(alphabets,)))]
for kmer in kmerList:
    print(kmer)