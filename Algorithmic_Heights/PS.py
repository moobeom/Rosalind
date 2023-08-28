### Partial sort ###

def getData(filename):
    lines = open(filename).readlines()
    n = int(lines[0].rstrip())
    A = [int(num) for num in lines[1].split()]
    k = int(lines[2].rstrip())
    return n,A,k

def PartialSort(array,k):
    for i in range(k):
        min_idx = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array[:k]

n,A,k = getData("C:/Users/anqja/Downloads/rosalind_ps.txt")
print(' '.join(str(i) for i in PartialSort(A,k)))