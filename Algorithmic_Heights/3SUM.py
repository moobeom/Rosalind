### 3SUM ###

def getData(filename):
    lines = open(filename).readlines()
    k, n = lines[0].rstrip().split(' ')
    arrays = []
    for i in range(int(k)):
        arrays.append([int(num) for num in lines[i+1].split(' ')])
    return int(k),int(n),arrays

def ThreeSum(array,i):
    HashTable = {}
    for j in range(len(array)):
        if i < j:
            if -1*(array[i] + array[j]) not in HashTable:
                HashTable[array[j]] = j
            else:
                return (i,HashTable[-1*(array[i]+array[j])],j)
    return -1


k,n,A = getData("C:/Users/anqja/Downloads/rosalind_3sum.txt")
for i in range(k):
    temp = []
    for j in range(n):
        answer = ThreeSum(A[i],j)
        if type(answer) is tuple:
            answer = '{} {} {}'.format(str(answer[0]+1),str(answer[1]+1),str(answer[2]+1))
            print(answer)
            break
        else:
            temp.append(answer)
    if sum(temp) == -1 * n:
        print(-1)