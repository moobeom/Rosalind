### Quick sort ###

def getData(filename):
    lines = open(filename).readlines()
    n = lines[0].rstrip()
    A = lines[1].rstrip().split(' ')
    return int(n), [int(num) for num in A]

def Median(A,p,r):
    m = (p + r) // 2
    if A[p] > A[m]:
        A[p], A[m] = A[m], A[p]
    if A[m] > A[r]:
        A[m], A[r] = A[r], A[m]
        if A[p] > A[m]:
            A[p], A[m] = A[m], A[p]
    return A[m]

def Partition3(A,p,r):
    pivot = Median(A,p,r)
    lt, gt = p, r
    i = p
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
    return lt, gt

def QuickSort(A,p,r):
    if p < r:
        lt, gt = Partition3(A,p,r)
        QuickSort(A,p,lt-1)
        QuickSort(A,gt+1,r)

n,A = getData("C:/Users/anqja/Downloads/rosalind_qs (1).txt")
QuickSort(A,0,n-1)
answer = ' '.join([str(num) for num in A])
print(answer)