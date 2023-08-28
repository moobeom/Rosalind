### Generate the theoretical spectrum of a linear peptide ###

mwTable = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
               'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def LinearSpectrum(peptide):
    subpeptides = [peptide]
    for unit in range(1, len(peptide)):
        for i in range(len(peptide)-unit+1):
            subpeptides.append(peptide[i:i+unit])
    massSpectrum = [0]
    for subpeptide in subpeptides:
        mass = 0
        for i in range(len(subpeptide)):
            mass += mwTable[subpeptide[i]]
        massSpectrum.append(mass)
    return sorted(massSpectrum)

spectra = LinearSpectrum('AIVGYMPSWHNDENENMENFHWAVPFLEGPMIPHLGATV')
print(' '.join(str(spectrum) for spectrum in spectra))