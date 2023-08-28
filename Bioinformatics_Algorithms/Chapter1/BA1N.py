### Generate the d-Neighborhood of a string ###

def Neighbors(pattern,d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A','C','G','T'}
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Suffix(pattern),d)
    for text in SuffixNeighbors:
        if HammingDistance(Suffix(pattern),text) < d:
            for x in ['A','C','G','T']:
                Neighborhood.add(x + text)
        else:
            Neighborhood.add(FirstSymbol(pattern) + text)
    return Neighborhood

def Suffix(text):
    return text[1:]

def HammingDistance(p,q):
    return sum([x != y for x,y in zip(p,q)])

def FirstSymbol(text):
    return text[0]

neighbors = Neighbors('TAACTCAGCG',3)
for neighbor in neighbors:
    print(neighbor)