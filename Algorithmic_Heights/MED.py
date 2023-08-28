### Median ###
from random import choice

def getData(filename):
    lines = open(filename).readlines()
    n = int(lines[0].rstrip())
    A = [int(num) for num in lines[1].split()]
    k = int(lines[2].rstrip())
    return n,A,k

def MedianSort(array):
    if len(array) <= 1:
        return array
    pivot = choice(array)       # to use randomized algorithm in a given statement
    less = [i for i in array if i < pivot]
    equal = [i for i in array if i == pivot]
    greater = [i for i in array if i > pivot]
    return MedianSort(less) + equal + MedianSort(greater)

n,A,k = getData("C:/Users/anqja/Downloads/rosalind_med.txt")
print(MedianSort(A)[k-1])