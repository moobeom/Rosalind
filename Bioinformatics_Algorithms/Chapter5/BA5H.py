### Find a highest-scoring fitting alignment of two strings ###

def FittingAlign(v,w):
    n,m = len(v),len(w)
    s, backtrack = [[0 for j in range(m+1)] for i in range(n+1)], [["" for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = 0     # no penalty for an opening gap
        backtrack[i][0] = "down"
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] -1
        backtrack[0][j] = "right"
    s_list = [0]        # max top-row score
    for i in range(1, n+1):
        for j in range(1, m+1):
            match = 0
            if v[i-1] == w[j-1]:
                match += 1
            else:
                match += -1
            s[i][j] = max(s[i-1][j] -1, s[i][j-1] -1, s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j] -1:
                backtrack[i][j] = "down"
            elif s[i][j] == s[i][j-1] -1:
                backtrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "diagonal"
        s_list.append(s[i][m])
    max_s = max(s_list)
    v_sink = s_list.index(s_list[-1])
    for i in range(len(s_list)-1,-1,-1):
        if s_list[i] == max_s:
            v_sink = i
    return backtrack,s[v_sink][-1],v_sink

def OutputAlignment(backtrack,v,w,i,j):
    if i == 0 or j == 0:
        return ("","")
    elif backtrack[i][j] == "down":
        return OutputAlignment(backtrack,v,w,i-1,j) + (v[i-1],"-")
    elif backtrack[i][j] == "right":
        return OutputAlignment(backtrack,v,w,i,j-1) + ("-",w[j-1])
    else:
        return OutputAlignment(backtrack,v,w,i-1,j-1) + (v[i-1],w[j-1])

sample_v = 'GTAGGCTTAAGGTTA'
sample_w = 'TAGATA'
backtrack,score,v_sink = FittingAlign(sample_v,sample_w)
print(score)

alignment = OutputAlignment(backtrack,sample_v,sample_w,v_sink,len(sample_w))
aligned_v,aligned_w = "",""
for i in range(len(alignment)//2):
    aligned_v += alignment[2*i]
    aligned_w += alignment[2*i+1]
print(aligned_v)
print(aligned_w)