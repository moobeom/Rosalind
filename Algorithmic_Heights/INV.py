### Counting inversions ###

def getData(filename):
    lines = open(filename).readlines()
    n = int(lines[0].rstrip())
    A = [int(i) for i in lines[1].split()]
    return n,A

def MergeCountInv(arr):
    if len(arr) == 1:
        return arr,0
    A, invA = MergeCountInv(arr[:len(arr)//2])
    B, invB = MergeCountInv(arr[len(arr)//2:])
    M, invM = MergeSort(A,B)
    return M, invA + invB + invM

def MergeSort(A,B):
    i = j = 0
    merged = []
    inv = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
            inv += (len(A)-i)
    merged += A[i:]
    merged += B[j:]
    return merged, inv

n,A = getData("C:/Users/anqja/Downloads/rosalind_inv.txt")
print(MergeCountInv(A))