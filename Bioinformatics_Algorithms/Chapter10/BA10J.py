### Solve the soft decoding problem ###


def SoftDecoding(x,states,transition,emission):
    def weight(l,k,sym):
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
                forward[state][i] = sum(forward[prev_state][i-1] * weight(prev_state, state, x[i]) for prev_state in states)

    backward = {}
    for i in range(len(x) -1, -1, -1):
        for state in states:
            if state not in backward:
                backward[state] = {}
            if i == len(x) -1:
                backward[state][i] = 1
            else:
                backward[state][i] = sum(backward[next_state][i+1] * weight(state,next_state,x[i+1]) for next_state in states)

    prob_x = sum(forward[state][len(x) -1] for state in states)
    prob_k_x = {}
    for i in range(len(x)):
        for state in states:
            if state not in prob_k_x:
                prob_k_x[state] = {}
            prob_k_x[state][i] = forward[state][i] * backward[state][i] / prob_x
    return forward, backward, prob_x, prob_k_x    # forward,backward,prob_x are used in Baum-Welch Learning


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10j (1).txt').readlines()
    string = lines[0].rstrip()
    symbols = [sym.rstrip() for sym in lines[2].split('\t')]
    states = [line.rstrip() for line in lines[4].split('\t')]
    transition = {}
    for i in range(len(states)):
        probs = lines[7+i].split('\t')[1:]
        row = {states[j]: float(probs[j]) for j in range(len(states))}
        transition[states[i]] = row
    emission = {}
    for i in range(len(states)):
        probs = lines[9+len(states)+i].split('\t')[1:]
        row = {symbols[j]: float(probs[j]) for j in range(len(symbols))}
        emission[states[i]] = row
    cond_probs = SoftDecoding(string,states,transition,emission)[3]

    print('\t'.join(states))
    for i in range(len(string)):
        print('\t'.join([str(round(cond_probs[state][i], 4)) for state in states]))