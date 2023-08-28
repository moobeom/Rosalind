### Constructing a De Bruijn graph ###

def getData(filename):
    lines = open(filename).readlines()
    strings = []
    for string in lines:
        strings.append(string.rstrip())
        strings.append(ReverseComplement(string.rstrip()))
    return strings

def ReverseComplement(string):
    basepair = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rc_string = ''
    for base in string:
        rc_string += basepair[base]
    return rc_string[::-1]

def DeBruijn(k_1mers):
    k, kmers = len(k_1mers[0])-1, []
    for k_1mer in k_1mers:
        if (k_1mer[:k],k_1mer[1:k+1]) not in kmers:
            kmers.append((k_1mer[:k],k_1mer[1:k+1]))
    return sorted(kmers)

strings = getData("C:/Users/anqja/Downloads/rosalind_dbru (1).txt")
edges = DeBruijn(strings)
for edge in edges:
    print('({}, {})'.format(edge[0],edge[1]))