### Generate the theoretical spectrum of a cyclic peptide ###

def CycloSpectrum(peptide):
    mwTable = {'G': 57, 'A': 71,'S': 87, 'P': 97,'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

    subpeptides = [peptide]
    for unit in range(1,len(peptide)):
        temp = (peptide*2)[:(len(peptide)+(unit-1))]
        for i in range(len(temp)-unit+1):
            subpeptide = temp[i:i+(unit)]
            subpeptides.append(subpeptide)

    massSpectrum = [0]
    for subpeptide in subpeptides:
        mass = 0
        for i in range(len(subpeptide)):
            mass += mwTable[subpeptide[i]]
        massSpectrum.append(mass)
    return sorted(massSpectrum)

#print(CycloSpectrum(peptide='NQEL'))

answer = ''
for mass in CycloSpectrum(peptide='GVTHRWFQEKNQ'):
    answer += str(mass) + ' '
print(answer[:-1])