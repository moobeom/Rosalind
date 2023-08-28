### Finding disjoint motifs in a gene ###

def getData(filename):
    lines = open(filename).readlines()
    text = lines[0].rstrip()
    patterns = [line.rstrip() for line in lines[1:]]
    return text, patterns

def isInterwoven(s,t,u):
    i,j,k = 0,0,0
    while i < len(t) and j < len(u):
        if s[k] != t[i] and s[k] != u[j]:
            return 0
        else:
            if s[k] == t[i] and s[k] != u[j]:
                i += 1
            elif s[k] != t[i] and s[k] == u[j]:
                j += 1
            else:
                i += 1
            k += 1
    if i < len(t) and s[k:] == t[i:]:
        return 1
    elif j < len(u) and s[k:] == u[j:]:
        return 1
    else:
        return 0


string, subsequences = getData("C:/Users/anqja/Downloads/rosalind_itwv_sample.txt")
matrix = [[0 for j in range(len(subsequences))] for i in range(len(subsequences))]
for i in range(len(subsequences)):
    for j in range(len(subsequences)):
        if i <= j:
            s,t = subsequences[i], subsequences[j]
            ls,lt = len(s), len(t)
            substrings = [string[k:k+ls+lt] for k in range(len(string)-ls-lt+1)]
            for substring in substrings:
                matrix[i][j] = isInterwoven(substring,s,t)
                if matrix[i][j] == 1:
                    break
        else:
            matrix[i][j] = matrix[j][i]
for row in matrix:
        print(" ".join(map(str,row)))