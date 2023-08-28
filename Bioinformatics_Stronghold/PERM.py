### Enumerate gene orders ###
from itertools import permutations
n = 5
perms = list(permutations(range(1,n+1)))
print(len(perms))
for perm in perms:
    print(' '.join(str(num) for num in list(perm)))
