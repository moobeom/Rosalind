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