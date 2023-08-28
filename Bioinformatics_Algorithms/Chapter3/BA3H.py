### Reconstruct a string from its k-mer composition ###
import itertools as it
import sys
sys.setrecursionlimit(10**7)

def StringReconstruction(patterns):
    dB = DeBruijn(patterns)
    path = EulerianPath(dB)
    text = PathToGenome(path)
    return text

#####################################################################################
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
def EulerianPath(graph):
    # 1. assign kmers to numbers in lexicographic order
    edges = edgeFind(graph)
    nodes = sorted(list(set(it.chain(*edges))))
    n = len(nodes)

    nodeDict = {}
    for i in range(n):
        nodeDict[nodes[i]] = i
    new_edges = []
    for edge in edges:
        new_edges.append([nodeDict[edge[0]],nodeDict[edge[1]]])

    # 2. finding the starting node and ending node, and adding an extra edge
    indegrees, outdegrees = [edge[0] for edge in new_edges], [edge[1] for edge in new_edges]

    indegreeDict, outdegreeDict = {},{}
    for i in range(n):
        counts = indegrees.count(i)
        indegreeDict[i] = counts
        counts = outdegrees.count(i)
        outdegreeDict[i] = counts

    startingNode, endingNode = 0,0  # default
    for i in range(n):
        if indegreeDict[i] - outdegreeDict[i] > 0:
            startingNode = i
        elif indegreeDict[i] - outdegreeDict[i] < 0:
            endingNode = i
    #new_edges.append([endingNode,startingNode])

    # 3. construct the Eulerian cycle
    adj = adjMaker(n,new_edges)

    start, path = startingNode, []
    dfs(start, n, adj, path)
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
