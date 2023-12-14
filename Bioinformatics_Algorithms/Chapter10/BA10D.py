### Compute the probability of a string emitted by an HMM ###


def OutcomeLikelihood(x, states, transition, emission):
    def weight(l, k, sym):
        return transition[l][k] * emission[k][sym]

    init_trans_prob = 1 / len(states)
    forward = {}
    for i in range(len(x)):
        for state in states:
            if state not in forward:
                forward[state] = {}
            if i == 0:
                forward[state][i] = 1 * init_trans_prob * emission[state][x[i]]
            else:
                forward[state][i] = sum(
                    forward[prev_state][i - 1] * weight(prev_state, state, x[i]) for prev_state in states)

    prob = sum(forward[state][len(x) - 1] for state in states)
    return prob


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10d.txt').readlines()
    string = lines[0].rstrip()
    symbols, states = [sym.rstrip() for sym in lines[2].split('\t')], [sym.rstrip() for sym in lines[4].split('\t')]
    transition = {}
    for i in range(len(states)):
        probs = lines[7 + i].split('\t')[1:]
        trans = {states[j]: float(probs[j]) for j in range(len(states))}
        transition[states[i]] = trans
    emission = {}
    for i in range(len(states)):
        probs = lines[9 + len(states) + i].split('\t')[1:]
        emis = {symbols[j]: float(probs[j]) for j in range(len(symbols))}
        emission[states[i]] = emis
    print(OutcomeLikelihood(string, states, transition, emission))