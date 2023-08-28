### MergeSort ###

def getData(filename):
    lines = open(filename).readlines()
    n = lines[0].rstrip()
    A = lines[1].rstrip().split(' ')
    return int(n), [int(num) for num in A]

def MergeSort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    listA, listB = MergeSort(array[:mid]), MergeSort(array[mid:])
    return Merge(listA, listB)

def Merge(A,B):
    i = j = 0
    merged = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    merged += A[i:]
    merged += B[j:]
    return merged

n,array = getData("C:/Users/anqja/Downloads/rosalind_ms.txt")
sorted_array = MergeSort(array)
answer = ''
for num in sorted_array:
    answer += str(num) + ' '
print(answer)