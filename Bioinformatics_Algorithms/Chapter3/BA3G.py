### Find an Eulerian path in a graph ###
from BA3F import edgeFind,adjMaker,startFind,dfs
import itertools as it


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




graph = 'C:/Users/anqja/Downloads/rosalind_ba3g.txt'
path = EulerianPath(graph)
answer = '->'.join(path)
print(answer)