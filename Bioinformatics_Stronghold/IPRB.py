### Mendel's first law ###

k,m,n = 30,26,30
t = k + m + n
print(1 - 0.25*(m/t)*((m-1)/(t-1)) - 0.5*(m/t)*(n/(t-1)) - 0.5*(n/t)*(m/(t-1)) - (n/t)*((n-1)/(t-1)))