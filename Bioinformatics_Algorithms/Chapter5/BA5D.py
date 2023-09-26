### Find the longest path in DAG ###
from BA5N import TopoSort

def LongestPath(graph,source,sink,unweighted_graph,nodes):
    s,backtrack = {node: float('-inf') for node in nodes}, {}
    ordered_graph = TopoSort(unweighted_graph)
    s[source] = 0
    for b in ordered_graph:     # a:predecessor, b:successor
        aList = [a for a in unweighted_graph if (a,b) in graph]
        for a in aList:
            if s[a] + graph[(a, b)] > s[b]:
                s[b] = s[a] + graph[(a, b)]
                backtrack[b] = a
    path = [sink]
    while source not in path:
        path.append(backtrack[path[-1]])
    return s[sink], path[::-1]


if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5d (2).txt').readlines()
    source, sink = int(lines[0]), int(lines[1])
    graph, nodes = {}, set()
    for line in lines[2:]:
        subgraph = line.split('->')
        v, u, weight = int(subgraph[0]), int(subgraph[1].split(':')[0]), int(subgraph[1].split(':')[1].rstrip())
        graph[(v,u)] = weight
        nodes.add(v) or nodes.add(u)
    unweighted_graph = {}
    for v,u in graph:
        if v in unweighted_graph:
            unweighted_graph[v].append(u)
        else:
            unweighted_graph[v] = [u]
    score, path = LongestPath(graph,source,sink,unweighted_graph,nodes)
    print(score)
    print('->'.join([str(node) for node in path]))