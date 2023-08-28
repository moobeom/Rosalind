### Find the most frequent words with mismatches in a string ###
from BA1G import HammingDistance
import itertools as it

def BetterFrequentWordsWithMismatches(text,k,d):
    patterns = []
    freqMap = {}
    n = len(text)

    for i in range(n-k):
        pattern = text[i:i+k]
        neighborhood = Neighbors(pattern,text,d)
        for j in range(len(neighborhood)-1):
            neighbor = neighborhood[j]
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1

    m = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns

def Neighbors(pattern,string,d):
    l,m = len(pattern),len(string)
    neighborhood = []
    for i in range(m-l+1):
        substring = string[i:i+l]
        if HammingDistance(pattern,substring) <= d:
            neighborhood.append(substring)
    return neighborhood

def MaxMap(freqMap):
    return max(list(freqMap.values()))


def FrequentWordsWithMismatches(text,k,d):
    patterns = []

    base = "ACGT"
    kmerList = [''.join(chars) for chars in it.product(*(k * (base,)))]
    freqMap = dict()
    for kmer in kmerList:
        freqMap[kmer] = 0

    for pattern in list(kmerList):
        l, m = len(pattern), len(string)
        count = 0
        for i in range(m-l+1):
            substring = string[i:i + l]
            if HammingDistance(pattern, substring) <= d:
                count += 1
        freqMap[pattern] = count

    m = MaxMap(freqMap)
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns


string = 'TAGATTCCGACACGTTCATAGATTCCGACACGTTCATTCGTCTGGCCACGTTCACACGTTCAAGTCAGGTCACGTTCACACGTTCATTCGTCTGGCTAGATTCCGACACGTTCAAACATTGCATAACATTGCATTTCGTCTGGCAACATTGCATAACATTGCATAACATTGCATAACATTGCATTTCGTCTGGCCACGTTCAAGTCAGGTCACGTTCATAGATTCCGATAGATTCCGATAGATTCCGATTCGTCTGGCTAGATTCCGACACGTTCAAACATTGCATCACGTTCACACGTTCAAGTCAGGTAGTCAGGTAACATTGCATTTCGTCTGGCAACATTGCATAGTCAGGTCACGTTCAAACATTGCATAGTCAGGTTTCGTCTGGCTAGATTCCGACACGTTCATAGATTCCGAAGTCAGGTAGTCAGGTTAGATTCCGATTCGTCTGGCTTCGTCTGGCTTCGTCTGGCCACGTTCATTCGTCTGGCAGTCAGGTTTCGTCTGGCTAGATTCCGAAACATTGCATAACATTGCATAACATTGCATCACGTTCACACGTTCAAGTCAGGTTTCGTCTGGCTTCGTCTGGCCACGTTCAAGTCAGGTAACATTGCATAACATTGCATCACGTTCAAACATTGCATAGTCAGGTAACATTGCATAACATTGCATTAGATTCCGATTCGTCTGGCAGTCAGGTAACATTGCATCACGTTCACACGTTCACACGTTCAAACATTGCATAGTCAGGTCACGTTCACACGTTCAAACATTGCATAACATTGCATTAGATTCCGAAACATTGCATTAGATTCCGACACGTTCATAGATTCCGATTCGTCTGGCTAGATTCCGACACGTTCAAGTCAGGTTAGATTCCGAAACATTGCAT'
k = 7
d = 2
print(FrequentWordsWithMismatches(string,k,d))