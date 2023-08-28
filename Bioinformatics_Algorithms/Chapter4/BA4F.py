### Compute the score of a cyclic peptide against a spectrum ###
from BA4C import CycloSpectrum

def Score(peptide,exp_spectrum):
    theo_spectrum = CycloSpectrum(peptide)

    score,checked = 0,[]
    for mass in theo_spectrum:
        if mass not in checked and mass in exp_spectrum:
            m,n = theo_spectrum.count(mass),exp_spectrum.count(mass)      # m: multiplicity
            score += min(m,n)
            checked.append(mass)
    return score

sample_peptide = 'NQEL'
sample_spectrum = [0,99,113,114,128,227,257,299,355,356,370,371,484]
#print(Score(sample_peptide,sample_spectrum))


test_peptide = 'NSRQLNWFTTEKIVMMHLTQQNSKISGIQTIEYIDGWMMFHFE'
test_spectrum = []

file = open('C:/Users/anqja/Downloads/rosalind_ba4f (2).txt','r')
line = file.readline()
temp = line.split(' ')
for mass in temp:
    test_spectrum.append(int(mass))
print(Score(test_peptide,test_spectrum))