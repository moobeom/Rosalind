### Construct the partial suffix array of a string ###
from BA9G import SuffixArrayConstruction

def PartialSuffixArray(text,k):
    suffixArray = SuffixArrayConstruction(text)
    return {i: idx for i,idx in enumerate(suffixArray) if idx % k == 0}

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba9q.txt').readlines()
    string, k = lines[0].rstrip(), int(lines[1])
    answers = PartialSuffixArray(string,k)
    for ans in answers:
        print('{},{}'.format(ans,answers[ans]))