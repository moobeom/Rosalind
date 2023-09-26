### Find a higest-scoring local alignment of two strings ###
import sys
sys.setrecursionlimit(10**7)

PAM250 = [[2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3],
          [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0],
          [0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4],
          [0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4],
          [-3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7],
          [1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5],
          [-1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0],
          [-1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1],
          [-1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4],
          [-2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2, 2, -2, -1],
          [-1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2],
          [0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2],
          [1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5],
          [0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4],
          [-2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4],
          [1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3],
          [1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3],
          [0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2],
          [-6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0],
          [-3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10]]
alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def LocalAlign(v,w,sigma,scoring_matrix):
    n,m = len(v),len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = 0
        backtrack[i][0] = "free ride"
    for j in range(1,m+1):
        s[0][j] = 0
        backtrack[0][j] = "free ride"
    for i in range(1,n+1):
        for j in range(1,m+1):
            score = scoring_matrix[alphabet.index(v[i-1])][alphabet.index(w[j-1])]
            s[i][j] = max(0, s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + score)
            if s[i][j] == 0:
                backtrack[i][j] = "free ride"
            elif s[i][j] == s[i-1][j] - sigma:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1] - sigma:
                backtrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + score:
                backtrack[i][j] = "diagonal"

    sink_score= 0
    sink = [0,0]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i][j] > sink_score:
                sink_score = s[i][j]
                sink[0],sink[1] = i,j
    return backtrack,sink_score,sink

def RecursiveOutputAlignment(backtrack,v,w,i,j):
    if backtrack[i][j] == "free ride":
        return ("","")
    elif backtrack[i][j] == "down":
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return RecursiveOutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    elif backtrack[i][j] == "diagonal":
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

def IterativeOutputAlignment(backtrack,v,w,i,j):
    aligned_v, aligned_w = "", ""
    while i > 0 and j > 0:
        if backtrack[i][j] == "free ride":
            break
        elif backtrack[i][j] == "down":
            aligned_v = v[i-1] + aligned_v
            aligned_w = "-" + aligned_w
            i -= 1
        elif backtrack[i][j] == "right":
            aligned_v = "-" + aligned_v
            aligned_w = w[j-1] + aligned_w
            j -= 1
        elif backtrack[i][j] == "diagonal":
            aligned_v = v[i-1] + aligned_v
            aligned_w = w[j-1] + aligned_w
            i -= 1
            j -= 1
    return (aligned_v, aligned_w)


if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5f.txt').readlines()
    v,w = lines[0].rstrip(), lines[1].rstrip()
    backtrack,score,sink = LocalAlign(v,w,sigma=5,scoring_matrix=PAM250)
    alignment = IterativeOutputAlignment(backtrack,v,w,sink[0],sink[1])

    aligned_v,aligned_w = "",""
    for i in range(len(alignment)//2):
        aligned_v += alignment[2*i]
        aligned_w += alignment[2*i+1]
    print(score)
    print(aligned_v)
    print(aligned_w)