### Implement Baum-Welch learning ###
from BA10J import SoftDecoding


def BaumWelchResponsibility(x, states, transition, emission):
    def weight(l, k, sym):
        return transition[l][k] * emission[k][sym]

    forward, backward, prob_x, node_resp = SoftDecoding(x, states, transition, emission)
    edge_resp = {}
    for i in range(len(x) - 1):
        for state1 in states:
            for state2 in states:
                if (state1, state2) not in edge_resp:
                    edge_resp[(state1, state2)] = {}
                edge_resp[(state1, state2)][i] = forward[state1][i] * weight(state1, state2, x[i + 1]) * \
                                                 backward[state2][i + 1] / prob_x
    return node_resp, edge_resp


def BaumWelchParameterEstimate(x, responsibility, states, symbols):
    node_resp, edge_resp = responsibility
    transition = {}
    for state1 in states:
        transition[state1] = {state2: sum(edge_resp[(state1, state2)][i] for i in range(len(x) - 1)) for state2 in
                              states}
        norm = sum(transition[state1].values())
        transition[state1] = {state2: round(transition[state1][state2] / norm, 3) for state2 in states}

    emission = {}
    for state in states:
        emission[state] = {symbol: sum(node_resp[state][i] if x[i] == symbol else 0 for i in range(len(x))) for symbol
                           in symbols}
        norm = sum(emission[state].values())
        emission[state] = {symbol: round(emission[state][symbol] / norm, 3) for symbol in symbols}
    return transition, emission


def BaumWelchLearning(n, x, transition, emission, states, symbols):
    for i in range(n):
        responsibility = BaumWelchResponsibility(x, states, transition, emission)
        transition, emission = BaumWelchParameterEstimate(x, responsibility, states, symbols)
    return transition, emission


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10k (4).txt').readlines()
    iters = int(lines[0])
    string = lines[2].rstrip()
    symbols = [sym.rstrip() for sym in lines[4].split('\t')]
    states = [line.rstrip() for line in lines[6].split('\t')]
    init_transition = {}
    for i in range(len(states)):
        probs = lines[9 + i].split('\t')[1:]
        row = {states[j]: float(probs[j]) for j in range(len(states))}
        init_transition[states[i]] = row
    init_emission = {}
    for i in range(len(states)):
        probs = lines[11 + len(states) + i].split('\t')[1:]
        row = {symbols[j]: float(probs[j]) for j in range(len(symbols))}
        init_emission[states[i]] = row
    TM, EM = BaumWelchLearning(iters, string, init_transition, init_emission, states, symbols)

    print('\t'.join(states))
    for i in range(len(TM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(TM[states[i]][state2]) for state2 in states]))
    print('--------')
    print('\t'.join(symbols))
    for i in range(len(EM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(EM[states[i]][symbol]) for symbol in symbols]))