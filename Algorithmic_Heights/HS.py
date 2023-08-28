### Building a Heap ###

def getData(filename):
    lines = open(filename).readlines()
    n = lines[0].rstrip()
    A = lines[1].rstrip().split(' ')
    return int(n), [int(num) for num in A]

def MaxHeapify(A,i,n):
    l, r, max = 2*i+1, 2*i+2, i
    if l < n and A[l] > A[i]:
        max = l
    if r < n and A[r] > A[max]:
        max = r
    if max != i:
        A[i], A[max] = A[max], A[i]
        MaxHeapify(A,max,n)

def BuildMaxHeap(A,n):
    for i in range(n//2 -1,-1,-1):
        MaxHeapify(A,i,n)

def HeapSort(A):
    n = len(A)
    BuildMaxHeap(A, n)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, 0, i)

n,A = getData("C:/Users/anqja/Downloads/rosalind_hs.txt")
HeapSort(A)
answer = ' '.join([str(num) for num in A])
print(answer)