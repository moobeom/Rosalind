### Compute the probability of an outcome given a hidden path ###


def OutcomeGivenPathProb(x, pi, emission):
    prob = 1
    for i in range(len(x)):
        prob *= emission[pi[i]][x[i]]
    return prob


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10b (3).txt').readlines()
    string, symbols = lines[0].rstrip(), [sym.rstrip() for sym in lines[2].split('\t')]
    hidden_path, states = lines[4].rstrip(), [sym.rstrip() for sym in lines[6].split('\t')]
    emission = {}
    for i in range(len(states)):
        probs = lines[9+i].split('\t')[1:]
        emis = {symbols[j]:float(probs[j]) for j in range(len(symbols))}
        emission[states[i]] = emis
    print(OutcomeGivenPathProb(string,hidden_path,emission))