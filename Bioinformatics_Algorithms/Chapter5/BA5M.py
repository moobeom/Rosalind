### Find a highest-scoring multiple sequence alignment ###

def Three_wayAlign(v,w,u,sigma):
    n,m,l = len(v), len(w), len(u)
    s = [[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]
    backtrack = [[["" for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]
    for i in range(1, n+1):
        s[i][0][0] = s[i-1][0][0] - sigma
        backtrack[i][0][0] = "down"
    for j in range(1, m+1):
        s[0][j][0] = s[0][j-1][0] - sigma
        backtrack[0][j][0] = "right"
    for k in range(1, l+1):
        s[0][0][k] = s[0][0][k-1] - sigma
        backtrack[0][0][k] = "forward"
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if v[i-1] == w[j-1] == u[k-1]:
                    match_score = 1
                else:
                    match_score = 0
                s[i][j][k] = max(s[i-1][j][k] - sigma, s[i][j-1][k] - sigma, s[i][j][k-1] - sigma, s[i-1][j-1][k] - sigma,
                                 s[i-1][j][k-1] - sigma, s[i][j-1][k-1] - sigma, s[i-1][j-1][k-1] + match_score)
                if s[i][j][k] == s[i-1][j][k] - sigma:
                    backtrack[i][j][k] = "down"
                elif s[i][j][k] == s[i][j-1][k] - sigma:
                    backtrack[i][j][k] = "right"
                elif s[i][j][k] == s[i][j][k-1] - sigma:
                    backtrack[i][j][k] = "forward"
                elif s[i][j][k] == s[i][j-1][k-1] - sigma:
                    backtrack[i][j][k] = "down-diagonal"
                elif s[i][j][k] == s[i-1][j][k-1] - sigma:
                    backtrack[i][j][k] = "right-diagonal"
                elif s[i][j][k] == s[i-1][j-1][k] - sigma:
                    backtrack[i][j][k] = "forward-diagonal"
                elif s[i][j][k] == s[i-1][j-1][k-1] + match_score:
                    backtrack[i][j][k] = "diagonal"
    return backtrack, s[n][m][l]

def RecursiveOutputTripleAlignment(backtrack,v,w,u,i,j,k):
    if i == 0 and j == 0 and k == 0:
        return ("", "", "")
    elif backtrack[i][j][k] == "down":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i-1, j, k) + (v[i-1], "-", "-")
    elif backtrack[i][j][k] == "right":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i, j-1, k) + ("-", w[j-1], "-")
    elif backtrack[i][j][k] == "forward":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i, j, k-1) + ("-", "-", u[k-1])
    elif backtrack[i][j][k] == "down-diagonal":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i, j-1, k-1) + ("-", w[j-1], u[k-1])
    elif backtrack[i][j][k] == "right-diagonal":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i-1, j, k-1) + (v[i-1], "-", u[k-1])
    elif backtrack[i][j][k] == "forward-diagonal":
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i-1, j-1, k) + (v[i-1], w[j-1], "-")
    else:
        return RecursiveOutputTripleAlignment(backtrack, v, w, u, i-1, j-1, k-1) + (v[i-1], w[j-1], u[k-1])


def IterativeOutputTripleAlignment(backtrack,v,w,u,i,j,k):
    aligned_v, aligned_w, aligned_u = '', '', ''
    while i > 0 or j > 0 or k > 0:
        if backtrack[i][j][k] == "down":
            aligned_v += v[i-1]
            aligned_w += "-"
            aligned_u += "-"
            i -= 1
        elif backtrack[i][j][k] == "right":
            aligned_v += "-"
            aligned_w += w[j-1]
            aligned_u += "-"
            j -= 1
        elif backtrack[i][j][k] == "forward":
            aligned_v += "-"
            aligned_w += "-"
            aligned_u += u[k-1]
            k -= 1
        elif backtrack[i][j][k] == "down-diagonal":
            aligned_v += "-"
            aligned_w += w[j-1]
            aligned_u += u[k-1]
            j -= 1
            k -= 1
        elif backtrack[i][j][k] == "right-diagonal":
            aligned_v += v[i-1]
            aligned_w += "-"
            aligned_u += u[k-1]
            i -= 1
            k -= 1
        elif backtrack[i][j][k] == "forward-diagonal":
            aligned_v += v[i-1]
            aligned_w += w[j-1]
            aligned_u += "-"
            i -= 1
            j -= 1
        else:
            aligned_v += v[i-1]
            aligned_w += w[j-1]
            aligned_u += u[k-1]
            i -= 1
            j -= 1
            k -= 1
    return (aligned_v[::-1], aligned_w[::-1], aligned_u[::-1])


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba5m.txt').readlines()
    v,w,u = lines[0].rstrip(), lines[1].rstrip(), lines[2].rstrip()
    backtrack, score = Three_wayAlign(v,w,u,sigma=0)
    alignment = IterativeOutputTripleAlignment(backtrack,v,w,u,len(v),len(w),len(u))
    aligned_v, aligned_w , aligned_u = "", "", ""
    for i in range(len(alignment) // 3):
        aligned_v += alignment[3*i]
        aligned_w += alignment[3*i+1]
        aligned_u += alignment[3*i+2]
    print(score)
    print(aligned_v)
    print(aligned_w)
    print(aligned_u)