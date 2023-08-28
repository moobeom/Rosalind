### Matching random motifs ###

def CalRandomString(string,gc_p):
    p = 1
    symbFreq = {'A':(1-gc_p)/2, 'C':gc_p/2, 'G':gc_p/2,'T':(1-gc_p)/2}
    for symbol in string:
        p *= symbFreq[symbol]
    return p

N = 80003
gc_p = 0.552214
string = 'TTCCGCTAAC'
print(1 - (1 - CalRandomString(string,gc_p)) ** N)
