### Maximal matchings and RNA secondary structures ###
from math import factorial

def Permutation(n,r):
    return int(factorial(n)/ factorial(n-r))

string = 'UCGAGGUGACUCAAGGACAUUAAAGGAGGCGCAAACUUGCUGUGUCCAACGUAGGCAGUUUACGAAGUUGCUCGCUUACGAUU'
countDict = {symbol : string.count(symbol) for symbol in string}
max_matchings = Permutation(max(countDict['A'],countDict['U']),min(countDict['A'],countDict['U']))
max_matchings *= Permutation(max(countDict['C'],countDict['G']),min(countDict['C'],countDict['G']))
print(max_matchings)