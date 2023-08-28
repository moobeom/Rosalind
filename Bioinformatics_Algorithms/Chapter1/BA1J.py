### Find frequent words with mismatches and reverse complements ###
from BA1C import reverse_complement
from BA1G import HammingDistance
from BA1I import MaxMap
import itertools as it

def FrequentWordsWithMismatches_rc(text,k,d):
    patterns = []

    base = "ACGT"
    kmerList = [''.join(chars) for chars in it.product(*(k * (base,)))]
    freqMap = dict()
    for kmer in kmerList:
        freqMap[kmer] = 0

    for pattern in kmerList:
        l, m = len(pattern), len(text)
        count = 0
        for i in range(m-l+1):
            substring = text[i:i+l]
            if HammingDistance(pattern, substring) <= d:
                count += 1

            pattern_rc = reverse_complement(pattern)
            if HammingDistance(pattern_rc, substring) <= d:
                count += 1
        freqMap[pattern] = count

    m = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

string = 'CAGCCAACAGCCAAACCCCGCTAATCCGTATAATCCGTAACCCCGCTAATCCGTAACCCCGCACGGTTCCTAGGTTCCACGGTTCCTAGGTTCCCAGCCAACAGCCAAACCCCGCCAGCCAAAGGTTCCACGGTTCCTACGGTTCCTAGGTTCCCAGCCAAACCCCGCACCCCGCACCCCGCACCCCGCACGGTTCCTAGGTTCCCAGCCAAAGGTTCCTAATCCGTAACGGTTCCTACCCCGCACCCCGCACCCCGCCAGCCAATAATCCGTAACCCCGCACGGTTCCTCAGCCAAACCCCGCCAGCCAATAATCCGTAACCCCGCACGGTTCCTACGGTTCCTCAGCCAAACGGTTCCTTAATCCGTATAATCCGTACAGCCAAAGGTTCCACGGTTCCTAGGTTCCACCCCGCAGGTTCCCAGCCAAACCCCGCACGGTTCCTCAGCCAAACGGTTCCTACCCCGCAGGTTCCACCCCGCAGGTTCCAGGTTCCCAGCCAAACCCCGCAGGTTCCCAGCCAAAGGTTCCAGGTTCCTAATCCGTAACGGTTCCTAGGTTCCACCCCGCACCCCGCACGGTTCCTTAATCCGTAACCCCGCACCCCGCACGGTTCCTTAATCCGTAAGGTTCCACCCCGCACGGTTCCTACGGTTCCTAGGTTCCCAGCCAAAGGTTCCAGGTTCCACCCCGCACGGTTCCTAGGTTCCAGGTTCCTAATCCGTAACGGTTCCTAGGTTCCACCCCGCAGGTTCCACGGTTCCTACCCCGCACGGTTCCTTAATCCGTAAGGTTCCAGGTTCCCAGCCAATAATCCGTAACGGTTCCTCAGCCAATAATCCGTA'
k = 6
d = 2
print(FrequentWordsWithMismatches_rc(string,k,d))