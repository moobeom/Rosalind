### Align two strings using affine gap penalties ###
from BA5E import RecursiveOutputAlignment,IterativeOutputAlignment

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

def AffinedAlign(v,w,sigma,epsilon,scoring_matrix):
    n, m = len(v), len(w)
    s_l, s_m, s_u = [[0 for j in range(m+1)] for i in range(n+1)], [[0 for j in range(m+1)] for i in range(n+1)], [[0 for j in range(m+1)] for i in range(n+1)]
    backtrack = [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        if i == 1:
            s_l[i][0] = s_l[i-1][0] - sigma
            s_m[i][0] = s_m[i-1][0] - sigma
        else:
            s_l[i][0] = s_l[i-1][0] - epsilon
            s_m[i][0] = s_m[i-1][0] - epsilon
        backtrack[i][0] = "down"
    for j in range(1, m+1):
        if j == 1:
            s_u[0][j] = s_u[0][j-1] - sigma
            s_m[0][j] = s_m[0][j-1] - sigma
        else:
            s_u[0][j] = s_u[0][j-1] - epsilon
            s_m[0][j] = s_m[0][j-1] - epsilon
        backtrack[0][j] = "right"
    for i in range(1, n+1):
        for j in range(1, m+1):
            match_score = scoring_matrix[alphabet.index(v[i-1])][alphabet.index(w[j-1])]
            s_l[i][j] = max(s_m[i-1][j] - sigma, s_l[i-1][j] - epsilon)
            s_u[i][j] = max(s_m[i][j-1] - sigma, s_u[i][j-1] - epsilon)
            s_m[i][j] = max(s_l[i][j], s_u[i][j], s_m[i-1][j-1] + match_score)
            if s_m[i][j] == s_l[i][j]:
                backtrack[i][j] = "down"
            elif s_m[i][j] == s_u[i][j]:
                backtrack[i][j] = "right"
            elif s_m[i][j] == s_m[i-1][j-1] + match_score:
                backtrack[i][j] = "diagonal"
    return backtrack, s_m[-1][-1]

if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5j_sample.txt').readlines()
    v,w = lines[0].rstrip(), lines[1].rstrip()
    backtrack,score = AffinedAlign(v,w,sigma=11,epsilon=1,scoring_matrix=BlOSUM62)
    alignment = RecursiveOutputAlignment(backtrack,v,w,len(v),len(w))

    aligned_v, aligned_w = "", ""
    for i in range(len(alignment) // 2):
        aligned_v += alignment[2*i]
        aligned_w += alignment[2*i+1]
    print(score)
    print(aligned_v)
    print(aligned_w)