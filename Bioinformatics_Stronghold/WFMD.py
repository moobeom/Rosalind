### The Wright-Fisher model of genetic drift ###
from math import factorial

def Comb(n,r):
    return factorial(n) / (factorial(r) * factorial(n - r))

N,m,g,k = [int(num) for num in '5 9 4 7'.split()]
q = 1 - m / (2*N)
p_arr = [Comb(2*N,i) * q ** i * (1-q) ** (2*N-i) for i in range(1,2*N+1)]

for gen in range(1,g):
    new_p_arr = []
    for i in range(1,2*N+1):
        temp = [Comb(2*N,i) * (n / (2*N)) ** i * (1 - n / (2*N)) ** (2*N - i) for n in range(1, 2*N+1)]
        new_p_arr.append(sum(temp[j] * p_arr[j] for j in range(len(temp))))
    p_arr = new_p_arr
final_p = sum(p_arr[k-1:])
print(final_p)