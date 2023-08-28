### Implement 2-BreakOnGenomeGraph ###

def TwoBreakOnGenomeGraph(genomeGraph,i,ii,j,jj):
    if (i,ii) in genomeGraph:
        genomeGraph.remove((i,ii))
    else:
        genomeGraph.remove((ii,i))
    if (j,jj) in genomeGraph:
        genomeGraph.remove((j,jj))
    else:
        genomeGraph.remove((jj,j))
    genomeGraph.append((i,j))
    genomeGraph.append((ii,jj))
    return genomeGraph

sample_graph = [(2, 4), (3, 8), (7, 5), (6, 1)]
test_graph = [(2, 4), (3, 6), (5, 7), (8, 10), (9, 12), (11, 13), (14, 16), (15, 17), (18, 19), (20, 21), (22, 24), (23, 25), (26, 27), (28, 29), (30, 31), (32, 34), (33, 35), (36, 37), (38, 39), (40, 42), (41, 43), (44, 45), (46, 48), (47, 50), (49, 52), (51, 54), (53, 55), (56, 58), (57, 59), (60, 62), (61, 63), (64, 66), (65, 67), (68, 70), (69, 71), (72, 74), (73, 75), (76, 77), (78, 79), (80, 81), (82, 83), (84, 86), (85, 87), (88, 89), (90, 91), (92, 93), (94, 95), (96, 98), (97, 100), (99, 101), (102, 104), (103, 106), (105, 108), (107, 109), (110, 111), (112, 114), (113, 116), (115, 118), (117, 120), (119, 122), (121, 124), (123, 125), (126, 127), (128, 1)]
print(TwoBreakOnGenomeGraph(test_graph,15, 17, 14, 16))