### Genome assembly with perfect coverage ###

def CyclicSuperstring(kmers):
    k_1mers = {kmer[:-1]: kmer[1:] for kmer in kmers}
    keys = list(k_1mers)
    CSP,l = keys[0], len(keys[0])
    for i in range(len(keys)):
        CSP += k_1mers[CSP[i:i+l]][-1]
    return CSP[:len(keys)]

lines = open("C:/Users/anqja/Downloads/rosalind_pcov.txt").readlines()
substrings = [line.rstrip() for line in lines]
print(CyclicSuperstring(substrings))