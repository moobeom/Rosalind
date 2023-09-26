### Find a highest-scoring alignment of two strings ###
import sys
sys.setrecursionlimit(10**7)

BlOSUM62 = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1, 0, 0, -3, -2],
        [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
        [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
        [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
        [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
        [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
        [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
        [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
        [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
        [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
        [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
        [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
        [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
        [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
        [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
        [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
        [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
        [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
        [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]
alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def GlobalAlign(v,w,sigma,scoring_matrix):
    n,m = len(v),len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] - sigma
        backtrack[i][0] = "down"
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] - sigma
        backtrack[0][j] = "right"
    for i in range(1,n+1):
        for j in range(1,m+1):
            score = scoring_matrix[alphabet.index(v[i-1])][alphabet.index(w[j-1])]
            s[i][j] = max(s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + score)
            if s[i][j] == s[i-1][j] - sigma:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1] - sigma:
                backtrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + score:
                backtrack[i][j] = "diagonal"
    return backtrack,s[-1][-1]

def RecursiveOutputAlignment(backtrack,v,w,i,j):
    if i == 0 and j > 0:
        return ("-",w[j-1])
    elif i > 0 and j == 0:
        return (v[i-1],"-")
    elif i == 0 and j == 0:
        return (v[i-1],w[j-1])
    elif backtrack[i][j] == "down":
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return RecursiveOutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

def IterativeOutputAlignment(backtrack,v,w,i,j):
    aligned_v, aligned_w = '', ''
    while i > 0 or j > 0:
        if i > 0 and (j == 0 or backtrack[i][j] == "down"):
            aligned_v += v[i-1]
            aligned_w += "-"
            i -= 1
        elif j > 0 and (i == 0 or backtrack[i][j] == "right"):
            aligned_v += "-"
            aligned_w += w[j-1]
            j -= 1
        else:
            aligned_v += v[i-1]
            aligned_w += w[j-1]
            i -= 1
            j -= 1
    return (aligned_v[::-1],aligned_w[::-1])


if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5e (1).txt').readlines()
    v,w = lines[0].rstrip(), lines[1].rstrip()
    backtrack,score = GlobalAlign(v,w,sigma=5,scoring_matrix=BlOSUM62)
    alignment = IterativeOutputAlignment(backtrack,v,w,len(v),len(w))

    aligned_v,aligned_w = "",""
    for i in range(len(alignment)//2):
        aligned_v += alignment[2*i]
        aligned_w += alignment[2*i+1]
    print(score)
    print(aligned_v)
    print(aligned_w)