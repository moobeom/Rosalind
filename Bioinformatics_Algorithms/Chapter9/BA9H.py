### Pattern matching with the suffix array ###
from BA9G import SuffixArrayConstruction

def PatternMatchingWithSuffixArray(text,pattern,suffixArray):
    minIdx, maxIdx = 0, len(text) -1
    midIdx = (minIdx + maxIdx) // 2
    while minIdx <= maxIdx:
        midIdx = (minIdx + maxIdx) // 2
        if pattern > text[suffixArray[midIdx]:]:
            minIdx = midIdx + 1
        else:
            maxIdx = midIdx - 1
    if pattern == text[suffixArray[midIdx]: suffixArray[midIdx] + len(pattern)]:
        first = minIdx
    else:
        if pattern == text[suffixArray[midIdx+1]: suffixArray[midIdx+1] + len(pattern)]:
            first = minIdx
        else:
            return "Pattern does not appear in the string"

    minIdx, maxIdx = first, len(text) -1
    while minIdx <= maxIdx:
        midIdx = (minIdx + maxIdx) // 2
        if pattern == text[suffixArray[midIdx]: suffixArray[midIdx] + len(pattern)]:
            minIdx = midIdx + 1
        else:
            maxIdx = midIdx - 1
    last = maxIdx
    return (first,last)

if __name__ == '__main__':
    lines = open("C:/Users/moveo/Downloads/rosalind_ba9h (5).txt").readlines()
    string, reads = lines[0].rstrip(), [read.rstrip() for read in lines[1:]]
    suffixArray = SuffixArrayConstruction(string)
    posList = []
    for read in reads:
        first,last = PatternMatchingWithSuffixArray(string,read,suffixArray)
        posList.append(suffixArray[first:last+1])
    answer = sorted(sum(posList,[]))
    print(' '.join(str(pos) for pos in answer))