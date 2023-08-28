### Construct the de Bruijn graph of a collection of k-mers ###
from BA3D import Gluing

def DeBruijn(patterns):
    comp = Composition(patterns)
    deBruijn = Gluing(comp)
    return deBruijn



def Composition(patterns):
    presuffixList = []
    for pattern in patterns:
        presuffixList.append((pattern[:-1],pattern[1:]))
    return sorted(presuffixList)



file = open('C:/Users/anqja/Downloads/rosalind_ba3e.txt','r')
lines = file.readlines()
kmerList = []
for line in lines:
    kmerList.append(line[:-1])

#patterns = ['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']
pairs = DeBruijn(kmerList)

answer = ''
for pair in pairs:
    answer += '{} '.format(pair[0]) + '-> ' + '{}\n'.format(','.join(pair[1]))
answer = answer[:-1]
print(answer)