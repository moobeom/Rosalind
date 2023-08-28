### Find a k-universal circular string ###
import itertools as it


def BinGen(k):
    max = 2**k
    binkmerList = []
    for i in range(max):
        num,zeros = format(i,'b'), len(str(format(max,'b'))) -1
        binkmerList.append('{}'.format(num).zfill(zeros))
    return binkmerList

def KUCS(k):
    binary_kmers = BinGen(k)
    dB = DeBruijn(binary_kmers)
    cycle = EulerianCycle(dB)[:-(k-1)]
    text = PathToGenome(cycle)
    return text


# functions for constructing a de Bruijn graph
def DeBruijn(patterns):
    comp = Composition(patterns)
    pairs = Gluing(comp)
    dB = []
    for pair in pairs:
        edge = '{}->{}'.format(pair[0],','.join(pair[1]))
        dB.append(edge)
    return dB

def Composition(patterns):
    presuffixList = []
    for pattern in patterns:
        presuffixList.append((pattern[:-1],pattern[1:]))
    return sorted(presuffixList)

def Gluing(graph):
    nodes = [nodes[0] for nodes in graph]

    glued_graph, checked = [], []
    for node in nodes:
        if node not in checked:
            fork = []
            for pair in graph:
                if node == pair[0]:
                    fork.append(pair[1])
            glued_graph.append((node, fork))
            checked.append(node)
    return glued_graph
#####################################################################################

#####################################################################################
# functions for constructing an Eulerian path
def EulerianCycle(graph):
    edges = edgeFind(graph)
    nodes = sorted(list(set(it.chain(*edges))))
    n = len(nodes)

    nodeDict = {}
    for i in range(n):
        nodeDict[nodes[i]] = i
    new_edges = []
    for edge in edges:
        new_edges.append([nodeDict[edge[0]], nodeDict[edge[1]]])

    adj = adjMaker(n,new_edges)
    start, path = 0, []
    dfs(start,n,adj,path)
    path = list(reversed(path))

    restored_path = []
    for node in path:
        for original in nodeDict:
            if nodeDict[original] == node:
                restored_path.append(str(original))
    return restored_path

def edgeFind(graph):
    edges = []
    for edge in graph:
        nodes = edge.split('->')
        if ',' in nodes[1]:
            values = nodes[1].split(',')
            for value in values:
                edges.append([nodes[0],value])
        else:
            edges.append([nodes[0],nodes[1]])
    return edges

def adjMaker(n,edges):
    adj = [[0] * (n) for element in range(n)]
    for edge in edges:
        adj[edge[0]][edge[1]] = 1
    return adj

def startFind(start,n,adj):
    for i in range(n):
        count = 0
        for j in range(n):
            count += adj[i][j]
        if start == 0 and count > 0:
            start = i

def dfs(node,n,adj,path):
    for next in range(n):
        if adj[node][next] > 0:
            adj[node][next] -= 1
            dfs(next,n,adj,path)
    path.append(node)
#####################################################################################

#####################################################################################
def PathToGenome(path):
    l,string = len(path), ''
    for i in range(l):
        if i == 0:
            string = path[0]
        else:
            string += path[i][-1]
    return string

k = 8
print(KUCS(k))