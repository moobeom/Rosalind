### Implement Leaderboard cyclopeptide sequencing ###

mwTable = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115,
               'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

def LeaderboardCyclopeptideSequencing(spectrum,n):
    leaderboard = {''}
    leaderPeptide = ''

    while len(leaderboard) != 0:
        leaderboard = Expand(leaderboard)
        for peptide in leaderboard.copy():
            if Mass(peptide) == ParentMass(spectrum):
                if Score(peptide,spectrum) > Score(leaderPeptide,spectrum):
                    leaderPeptide = peptide
            elif Mass(peptide) > ParentMass(spectrum):
                leaderboard.remove(peptide)
        leaderboard = Trim(leaderboard,spectrum,n)
    return leaderPeptide


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

def Score(peptide,exp_spectrum):
    theo_spectrum = LinearSpectrum(peptide)

    score, checked = 0, []
    for mass in theo_spectrum:
        if mass not in checked and mass in exp_spectrum:
            m, n = theo_spectrum.count(mass), exp_spectrum.count(mass)  # m: multiplicity
            score += min(m, n)
            checked.append(mass)
    return score

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

def Trim(leaderboard,exp_spectrum,n):
    scores = sorted([Score(peptide,exp_spectrum) for peptide in leaderboard])[::-1]
    trimmed_leaderboard = set()

    if len(scores) <= n:
        trimmed_leaderboard = leaderboard
    else:
        cut = scores[n-1]
        for peptide in leaderboard:
            if Score(peptide,exp_spectrum) >= cut:
                trimmed_leaderboard.add(peptide)
    return trimmed_leaderboard




sample_n = 10
sample_spectrum = [0,71,113,129,147,200,218,260,313,331,347,389,460]


test_n = 330
test_spectrum = []
file = open('C:/Users/anqja/Downloads/rosalind_ba4g.txt','r')
line = file.readline()
temp = line.split(' ')
for mass in temp:
    test_spectrum.append(int(mass))

linearPeptide = LeaderboardCyclopeptideSequencing(test_spectrum,test_n)
mass = ''
for AA in linearPeptide:
    mass += str(mwTable[AA]) + '-'

mass = mass[:-1]
print(mass)