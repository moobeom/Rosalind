### Find a highest-scoring fitting alignment of two strings ###

def FittingAlign(v,w,sigma):
    n,m = len(v),len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = 0     # no penalty for an opening gap
        backtrack[i][0] = "down"
    for j in range(1,m+1):
        s[0][j] = 0
        backtrack[0][j] = "right"
    s_list = [0]        # max top-row score
    for i in range(1, n+1):
        for j in range(1, m+1):
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
        s_list.append(s[i][m])
    max_s = max(s_list)
    v_sink = s_list.index(max_s)
    return backtrack,max_s,v_sink

def OutputAlignment(backtrack,v,w,i,j):
    if i == 0 or j == 0:
        return ("","")
    elif backtrack[i][j] == "down":
        return OutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return OutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return OutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

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
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5h (1).txt').readlines()
    v,w = lines[0].rstrip(), lines[1].rstrip()
    backtrack,score,v_sink = FittingAlign(v,w,sigma=1)
    alignment = IterativeOutputAlignment(backtrack,v,w,v_sink,len(w))

    aligned_v,aligned_w = "",""
    for i in range(len(alignment)//2):
        aligned_v += alignment[2*i]
        aligned_w += alignment[2*i+1]
    print(score)
    print(aligned_v)
    print(aligned_w)