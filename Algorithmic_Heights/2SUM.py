### 2SUM ###

def getData(filename):
    lines = open(filename).readlines()
    k, n = lines[0].rstrip().split(' ')
    arrays = []
    for i in range(int(k)):
        arrays.append([int(num) for num in lines[i+1].split(' ')])
    return int(k),int(n),arrays

def TwoSum(n,array):
    s = -1
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i] == -1 * array[j]:
                s = (i,j)
    return s


k,n,A = getData("C:/Users/anqja/Downloads/rosalind_2sum.txt")
for i in range(k):
    answer = TwoSum(n,A[i])
    if type(answer) is tuple:
        answer = '{} {}'.format(answer[0]+1, answer[1]+1)
    else:
        answer = str(answer)
    print(answer)