### Implement Viterbi learning ###
from BA10C import Viterbi
from BA10H import HMMParameterEstimate

def Matrix2Dict(matrix,states,symbols=None):
    if symbols is None:
        symbols = states
    dict = {}
    for i in range(len(states)):
        dict[states[i]] = {}
        for j in range(len(symbols)):
            dict[states[i]][symbols[j]] = matrix[i][j]
    return dict

def ViterbiLearning(n,x,states,symbols,transition,emission):
    for i in range(n-1):
        pi = Viterbi(x,states,transition,emission)
        TM, EM = HMMParameterEstimate(x,pi,states,symbols)
        transition, emission = Matrix2Dict(TM,states), Matrix2Dict(EM,states,symbols)
    pi = Viterbi(x, states, transition, emission)
    transition, emission = HMMParameterEstimate(x, pi, states, symbols)
    return transition, emission

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10i (1).txt').readlines()
    iters = int(lines[0])
    string = lines[2].rstrip()
    symbols = [sym.rstrip() for sym in lines[4].split('\t')]
    states = [line.rstrip() for line in lines[6].split('\t')]
    transition = {}
    for i in range(len(states)):
        probs = lines[9+i].split('\t')[1:]
        row = {states[j]: float(probs[j]) for j in range(len(states))}
        transition[states[i]] = row
    emission = {}
    for i in range(len(states)):
        probs = lines[11+len(states)+i].split('\t')[1:]
        row = {symbols[j]: float(probs[j]) for j in range(len(symbols))}
        emission[states[i]] = row
    TM, EM = ViterbiLearning(iters,string,states,symbols,transition,emission)

    print('\t'.join(states))
    for i in range(len(TM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in TM[i]]))
    print('--------')
    print('\t'.join(symbols))
    for i in range(len(EM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in EM[i]]))
