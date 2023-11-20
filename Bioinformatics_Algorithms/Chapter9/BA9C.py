### Construct the suffix tree of a string ###
def ModifiedSuffixTrieConstruction(text):       # Needs fixing
    trie = {'root': {}}
    for i in range(len(text)):
        curNode = trie['root']
        for j in range(i, len(text)):
            curSym = text[j]
            if curSym in curNode:
                curNode = curNode[curSym]
            else:
                newNode = {}
                curNode[curSym] = {'sym': curSym, 'pos': j, 'next': newNode}
                curNode = newNode
        if not curNode:
            curNode['leaf'] = i
    return trie

def FindNonbranchingPaths(trie,node,path):
    if node != 'leaf':
        if node == 'root':
            if len(trie[node].keys()) == 1:
                FindNonbranchingPaths(trie[node],list(trie[node].keys())[0],path)
        else:
            if len(trie['next'].keys()) == 1:
                nextNode = list(trie['next'].keys())[0]
                FindNonbranchingPaths(trie['next'][nextNode],nextNode,path)
        path.append(trie['sym'])
    return path[::-1]

def SuffixTreeConstruction(text):
    trie = ModifiedSuffixTrieConstruction(text)
    nbPaths = []
    for edge in trie['root']:
        path = FindNonbranchingPaths(trie['root'][edge],trie['root'][edge]['sym'],path=[])
        nbPaths.append(''.join(path))
    return nbPaths


if __name__ == '__main__':
    string = open("C:/Users/moveo/Downloads/rosalind_ba9c.txt").readline().rstrip()
    edges = SuffixTreeConstruction(string)
    for edge in edges:
        print('{}'.format(edge))