### Find the longest path in DAG ###
from BA5N import TopoSort

def LongestPath(graph,source,sink):
    new_graph = {}
    P,S = sorted(set(list(graph.keys()))), set()
    for v in P:
        temp = []
        for (u,w) in graph[v]:
            S.add(u)
            temp.append(u)
        new_graph[v] = temp
    S,V = sorted(S), sorted(set(list(P) + list(S)))

    W = [[0 for j in range(len(V))] for i in range(len(V))]
    for v in P:
        for (u,w) in graph[v]:
            W[v][u] = w

    s,backTrack = [-1000 for v in range(len(V))], []
    s[source] = 0
    ordered_graph = TopoSort(new_graph)
    for b in ordered_graph[(ordered_graph.index(source) +1):]:
        aList = [a for a in P if b in new_graph[a]]
        s[b] = max(s[a] + W[a][b] for a in aList)
        for a in aList:
            if s[b] == s[a] + W[a][b]:
                backTrack.append((a,b))

    path = [sink]
    while source not in path:
        b = path[-1]
        for edge in backTrack:
            if edge[1] == b:
                path.append(edge[0])
    return s[sink],path[::-1]



sample_source = 0
sample_sink = 4
sample_graph = {0:[(1,7),(2,4)], 2:[(3,2)], 1:[(4,1)], 3:[(4,3)]}
#print(LongestPath(sample_graph,sample_source,sample_sink))

test_source = 9
test_sink = 20
test_graph = {}
file = open('C:/Users/anqja/Downloads/rosalind_ba5d.txt','r')
lines =file.readlines()
adj = []
for line in lines:
    vertices = line.split('->')
    key,value,weight = int(vertices[0]), int(vertices[1].split(':')[0]), int(vertices[1].split(':')[1].rstrip())
    adj.append([key,(value,weight)])


for edge in adj:
    p,sList = edge[0], [edge[1]]
    for edge2 in adj:
        if edge != edge2 and p == edge2[0]:
            sList.append(edge2[1])
    test_graph[p] = sList
(length,path) = LongestPath(test_graph,test_source,test_sink)
answer = ''
for node in path:
    answer += str(node) + '->'
answer = answer[:-2]
print(length)
print(answer)