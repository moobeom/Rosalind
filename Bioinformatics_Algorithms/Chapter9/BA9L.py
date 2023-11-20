### Implement BWMatching ###
from BA9K import LastToFirst

def BWMatching(lastCol,pattern):
    bwt = ''.join(c for i,c in lastCol)
    top = 0
    bot = len(lastCol) -1
    while top <= bot:
        if len(pattern) > 0:
            sym = pattern[-1]
            pattern = pattern[:-1]
            l_indices = [i for (i,c) in lastCol[top:bot+1] if c == sym]
            if len(l_indices) > 0:
                top_idx, bot_idx = min(l_indices), max(l_indices)
                top, bot = LastToFirst(bwt,top_idx), LastToFirst(bwt,bot_idx)
            else:
                return 0
        else:
            return bot - top + 1

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba9l (4).txt').readlines()
    string, kmers = lines[0].rstrip(), lines[1].split(' ')
    lastCol = [(i, c) for i, c in enumerate(string)]
    posList = []
    for kmer in kmers:
        posList.append(BWMatching(lastCol,kmer))
    print(' '.join([str(pos) for pos in posList]))