### Interleaving two motifs ###

def SCSPBackTrack(v,w):
    s,backTrack = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)], [["" for j in range(len(w)+1)] for i in range(len(v)+1)]
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match += 1
            s[i][j] = max(s[i-1][j] , s[i][j-1] , s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j]:
                backTrack[i][j] = "down"
            elif s[i][j] == s[i][j-1]:
                backTrack[i][j] = "right"
            elif s[i][j] == s[i-1][j-1] + match:
                backTrack[i][j] = "diagonal"
    return backTrack

def OutputSCSP(backTrack,v,w,i,j):
    if i == 0 and j == 0:
        return ''
    elif i == 0 and j > 0:
        return OutputSCSP(backTrack,v,w,i,j-1) + w[i-1]
    elif i > 0 and j == 0:
        return OutputSCSP(backTrack,v,w,i-1,j) + v[i-1]
    elif backTrack[i][j] == "down":
        return OutputSCSP(backTrack,v,w,i-1,j) + v[i-1]
    elif backTrack[i][j] == "right":
        return OutputSCSP(backTrack,v,w,i,j-1) + w[j-1]
    else:
        return OutputSCSP(backTrack,v,w,i-1,j-1) + v[i-1]

sample_v = 'CCTGGGAAAGTCTAAGGTACCCCACCCGTGTTACCTCACTTGAACTGGAATGATGTCCGCGAAAGAACGCCCCAGCACAGCGTCAGTCTTCGG'
sample_w = 'GATTTCACACCACTTACACGTTGACAGCCTGGTCCGGGTTCATTAGAAAATCATATTGACGGGAGTACAATAGTCTTCGCAAGAAGTCGAACCTGA'
print(OutputSCSP(SCSPBackTrack(sample_v,sample_w),sample_v,sample_w,len(sample_v),len(sample_w)))