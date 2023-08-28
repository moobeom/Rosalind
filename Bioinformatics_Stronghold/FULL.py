### Infering peptide from full spectrum ###

mwTable = {'A':71.03711, 'C':103.00919, 'D': 115.02694, 'E':129.04259, 'F':147.06841, 'G': 57.02146, 'H':137.05891,
           'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P':97.05276, 'Q':128.05858,
           'R':156.10111, 'S':87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

def FindAA(current,masses):
    for mass in masses:
        for aa in mwTable:
            if abs(mwTable[aa] - (mass - current)) < 0.001:
                return aa
    return False

lines = open("C:/Users/anqja/Downloads/rosalind_full.txt").readlines()
masses = [float(line) for line in lines]
n = (len(masses) - 3) // 2

peptide = ''
current, BYions = masses[1], masses[2:]
while len(peptide) < n:
    aa = FindAA(current,BYions)
    peptide += aa
    current += mwTable[aa]
    BYions = [mass for mass in BYions if mass - current > 0]
print(peptide)

