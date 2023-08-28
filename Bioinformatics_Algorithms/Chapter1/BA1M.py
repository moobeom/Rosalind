### Implement NumberToPattern ###

def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    prefixIndex = Quotient(index,4)
    r = Remainder(index,4)
    symbol = NumberToSymbol(r)
    PrefixPattern = NumberToPattern(prefixIndex,k-1)
    return  PrefixPattern + symbol

def NumberToSymbol(index):
    T_i = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    return T_i[index]

def Quotient(n,m):
    return n // m

def Remainder(n,m):
    return n % m

print(NumberToPattern(7136,7))
