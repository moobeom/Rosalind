### Estimate the parameters of an HMM ###


def PseudoNormalize(matrix):
    return [[round(value / sum(row), 3) if sum(row) != 0 else round(1 / len(row), 3) for value in row] for row in matrix]

def HMMParameterEstimate(x,pi,states,symbols):
    state_index = {state:idx for idx,state in enumerate(states)}
    symbol_index = {sym:idx for idx,sym in enumerate(symbols)}

    transition = [[0 for j in range(len(states))] for i in range(len(states))]
    for i in range(len(pi) -1):
        transition[state_index[pi[i]]][state_index[pi[i+1]]] += 1

    emission = [[0 for j in range(len(symbols))] for i in range(len(states))]
    for i in range(len(x)):
        emission[state_index[pi[i]]][symbol_index[x[i]]] += 1
    return PseudoNormalize(transition), PseudoNormalize(emission)


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10h (1).txt').readlines()
    string = lines[0].rstrip()
    symbols = [sym.rstrip() for sym in lines[2].split('\t')]
    path = lines[4].rstrip()
    states = [line.rstrip() for line in lines[6].split('\t')]
    TM, EM = HMMParameterEstimate(string,path,states,symbols)

    print('\t'.join(states))
    for i in range(len(TM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in TM[i]]))
    print('--------')
    print('\t'.join(symbols))
    for i in range(len(EM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in EM[i]]))
