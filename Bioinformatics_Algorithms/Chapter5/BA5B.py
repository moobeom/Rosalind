### Find the length of a longest path in Manhattan-like grid ###

def ManhattanTourist(n,m,down,right):       # n,m = grid size & down,right = weight matrices
    s = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j] + down[i-1][j] , s[i][j-1] + right[i][j-1])
    return s[n][m]

if __name__ == '__main__':
    lines = open('C:/Users/anqja/Downloads/rosalind_ba5b (1).txt').readlines()
    n,m = [int(i) for i in lines[0].split()]
    sep = lines.index('-\n')
    down = [[int(i) for i in lines[row].split(' ')] for row in range(1,sep)]
    right = [[int(i) for i in lines[row].split(' ')] for row in range(sep+1, len(lines))]
    print(ManhattanTourist(n,m,down,right))