### Independent alleles ###
from math import factorial

k, N = 5, 7
p = 0.25    # the prob of which a child has AaBb
n = 2 ** k


prob = 0
for i in range(N,n+1):
    prob += (factorial(n) / (factorial(i) * factorial(n-i))) * (p ** i) * ((1-p) ** (n-i))
print(prob)
