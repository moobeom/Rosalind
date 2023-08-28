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


n,A = getData("C:/Users/anqja/Downloads/rosalind_hea (1).txt")
for i in range(n//2 -1, -1, -1):
    MaxHeapify(A,i,n)
answer = ' '.join([str(num) for num in A])
print(answer)