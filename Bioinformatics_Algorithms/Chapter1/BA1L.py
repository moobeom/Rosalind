### Implement PatternToNumber ###

def PatternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = LastSymbol(pattern)
    prefix = Prefix(pattern)
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def LastSymbol(pattern):
    return pattern[-1]

def Prefix(pattern):
    return pattern[:-1]

def SymbolToNumber(symbol):
    T = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return T[symbol]

print(PatternToNumber('ATATCAATCGTGTTTTCTTTAGTTTT'))