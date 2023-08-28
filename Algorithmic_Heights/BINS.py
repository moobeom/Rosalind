### Binary search ###
def getData(filename):
    lines = open(filename).readlines()
    n,m = int(lines[0]), int(lines[1])
    A,B = [int(num) for num in lines[2].rstrip().split(' ')],[int(num) for num in lines[3].rstrip().split(' ')]
    return n,m,A,B

def BinarySearch(sorted_list,x):
    bot = 0
    top = len(sorted_list) -1

    while bot <= top:
        mid = (top + bot) // 2
        if x < sorted_list[mid]:
            top = mid - 1
        elif x > sorted_list[mid]:
            bot = mid + 1
        else:
            return mid
    return -1

n,m,A,keys = getData("C:/Users/anqja/Downloads/rosalind_bins.txt")
answer = ''
for i in range(m):
    if BinarySearch(A,keys[i]) == -1:
        answer += str(BinarySearch(A,keys[i])) + ' '
    else:
        answer += str(BinarySearch(A,keys[i])+1) + ' '
print(answer)