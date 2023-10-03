### Find a highest-scoring overlap alignment of two strings ###

def OverlapAlign(v,w,sigma):
    n, m = len(v), len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = 0
        backtrack[i][0] = "down"
    for j in range(1,m+1):
        s[0][j] = 0
        backtrack[0][j] = "right"
    for i in range(1,n+1):
        for j in range(1,m+1):
            match = 0
            if v[i-1] == w[j-1]:
                match += 1
            else:
                match -= sigma
            s[i][j] = max(s[i-1][j] - sigma, s[i][j-1] - sigma, s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j] - sigma:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1] - sigma:
                backtrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "diagonal"
    s_max, w_sink = max(s[-1]), 0
    for j in range(m-1,-1,-1):
        if s[-1][j] == s_max:
            w_sink = j
            break
    return backtrack,s[-1][w_sink],w_sink

def RecursiveOutputAlignment(backtrack,v,w,i,j):
    if i == 0 or j == 0:
        return ("","")
    elif backtrack[i][j] == "down":
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return RecursiveOutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return RecursiveOutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

def IterativeOutputAlignment(backtrack,v,w,i,j):
    aligned_v, aligned_w = '', ''
    while i > 0 and j > 0:
        if backtrack[i][j] == "down":
            aligned_v += v[i-1]
            aligned_w += "-"
            i -= 1
        elif backtrack[i][j] == "right":
            aligned_v += "-"
            aligned_w += w[j-1]
            j -= 1
        else:
            aligned_v += v[i-1]
            aligned_w += w[j-1]
            i -= 1
            j -= 1
    return (aligned_v[::-1], aligned_w[::-1])

if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5i.txt').readlines()
    v,w = lines[0].rstrip(), lines[1].rstrip()
    backtrack,score,w_sink = OverlapAlign(v,w,sigma=2)
    alignment = IterativeOutputAlignment(backtrack,v,w,len(v),w_sink)

    aligned_v,aligned_w = "",""
    for i in range(len(alignment)//2):
        aligned_v += alignment[2*i]
        aligned_w += alignment[2*i+1]
    print(score)
    print(aligned_v)
    print(aligned_w)