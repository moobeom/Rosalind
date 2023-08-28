### Construct the overlap graph of a collection of k-mer ###

def Overlap(kmerList):
    n, k = len(kmerList), len(kmerList[0])
    genome = ''

    prefDict, sufDict = {}, {}
    for kmer in kmerList:
        prefix, suffix = kmer[:-1], kmer[1:]
        prefDict[prefix], sufDict[suffix] = kmer, kmer

    graph = []
    for suffix in sufDict:
        if suffix in prefDict:
            graph.append((sufDict[suffix],prefDict[suffix]))

    return sorted(graph)

# kmerList = ['ATGCG','GCATG','CATGC','CATGC','AGGCA','GGCAT']

file = open('C:/Users/anqja/Downloads/rosalind_ba3c.txt','r')
lines = file.readlines()
kmerList = []

for line in lines:
    kmerList.append(line[:-1])


pairs = Overlap(kmerList)

answer = ''
for pair in pairs:
    answer += '{} '.format(pair[0]) + '-> ' + '{}\n'.format(pair[1])
answer = answer[:-1]

print(answer)