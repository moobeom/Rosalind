### Implement SmallParsimony ###

def DataToAdj(filename):
    leaves, tree = {},[]
    lines = open(filename, 'r').readlines()
    n,edges = int(lines[0].rstrip()), [line.rstrip().split('->') for line in lines[1:]]
    for i in range(n):
        leaves[i] = edges[i][1]
        tree.append((int(edges[i][0]),i))
    for (v,w) in edges[n:]:
        tree.append((int(v),int(w)))
    return tree,leaves

def RipeFind(T,tag):
    ripes = []
    internodes = list(set([v for (v,w) in T]))
    for v in internodes:
        subtree = [(vv,w) for (vv,w) in T if vv == v]
        count = 0
        for (vv,w) in subtree:
            if tag[w] == 1:
                count += 1
        if tag[v] == 0 and count == len(subtree):
            ripes.append(v)
    return ripes

def delta(i,k):
    if i == k:
        return 0
    else:
        return 1

def SmallParsimony(T,Chr):
    nodes = list(set([v for (v,w) in T])) + Chr
    tag,symbols = {}, {'A': 0,'C': 1,'G': 2,'T': 3}
    s = [[0 for j in range(len(nodes))] for i in range(len(symbols))]
    for v in range(len(nodes)):
        tag[v] = 0
        if v < len(Chr):
            tag[v] = 1
            for k in symbols:
                if Chr[v] != k:
                    s[symbols[k]][v] = 9999
    while len(RipeFind(T,tag)) > 0:
        v = RipeFind(T,tag)[0]
        tag[v] = 1
        for k in symbols:
            (daughter,son),s_i,s_j = [w for (vv,w) in T if vv == v], [], []
            for i in symbols:
                s_i.append(s[symbols[i]][daughter] + delta(i,k))
            for j in symbols:
                s_j.append(s[symbols[j]][son] + delta(j,k))
            s[symbols[k]][v] = min(s_i) + min(s_j)
    return s, min(s[symbols[k]][nodes[-(len(Chr)+1)]] for k in symbols)     # parsimony score of root

def BackTrack(profiles,m,v):
    symbols = ['A','C','G','T']
    if m == 0:
        return []
    else:
        v_profile = [profile[v] for profile in profiles[m-1]]
        candidates = [symbols[i] for i in range(len(symbols)) if v_profile[i] == min(v_profile)]
        if len(candidates) > 1:
            return BackTrack(profiles,m-1,v) + [tuple(candidates)]
        else:
            return BackTrack(profiles,m-1,v) + candidates

def NodeAssign(S,T,m,v):
    nodes = {}
    root = ''.join([candidate[0] for candidate in S[-1]])
    nodes[v-1] = root
    for i in range(v-2,-1,-1):
        p = [edge[0] for edge in T if edge[1] == i][0]
        chr = ''
        for j in range(m):
            if nodes[p][j] in strings[i][j]:
                chr += nodes[p][j]
            else:
                chr += strings[i][j][0]
        nodes[i] = chr
    return nodes

def HammingDistance(p,q):
    l = min(len(p),len(q))
    count = 0
    for i in range(l):
        if p[i] != q[i]:
            count += 1
    return count

tree,leaves = DataToAdj("C:/Users/anqja/Downloads/rosalind_ba7f (1).txt")
m = len(list(leaves.values())[0])

s,profiles = 0,[]
for i in range(m):
    leaf_frags = [leaves[leaf][i] for leaf in leaves]
    profiles.append(SmallParsimony(tree,leaf_frags)[0])
    s += SmallParsimony(tree,leaf_frags)[1]
print(s)

nn = len(sorted(list(set([v for (v,w) in tree])) + list(leaves.keys())))
strings = []
for i in range(nn):
    strings.append(BackTrack(profiles,m,i))
nodes = NodeAssign(strings,tree,m,nn)
adj = sorted(tree + [(w,v) for (v,w) in tree])
for (v,w) in adj:
    print('{}->{}:{}'.format(nodes[v],nodes[w],HammingDistance(nodes[v],nodes[w])))