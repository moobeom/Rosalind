### Implement the Viterbi algorithm ###


def Viterbi(x, states, transition, emission):
    def weight(l, k, sym):
        return transition[l][k] * emission[k][sym]

    init_trans_prob = 1 / len(states)
    backtrack, s = {}, {}
    for i in range(len(x)):
        backtrack[i] = {}
        for state in states:
            if state not in s:
                s[state] = {}
            if i == 0:
                s[state][i] = 1 * init_trans_prob * emission[state][x[i]]
            else:
                for state in states:
                    s[state][i] = max(s[prev_state][i-1] * weight(prev_state,state,x[i]) for prev_state in states)
                    for prev_state in states:
                        if s[state][i] == s[prev_state][i-1] * weight(prev_state,state,x[i]):
                            backtrack[i][state] = prev_state

    pi = max(s.keys(), key=lambda state: s[state][len(x)-1])
    for i in range(len(x)-1, 0, -1):
        pi += backtrack[i][pi[-1]]
    return pi[::-1]

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10c.txt').readlines()
    string = lines[0].rstrip()
    symbols, states = [sym.rstrip() for sym in lines[2].split('\t')], [sym.rstrip() for sym in lines[4].split('\t')]
    transition = {}
    for i in range(len(states)):
        probs = lines[7+i].split('\t')[1:]
        trans = {states[j]:float(probs[j]) for j in range(len(states))}
        transition[states[i]] = trans
    emission = {}
    for i in range(len(states)):
        probs = lines[9 + len(states) + i].split('\t')[1:]
        emis = {symbols[j]:float(probs[j]) for j in range(len(symbols))}
        emission[states[i]] = emis
    print(Viterbi(string,states,transition,emission))