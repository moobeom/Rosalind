### Mortal fibonacci rabbits ###

FiboDict = {1:1, 2:1}       # memoization
def MortalFibo(n,m):
    if n in FiboDict:
        return FiboDict[n]
    if 2 < n <= m:
        FiboDict[n] = MortalFibo(n-2,m) + MortalFibo(n-1,m)
    else:
        FiboDict[n] = sum(MortalFibo(n-k-1,m) for k in range(1,m))
    return FiboDict[n]
print(MortalFibo(89,17))