### Implement convolution cyclopeptide sequencing ###
from BA4H import Convolution

def ConvolutionCyclopeptideSequencing(M,N,spectrum):
    conv = Convolution(spectrum)
    aa = [mass for mass in conv if 57 <= mass <= 200]

    frequent_aa = []
    if len(set(aa)) <= M:
        frequent_aa = list(set(aa))
    else:
        masses = set(aa)
        m_dict = {}
        for mass in masses:
            m = aa.count(mass)
            m_dict[mass] = m

        cut = sorted(list(m_dict.values()))[::-1][M]
        for mass in masses:
            if m_dict[mass] >= cut:
                frequent_aa.append(mass)
    return LeaderboardCyclopeptideSequencing(spectrum,N,frequent_aa)

def LeaderboardCyclopeptideSequencing(spectrum,n,aaList):     # expanded amino acids
    leaderboard = {''}
    leaderPeptide = str(0)

    while len(leaderboard) != 0:
        leaderboard = Expand(leaderboard,aaList)
        for peptide in leaderboard.copy():
            if Mass(peptide) == ParentMass(spectrum):
                if Score(peptide, spectrum) > Score(leaderPeptide, spectrum):
                    leaderPeptide = peptide
            elif Mass(peptide) > ParentMass(spectrum):
                leaderboard.remove(peptide)
        leaderboard = Trim(leaderboard, spectrum, n)
    return leaderPeptide

def Mass(peptide):
    mass, peptide = 0, peptide.split('-')
    for aa in peptide:
        mass += int(aa)
    return mass

def ParentMass(spectrum):
    return max(spectrum)

def Expand(candidatePeptides,aaList):
    peptides = []
    for peptide in candidatePeptides:
        for aa in aaList:
            if peptide == '':
                peptides.append(str(aa))
            else:
                peptides.append(peptide+'-'+str(aa))
    return set(peptides)

def Score(peptide, exp_spectrum):
    theo_spectrum = CyclicSpectrum(peptide)

    score, checked = 0, []
    for mass in theo_spectrum:
        if mass not in checked and mass in exp_spectrum:
            m, mm = theo_spectrum.count(mass), exp_spectrum.count(mass)  # m: multiplicity
            score += min(m, mm)
            checked.append(mass)
    return score

def CyclicSpectrum(peptide):
    aaList = peptide.split('-')
    subpeptides = [aaList]
    for unit in range(1,len(aaList)):
        temp = (aaList*2)[:(len(aaList)+unit-1)]
        for i in range(len(temp)-unit+1):
            subpeptides.append(temp[i:i+unit])

    massSpectrum = [0]
    for subpeptide in subpeptides:
        mass = 0
        for aa in subpeptide:
            mass += int(aa)
        massSpectrum.append(mass)
    return sorted(massSpectrum)

def Trim(leaderboard, exp_spectrum, n):
    scores = sorted([Score(peptide, exp_spectrum) for peptide in leaderboard])[::-1]
    trimmed_leaderboard = set()
    if len(scores) <= n:
        trimmed_leaderboard = leaderboard
    else:
        cut = scores[n-1]
        for peptide in leaderboard:
            if Score(peptide, exp_spectrum) >= cut:
                trimmed_leaderboard.add(peptide)
    return trimmed_leaderboard



sample_m = 20
sample_n = 60
sample_spectrum = [57,57,71,99,129,137,170,186,194,208,228,265,285,299,307,323,356,364,394,422,493]
#print(ConvolutionCyclopeptideSequencing(sample_m,sample_n,sample_spectrum))


test_m = 18
test_n = 374
test_spectrum = []
file = open('C:/Users/anqja/Downloads/rosalind_ba4i (2).txt','r')
line = file.readline()
temp = line.split(' ')
for mass in temp:
    test_spectrum.append(int(mass))

print(ConvolutionCyclopeptideSequencing(test_m,test_n,test_spectrum))