### Construct the suffix array of a string ###

def SuffixArrayConstruction(text):
    suffices = [(text[i:], i) for i in range(len(text))]
    suffices.sort()
    suffixArray = [suffix[1] for suffix in suffices]
    return suffixArray

if __name__ == '__main__':
    string = open("C:/Users/moveo/Downloads/rosalind_ba9g.txt").readline().rstrip()
    print(', '.join(str(pos) for pos in SuffixArrayConstruction(string)))