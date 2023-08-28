### Partial permutations ###

n,k = 87,8
pper = 1
for i in range(k):
    pper *= n-i
print(pper % 1000000)