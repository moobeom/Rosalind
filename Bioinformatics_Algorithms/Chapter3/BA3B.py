### Reconstruct a string from its genome path ###

def Reconstruct(kmerList):
    n,k = len(kmerList), len(kmerList[0])
    genome = ''

    prefDict,sufDict = {},{}
    for kmer in kmerList:
        prefix,suffix = kmer[:-1],kmer[1:]
        prefDict[prefix], sufDict[suffix] = kmer, kmer

    # finding a starting node
    for prefix in prefDict:
        if prefix not in sufDict:
            genome += prefDict[prefix]

    # assembly k-mers via the genome path
    for i in range(1,n):
        suffix = genome[i:i+k-1]
        genome += prefDict[suffix][-1]
    return genome


file = open('C:/Users/anqja/Downloads/rosalind_ba3b (1).txt','r')
lines = file.readlines()
kmerList = []

for line in lines:
    kmerList.append(line[:-1])

print(Reconstruct(kmerList))