### Compute the 2-break distance between a pair of genomes ###

def Genome(p):
    chromosomes = p.split(')(')
    for chr in chromosomes:
        new_chr = chr.lstrip('(').rstrip(')').split()
        chromosomes[chromosomes.index(chr)] = new_chr
    return chromosomes

def NodeMaker(genome):
    blocks = sum(genome,[])
    nodes = [0] * (2*len(blocks))
    for j in range(len(blocks)):
        i = int(blocks[j])
        if i > 0:
            nodes[2*j] = 2*i -1
            nodes[2*j +1] = 2*i
        else:
            nodes[2*j] = -2*i
            nodes[2*j +1] = -2*i -1
    return nodes

def EdgeFind(nodes,genome):
    edges = []
    count = 0
    for chr in genome:
        new_nodes = nodes[count:count + 2*len(chr)]
        count += 2*len(chr)
        new_nodes.append(new_nodes[0])
        for i in range(len(new_nodes)//2):
            edges.append((new_nodes[2*i +1], new_nodes[2*i +2]))
    return edges

def Cycle(p_edges,q_edges):
    cycles, cycle, union = [], [p_edges[0][0]], [p_edges,q_edges]
    while len(p_edges) > 0 and len(q_edges) > 0:
        while cycle.count(cycle[-1]) < 2:
            head,tail = cycle[-1], 0
            turn = (cycle.index(head) +1) % 2
            for edge in union[turn]:
                if head in edge:
                    if head == edge[0]:
                        tail = edge[1]
                        union[turn].remove((head,tail))
                    else:
                        tail = edge[0]
                        union[turn].remove((tail,head))
                    break
            cycle.append(tail)
        cycles.append(cycle)
        if len(p_edges) > 0:
            cycle = [p_edges[0][0]]
    return cycles

def TwoBreakDist(p,q):
    p_blocks, q_blocks = sum(Genome(p),[]), sum(Genome(q),[])
    p_nodes, q_nodes = NodeMaker(Genome(p)), NodeMaker(Genome(q))
    p_edges, q_edges = EdgeFind(p_nodes,Genome(p)), EdgeFind(q_nodes,Genome(q))
    return len(p_blocks) - len(Cycle(p_edges,q_edges))



sample_p = '(+1 +2 +3 +4 +5 +6)'
sample_q = '(+1 -3 -6 -5)(+2 -4)'

file = open('C:/Users/anqja/Downloads/rosalind_ba6c (2).txt','r')
lines = file.readlines()
test_p,test_q = lines[0].rstrip('\n'), lines[1].rstrip('\n')
print(TwoBreakDist(test_p,test_q))