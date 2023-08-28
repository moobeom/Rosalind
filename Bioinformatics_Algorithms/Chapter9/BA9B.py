### Implement TrieMatching ###
from BA9A import TrieConstruct

def TrieMatching(text,trie):
    indices = []
    idx = 0
    while len(text) > 0:
        if PrefixTrieMatching(text,trie) != "no matches found":
            indices.append(idx)
        idx += 1
        text = text[1:]
    return indices

def PrefixTrieMatching(text,trie,level=0):
    symbol = text[level]
    v = trie['root']
    path = ''

    while True:
        if bool(v) is False:    # if v is a leaf, meaning that dict(v) is empty(false)
            return path
        elif symbol in v:
            path += symbol
            v = v[[w for w in v if w == symbol][0]]
            if level < len(text) -1:
                symbol = text[level + 1]
                level += 1
        else:
            return "no matches found"


strings = [line.rstrip() for line in open("C:/Users/anqja/Downloads/rosalind_BA9B.txt").readlines()]
text,patterns = strings[0], strings[1:]
trie = TrieConstruct(patterns)
print(" ".join(str(idx) for idx in TrieMatching(text,trie)))