### Introduction to random strings ###
from math import log10

def CalRandomString(string,gc_p):
    p = 1
    symbFreq = {'A':(1-gc_p)/2, 'C':gc_p/2, 'G':gc_p/2,'T':(1-gc_p)/2}
    for symbol in string:
        p *= symbFreq[symbol]
    return p

data = open("C:/Users/anqja/Downloads/rosalind_prob.txt").readlines()
string, probs = data[0].rstrip(), [float(num) for num in data[1].rstrip().split()]
print(' '.join([str(log10(CalRandomString(string,prob))) for prob in probs]))