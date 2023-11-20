### Implement BetterBWMatching ###

def CountSymbol(idx,lastCol,sym):
    return ''.join(c for i,c in lastCol[:idx]).count(sym)

def BetterBWMatching(FirstOccurrence,lastCol,pattern):
    top = 0
    bot = len(lastCol) - 1
    while top <= bot:
        if len(pattern) > 0:
            sym = pattern[-1]
            pattern = pattern[:-1]
            l_indices = [i for (i, c) in lastCol[top:bot + 1] if c == sym]
            if len(l_indices) > 0:
                top = FirstOccurrence[sym] + CountSymbol(top, lastCol, sym)
                bot = FirstOccurrence[sym] + CountSymbol(bot + 1, lastCol, sym) - 1
            else:
                return 0
        else:
            return bot - top + 1

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba9m (4).txt').readlines()
    string, kmers = lines[0].rstrip(), lines[1].split(' ')
    lastCol = [(i, c) for i, c in enumerate(string)]
    firstCol = sorted(lastCol, key=lambda x:x[1])

    FirstOccurrence = {}
    for idx,sym in enumerate([c for (i,c) in firstCol]):
        if sym not in FirstOccurrence.keys():
            FirstOccurrence[sym] = idx

    counts = []
    for kmer in kmers:
        counts.append(BetterBWMatching(FirstOccurrence,lastCol,kmer))
    print(' '.join([str(j) for j in counts]))