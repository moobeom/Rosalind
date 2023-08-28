### Introduction to set operations ###

lines = open("C:/Users/anqja/Downloads/rosalind_seto (1).txt").readlines()
n = int(lines[0].rstrip())
U = {i+1 for i in range(n)}
A = set(int(num.rstrip().rstrip('}')) for num in lines[1].lstrip('{').rstrip('}').split(', '))
B = set(int(num.rstrip().rstrip('}')) for num in lines[2].lstrip('{').rstrip('}').split(', '))
print(A|B)      # union set
print(A&B)      # intersection set
print(A-B)      # difference set of A
print(B-A)      # difference set of B
print({x for x in U if x not in A})     # complement set of A
print({x for x in U if x not in B})     # complement set of B