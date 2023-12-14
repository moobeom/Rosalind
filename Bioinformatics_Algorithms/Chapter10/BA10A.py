### Compute the probability of a hidden path ###


def HiddenPathProb(pi, transition):
    prob = 0.5
    for i in range(1,len(pi)):
        prob *= transition[pi[i-1]][pi[i]]
    return prob


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10a (1).txt').readlines()
    pi, states = lines[0].rstrip(), [sym.rstrip() for sym in lines[2].split('\t')]
    transition = {}
    for i in range(5,len(lines)):
        probs = lines[i].split('\t')[1:]
        trans = {states[j]:float(probs[j]) for j in range(len(states))}
        transition[states[i-5]] = trans
    print(HiddenPathProb(pi,transition))