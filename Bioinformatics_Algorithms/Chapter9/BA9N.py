### Find all occurrences of a collection of patterns in a string ###
from BA9I import BWT
from BA9Q import PartialSuffixArray

def CheckPointArray(bwt, C):
    syms = list(set(bwt))
    checkpoint_arr = {}
    for idx in range(0, len(bwt), C):
        checkpoint_arr[idx] = {}
        for sym in syms:
            checkpoint_arr[idx][sym] = bwt[:idx].count(sym)
    return checkpoint_arr

def CountSymbol(cp_arr,idx,lastCol,sym):
    partial_indices = [x for x in cp_arr.keys() if x <= idx]
    max_idx = max(partial_indices)
    count = cp_arr[max_idx][sym]
    count += ''.join(c for i,c in lastCol[max_idx:idx]).count(sym)
    return count

def BetterBWMatching(FirstOccurrence,lastCol,pattern,cp_arr):
    top = 0
    bot = len(lastCol) - 1
    while top <= bot:
        if len(pattern) > 0:
            sym = pattern[-1]
            pattern = pattern[:-1]
            l_indices = [i for (i, c) in lastCol[top:bot + 1] if c == sym]
            if len(l_indices) > 0:
                top = FirstOccurrence[sym] + CountSymbol(cp_arr, top, lastCol, sym)
                bot = FirstOccurrence[sym] + CountSymbol(cp_arr, bot + 1, lastCol, sym) - 1
            else:
                return False, False
        else:
            return top, bot

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba9n (1).txt').readlines()
    string, kmers = lines[0].rstrip(), [kmer.rstrip() for kmer in lines[1:]]
    bwt = BWT(string + '$')
    lastCol = [(i, c) for i, c in enumerate(bwt)]
    firstCol = sorted(lastCol, key=lambda x:x[1])

    FirstOccurrence = {}
    for idx,sym in enumerate([c for (i,c) in firstCol]):
        if sym not in FirstOccurrence.keys():
            FirstOccurrence[sym] = idx
    checkpoints = CheckPointArray(bwt, C=100)
    pSuffixArray = PartialSuffixArray(string+'$', k=100)

    posList = []
    for kmer in kmers:
        top, bot = BetterBWMatching(FirstOccurrence, lastCol, kmer, checkpoints)
        if top:
            for idx in range(top, bot + 1):
                backtrack = 0
                while idx not in pSuffixArray.keys():
                    sym = [c for i,c in lastCol][idx]
                    idx = FirstOccurrence[sym] + CountSymbol(checkpoints, idx, lastCol, sym)
                    backtrack += 1
                posList.append(pSuffixArray[idx] + backtrack)
    print(' '.join([str(j) for j in sorted(posList)]))