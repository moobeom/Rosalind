### Find the length of a longest path in Manhattan-like grid ###

def ManhattanTourist(n,m,down,right):       # n,m = grid size & down,right = weight matrices
    s = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i][j] = max(s[i-1][j] + down[i-1][j] , s[i][j-1] + right[i][j-1])
    return s[n][m]

sample_n = 4
sample_m = 4
sample_down = [[1,0,2,4,3],
[4,6,5,2,1],
[4,4,5,2,1],
[5,6,8,5,3]]
sample_right = [[3,2,4,0],
[3,2,4,2],
[0,7,3,3],
[3,3,0,2],
[1,3,2,2]]
#print(ManhattanTourist(sample_n,sample_m,sample_down,sample_right))

test_n = 12
test_m = 12
file = open('C:/Users/anqja/Downloads/rosalind_ba5b (2).txt','r')
lines =file.readlines()
split = lines.index('-\n')
down = [lines[i].rstrip().split(' ') for i in range(split)]
test_down = [[int(element) for element in row] for row in down]
right = [lines[i].rstrip().split(' ') for i in range(split+1,len(lines))]
test_right = [[int(element) for element in row] for row in right]
print(ManhattanTourist(test_n,test_m,test_down,test_right))