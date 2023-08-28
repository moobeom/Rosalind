### Wobble bonding and RNA secondary structures ###

MotzDict = {}        # memoization
def MotzkinWobble(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    if seq in MotzDict:
        return MotzDict[seq]

    MotzDict[seq] = MotzkinWobble(seq[1:])
    for i in range(4,len(seq)):
        if (seq[0] == 'A' and seq[i] == 'U') or (seq[0] == 'U' and seq[i] == 'A') or \
                (seq[0] == 'C' and seq[i] == 'G') or (seq[0] == 'G' and seq[i] == 'C') or \
                (seq[0] == 'U' and seq[i] == 'G') or (seq[0] == 'G' and seq[i] == 'U'):
            MotzDict[seq] += MotzkinWobble(seq[1:i]) * MotzkinWobble(seq[i+1:])  # left and right side of base pair between first and i-th base in the sequence
    return MotzDict[seq]

string = 'ACCGGCCGGCCGACUGAACCUUAUUCUCCUGCAAAGCUAAGUGGAUCCUGACGUUGCUUGAUUUUGAAGGAUGAUUUAGCGUUGCAAGCGGGAACUUGCUCAAAGGGCGGCGGUGUUAGUGUCAGGCGUGUGGUCUCGAGGACACAAGUAUCUCGCGUUAUCGUUGCUACCAAUGGACUUAAGU'
print(MotzkinWobble(string))