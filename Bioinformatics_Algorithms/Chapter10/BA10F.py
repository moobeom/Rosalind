### Construct a profile HMM with pseudocounts ###
from BA10E import ProfileHMM

def TransitionPseudoNormalize(transition,sigma):
    for i in range(len(transition) -1):     # except 'E' state in rows
        row = transition[i]
        for j in range(3 if i < (len(row) -4) else 2):       # except 'E' state in columns
            row[3 * ((i+1) // 3) + (j+1)] += sigma
        transition[i] = [round(value / sum(row), 3) for value in row]
    return transition

def EmissionPseudoNormalize(emission,sigma):
    for i in range(1, len(emission)-1):     # except 'S' and 'E' state in rows
        if i % 3 != 0:      # except 'D' state in rows
            row = [value + sigma for value in emission[i]]
            emission[i] = [round(value / sum(row), 3) for value in row]
    return emission

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10f (2).txt').readlines()
    thres, pseudocount = [float(value) for value in lines[0].split('\t')]
    symbols = [sym.rstrip() for sym in lines[2].split('\t')]
    MSA = [line.rstrip() for line in lines[4:]]
    TM, EM, states = ProfileHMM(MSA,thres,symbols)
    pseudoTM, pseudoEM = TransitionPseudoNormalize(TM,pseudocount), EmissionPseudoNormalize(EM, pseudocount)

    print('\t'.join(states))
    for i in range(len(TM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in pseudoTM[i]]))
    print('--------')
    print('\t'.join(symbols))
    for i in range(len(EM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in pseudoEM[i]]))