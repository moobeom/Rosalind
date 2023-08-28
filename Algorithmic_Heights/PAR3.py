### 3-way partition ###

def getData(filename):
    lines = open(filename).readlines()
    n = lines[0].rstrip()
    A = lines[1].rstrip().split(' ')
    return int(n), [int(num) for num in A]

def Partition3(A,p,r):
    pivot = A[p]
    lt, gt = p, r-1
    i = p+1
    while i <= gt:
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
    return A

def QuickSort3(A,p,r):
    if p < r:
        lt, gt = Partition3(A, p, r)
        QuickSort3(A,p,lt)
        QuickSort3(A,gt+1,r)

n,A = getData("C:/Users/anqja/Downloads/rosalind_par3 (3).txt")
p = Partition3(A,0,n)
answer = ' '.join([str(num) for num in p])
print(answer)