### Independent segregation of chromosomes ###
from math import factorial,log10

n = 47
probs = []
for k in range(1,2*n+1):
    prob = 0
    for i in range(k,2*n+1):
        prob += factorial(2*n) / (factorial(i) * factorial(2*n-i)) * (0.5 ** (2*n))
    probs.append(round(log10(prob),3))

print(' '.join(str(prob) for prob in probs))