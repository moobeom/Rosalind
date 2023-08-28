### Counting point mutations ###

def getData(filename):
    lines = open(filename).readlines()
    return [string.rstrip() for string in lines]

def HammingDistance(p,q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

strings = getData("C:/Users/anqja/Downloads/rosalind_hamm.txt")
print(HammingDistance(strings[0],strings[1]))