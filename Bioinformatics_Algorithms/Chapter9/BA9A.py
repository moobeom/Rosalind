### Construct a trie from a collection of patterns ###

def TrieConstruct(patterns):
    trie = {'root': {}}
    for pattern in patterns:
        curNode = trie['root']
        for i in range(len(pattern)):
            curSym = pattern[i]
            if curSym in curNode:
                curNode = curNode[curSym]
            else:
                newNode = {}
                curNode[curSym] = newNode
                curNode = newNode
    return trie

def Trie2Adj(trie):
    adj = {}
    def traverse(node,i):
        nonlocal adj
        for symbol, childNode in node.items():
            j = len(adj)
            adj[i].append((symbol,j))
            adj[j] = []
            traverse(childNode,j)
    adj[0] = []
    traverse(trie['root'], 0)
    return adj

'''
strings = [line.rstrip() for line in open("C:/Users/anqja/Downloads/rosalind_BA9A_sample.txt").readlines()]
trie = TrieConstruct(strings)
adjList = Trie2Adj(trie)
nodes = []
for i in adjList:
    if adjList[i] != []:
        for childNode,j in adjList[i]:
            nodes.append((i,j,childNode))

for i,j,node in nodes:
    print('{}->{}:{}'.format(i,j,node))
    '''
