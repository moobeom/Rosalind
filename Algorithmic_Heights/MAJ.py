### Major element ###

def getData(filename):
    lines = open(filename).readlines()
    k,n = lines[0].rstrip().split(' ')
    arrays = []
    for i in range(int(k)):
        arrays.append([int(num) for num in lines[i+1].split(' ')])
    return int(k),int(n),arrays

def MajorFind(n,array):
    E,M = set(array),-1
    for element in E:
        f = array.count(element)
        if f > n/2:
            M = element
    return M


k,n,arrays = getData("C:/Users/anqja/Downloads/rosalind_maj.txt")
answer = ''
for i in range(k):
    answer += str(MajorFind(n,arrays[i])) + ' '
print(answer)