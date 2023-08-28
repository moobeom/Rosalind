### Generate the frequency array of a string ###
import itertools as it
def FrequencyTable(text,k):
    freqMap = dict()
    n = len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1
    return freqMap

text = 'GAAAGCGTATCTAAAAGGAAGAGCTACGTTCCGGTGGTAAGATCCATACTAATCATGTCTAGCACGTGTATTGGTCCATCTCATGTTTCACAGCCAAATTAATCTCTCAATGGATCATGTCCAGTATGACCAGTGACGTAATTTGGCATCCAACAACAATTACCGTCTCAGGAACGCACAACTCGTACATCTGTTTAAATGACTCAGCCGGCGTTGCACACTAGTCAATCATTGATACAACGATGATGTTTCATTAACAGCCTTTGTAAGTACGTACAGATACGGTCGTTAACAAATGTGCCTCTATCACATTATGCAGTGTAACTTGGTGTTTTTAGCATTTGAAACGTGGAAGGGCGTTATGGGCACTCACTGATTAGGACGCTGCGGGCTGGAACGGCGAAGTACCCAGGACTACACGCGTAAAGCAGACAGCGTGCGCTAAGAGATTCCTGGGATTCATACAAGCGATGGATAGTACGCTGGGAACGGGACCTATCACGTACAGTGGTCGGCTAACGGCATGTTGAACATGTGTTGCCGTATACTTTGTGTTGTGACAACTTGTTGTATGCGACGATATAATCATGCGAAGAAGAGAAG'
k = 7
# print(FrequencyTable(text,k))

def RL_FrequencyTable(text,k):
    base = "ACGT"
    kmerList = [''.join(chars) for chars in it.product(*(k*(base,)))]
    freqMap = dict()

    for kmer in kmerList:
        freqMap[kmer] = 0

    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1
    return(freqMap)

ansList = list(RL_FrequencyTable(text,k).values())
answer = ''
for ans in ansList:
    answer += str(ans) + ' '
answer = answer[:-1]
print(answer)