### Find a profile-most probable k-mer in a string ###
def PMPK(string,k,profileMatrix):
    l = len(string)
    row = {'A':0, 'C':1, 'G':2, 'T':3}
    pList = []
    for i in range(l-k+1):
        kmer = string[i:i+k]
        probability = 1

        for j in range(k):
            probability *= profileMatrix[row[kmer[j]]][j]
        pList.append(probability)
    m = pList.index(max(pList))
    probable = string[m:m+k]
    return probable

text = 'CCGCTGTACACTCACCGGATAAGTGTAGCGGTACCGACTACCGCCAATCATTTCGCAGCGAGGTGATCGATATTTTAGACCATATAGGGATGGATCGGTTCGGCCAATGCTCACGTTAGCATTTCATGTGAGAACTCTGGTTGAGGAGCAACGGTAAAGGTCGTGGCAAGCTCAGCGTGTGAGGACGCTTACATAATAAT'
k = 6
profileMatrix = [[0.273,0.364,0.242,0.273,0.212,0.424],[0.212,0.182,0.273,0.364,0.242,0.212],[0.273,0.333,0.333,0.121,0.242,0.152],[
0.242,0.121,0.152,0.242,0.303,0.212]]
print(PMPK(text,k,profileMatrix))