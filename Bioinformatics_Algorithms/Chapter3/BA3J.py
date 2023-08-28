### Reconstruct a string from its paired composition ###
import itertools as it
from BA3H import EulerianPath

def StringReconstruction(d,pairedReads):
    pdB = PairedDeBruijn(pairedReads)
    path = EulerianPath(pdB)
    text = PathToGenome(d,path)
    return text

#####################################################################################
# functions for constructing a paired de Bruijn graph
def PairedDeBruijn(pairedReads):
    comp = PairedComposition(pairedReads)
    elements = Gluing(comp)
    pdB = []
    for element in elements:
        suffixes = ['|'.join(suffix) for suffix in element[1]]
        edge = '{}->{}'.format('|'.join(element[0]), ','.join(suffixes))
        pdB.append(edge)
    return pdB

def PairedComposition(pairedReads):
    presuffixList = []
    for pairedRead in pairedReads:
        reads = pairedRead.split('|')
        prefixes, suffixes = (reads[0][:-1],reads[1][:-1]), (reads[0][1:],reads[1][1:])
        presuffixList.append((prefixes,suffixes))
    return sorted(presuffixList)

def Gluing(graph):
    pairedNodes = [nodes[0] for nodes in graph]

    glued_graph, checked = [], []
    for pairedNode in pairedNodes:
        if pairedNode not in checked:
            fork = []
            for copied_pairedNode in graph:
                if pairedNode == copied_pairedNode[0]:
                    fork.append(copied_pairedNode[1])
            glued_graph.append((pairedNode, fork))
            checked.append(pairedNode)
    return glued_graph
#####################################################################################

#####################################################################################
# functions for constructing a string from the Eulerian path
def PathToGenome(d,path):
    edgeList = edgeRestore(path)
    l, string = len(edgeList), ''
    for i in range(l-1):
        string += edgeList[i][0]

    lastKmers = edgeList[-1].split('|')
    gap = GapFind(d,edgeList)
    string += lastKmers[0] + gap + lastKmers[1]
    return string

def edgeRestore(path):
    edgeList = []
    for i in range(len(path)-1):
        prefixes,suffixes = path[i].split('|'),path[i+1].split('|')
        edge1,edge2 = prefixes[0]+suffixes[0][-1], prefixes[1]+suffixes[1][-1]
        edgeList.append('{}|{}'.format(edge1,edge2))
    return edgeList

def GapFind(d,edgeList):
    letter = ''
    for i in range(1,d+1):
        letter += edgeList[-(i+1)].split('|')[1][0]
    return letter[::-1]

