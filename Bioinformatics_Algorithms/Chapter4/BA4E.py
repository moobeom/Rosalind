### Find a cyclic peptide with theoretical spectrum matching an ideal spectrum ###
from BA4C import CycloSpectrum

mwTable = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
               'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def CyclopeptideSequencing(spectrum):
    candidatePeptides = {''}
    finalPeptides = []
    while len(candidatePeptides) != 0:
        candidatePeptides = Expand(candidatePeptides)
        for peptide in candidatePeptides.copy():
            if Mass(peptide) == ParentMass(spectrum):
                if CycloSpectrum(peptide) == spectrum and peptide not in finalPeptides:
                    finalPeptides.append(peptide)
                candidatePeptides.remove(peptide)
            elif Mass(peptide) not in spectrum:
                candidatePeptides.remove(peptide)
    return finalPeptides

def Mass(peptide):
    mass = 0
    for i in range(len(peptide)):
        mass += mwTable[peptide[i]]
    return mass

def ParentMass(spectrum):
    return max(spectrum)

def Expand(candidatePeptides):
    peptides = []
    for peptide in candidatePeptides:
        for AA in mwTable:
            peptides.append(peptide+AA)
    return set(peptides)

#sample_spectrum = [0,113,128,186,241,299,314,427]


file = open('C:/Users/anqja/Downloads/rosalind_ba4e (2).txt','r')
line = file.readline()
temp = line.split(' ')
test_spectrum = []
for mass in temp:
    test_spectrum.append(int(mass))
cyclopeptides = CyclopeptideSequencing(test_spectrum)
masses = []
for cyclopeptide in cyclopeptides:
    mass = ''
    for AA in cyclopeptide:
        mass += str(mwTable[AA]) + '-'
    masses.append(mass[:-1])
masses = set(masses)

answer = ''
for mass in masses:
    answer += mass + ' '

print(answer[:-1])