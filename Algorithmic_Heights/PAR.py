### 2-way partition ###

def getData(filename):
    lines = open(filename).readlines()
    n = lines[0].rstrip()
    A = lines[1].rstrip().split(' ')
    return int(n), [int(num) for num in A]

def Partition(A,p,r):
    i,j = p+1,r-1
    while i < j:
        while A[i] < A[p]:
            i += 1
        while A[j] > A[p]:
            j -= 1
        if i < j:
            A[i],A[j] = A[j],A[i]
    A[p],A[j] = A[j],A[p]
    return A
n,A = getData("C:/Users/anqja/Downloads/rosalind_par.txt")
p = Partition(A,0,n)
answer = ' '.join([str(num) for num in p])
print(answer)