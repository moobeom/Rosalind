### Generate all maximal non-branching paths in a graph ###

def MaximalNonBranchingPaths(graph):
    Paths = []
    for v in nodeList(graph):
        if not inDegree(v,graph) == outDegree(v,graph) == 1:
            if outDegree(v,graph) > 0:
                for (v,w) in edgeFind(v,graph):
                    NonBranchingPath = v+w[-1]
                    while inDegree(w,graph) == outDegree(w,graph) == 1:
                        for (w,u) in edgeFind(w,graph):
                            NonBranchingPath += u[-1]
                            w = u
                    Paths.append(NonBranchingPath)
    return Paths

def nodeList(graph):
    nodes = []
    for pair in graph:
        outNode,inNodes = pair.split('->')[0], pair.split('->')[1]
        nodes.append(outNode)
        for inNode in inNodes.split(','):
            nodes.append(inNode)
    return sorted(list(set(nodes)))

def inDegree(node,graph):
    inNodeDict = {}
    for pair in graph:
        nodes = pair.split('->')
        inNodes = nodes[1].split(',')

        for inNode in inNodes:
            if inNode not in inNodeDict:
                inNodeDict[inNode] = 1
            else:
                inNodeDict[inNode] += 1
    if node not in inNodeDict:
        inNodeDict[node] = 0
    return inNodeDict[node]

def outDegree(node,graph):
    outNodeDict = {}
    for pair in graph:
        nodes = pair.split('->')
        outNode,inNodes = nodes[0], nodes[1].split(',')
        outNodeDict[outNode] = len(inNodes)
    if node not in outNodeDict:
        outNodeDict[node] = 0
    return outNodeDict[node]

def edgeFind(node,graph):
    edgeDict = {}
    for pair in graph:
        nodes = pair.split('->')
        outNode, inNodes = nodes[0],nodes[1].split(',')

        edges = []
        for inNode in inNodes:
            edge = (outNode,inNode)
            edges.append(edge)
        edgeDict[outNode] = edges
    return edgeDict[node]

graph = ['1 -> 2','2 -> 3','3 -> 4,5','6 -> 7','7 -> 6']
paths = MaximalNonBranchingPaths(graph)
pathDict = {path[0]:path[1] for path in paths}
