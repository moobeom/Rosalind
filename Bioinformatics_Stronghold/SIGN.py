### Enumerating oriented gene orderings ###
from itertools import permutations,product

n = 5
perms = list(permutations(range(1,n+1)))
new_perms = []
for perm in perms:
    temp_perms = []
    signs = list(product([-1,1],repeat=n))
    for i in range(len(signs)):
        temp_perm = []
        for j in range(len(perm)):
            temp_perm.append(signs[i][j]*perm[j])
        temp_perms.append(temp_perm)
    new_perms.append(temp_perms)

print(len(sum(new_perms,[])))
for new_perm in new_perms:
    for perm in new_perm:
        print(' '.join(str(num) for num in perm))