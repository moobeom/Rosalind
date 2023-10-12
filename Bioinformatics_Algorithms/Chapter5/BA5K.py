### Find a middle edge in an alignment graph in linear space ###

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


def MiddleEdge(v, w, top, bottom, left, right, sigma=None, scoring_matrix=None):
    mid = (left + right) // 2
    n, m = bottom - top, right - left

    FromSource = [0] * (n+1)
    for j in range(1,mid+1):
        s = [0] * (n+1)
        for i in range(1,n+1):
            match_score = scoring_matrix[alphabet.index(v[i-1])][alphabet.index(w[j-1])]
            s[i] = max(s[i-1] - sigma, FromSource[i] - sigma, FromSource[i-1] + match_score)
        FromSource = s

    ToSink = [0] * (n+1)
    for j in range(1,mid+1):
        s = [0] * (n+1)
        for i in range(n-1,-1,-1):
            match_score = scoring_matrix[alphabet.index(v[i-1])][alphabet.index(w[j-1])]
            s[i] = max(s[i+1] - sigma, ToSink[i] - sigma, ToSink[i+1] + match_score)
        ToSink = s

    Length = [FromSource[i] + ToSink[i] for i in range(n+1)]
    midNode = (Length.index(max(Length)),mid)
    match_score = scoring_matrix[alphabet.index(v[midNode[0]])][alphabet.index(w[midNode[1]])]
    s = max(Length[midNode[0]+1], Length[midNode[0]] - sigma, Length[midNode[0]] + match_score)
    if s == Length[midNode[0]+1]:
        x,y = midNode[0] + 1, mid
    elif s == Length[midNode[0]] - sigma:
        x,y = Length[midNode[0]], mid + 1
    else:
        x,y = midNode[0] + 1, mid + 1
    return midNode,(x,y)

if __name__ =='__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba5k_sample.txt').readlines()
    v, w = lines[0].rstrip(), lines[1].rstrip()
    start,end = MiddleEdge(v,w,0,len(v),0,len(w),sigma=5,scoring_matrix=BlOSUM62)
    print('{} {}'.format(start, end))

