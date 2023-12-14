### Perform a multiple sequence alignment with a profile HMM ###
from BA10E import ProfileHMM
from BA10F import TransitionPseudoNormalize, EmissionPseudoNormalize


def Matrix2Dict(matrix,states,symbols=None):
    if symbols is None:
        symbols = states
    return {state: {sym: prob for sym, prob in zip(symbols, row)} for state, row in zip(states[:-1], matrix[:-1])}

# In progress
def ProfileHMMalignment(x,states,transition,emission):
    def HMMweight(l,k,sym):
        return transition[l][k] * emission[k][sym] if 'D' not in k else transition[l][k]

    score = [[0 for j in range(len(x) + 1)] for i in range(len(states[1:-1]))]
    backtrack = {}
    statesIndex = {i:state for i,state in enumerate(states)}

    for j in range(len(x) + 1):
        backtrack[j] = {}
        if j == 0:
            for i in range(2,len(states[1:-1]),3):
                score[i][j] = HMMweight(statesIndex[i-2], statesIndex[i+1], x[j-1])
                backtrack[j][statesIndex[i+1]] = statesIndex[i-2]

        else:
            for i in range(len(states[1:-1])):
                if i % 3 == 0:      # insertion
                    if i == 0:      # I0
                        if j == 1:
                            score[i][j] = score[i][j-1] * HMMweight(statesIndex[i], statesIndex[i+1], x[j-1])   # 'S'
                            backtrack[j][statesIndex[i+1]] = statesIndex[i]
                        else:
                            score[i][j] = score[i][j-1] * HMMweight(statesIndex[i+1], statesIndex[i+1], x[j-1]) # 'I0'
                            backtrack[j][statesIndex[i+1]] = statesIndex[i+1]
                    else:
                        M = score[i-2][j-1] * HMMweight(statesIndex[i-1], statesIndex[i+1], x[j-1])
                        D = score[i-1][j-1] * HMMweight(statesIndex[i], statesIndex[i+1], x[j-1])
                        I = score[i][j-1] * HMMweight(statesIndex[i+1], statesIndex[i+1], x[j-1])
                        score[i][j] = max(M, D, I)
                        if score[i][j] == M:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-1]
                        elif score[i][j] == D:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i]
                        else:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i+1]

                elif i % 3 == 1:    # match
                    if i == 1:      # M1
                        if j == 1:
                            score[i][j] = score[i-1][j-1] * HMMweight(statesIndex[i-1], statesIndex[i+1], x[j-1])   # 'S'
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-1]
                        else:
                            score[i][j] = score[i-1][j-1] * HMMweight(statesIndex[i], statesIndex[i+1],x[j-1])  # 'I0'
                            backtrack[j][statesIndex[i+1]] = statesIndex[i]
                    else:
                        M = score[i-3][j-1] * HMMweight(statesIndex[i-2], statesIndex[i+1], x[j-1])
                        D = score[i-2][j-1] * HMMweight(statesIndex[i-1], statesIndex[i+1], x[j-1])
                        I = score[i-1][j-1] * HMMweight(statesIndex[i], statesIndex[i+1], x[j-1])
                        score[i][j] = max(M, D, I)
                        if score[i][j] == M:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-2]
                        elif score[i][j] == D:
                            backtrack[j][statesIndex[i+1]] =  statesIndex[i-1]
                        else:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i]

                else:               # deletion
                    if i == 2:      # D1
                        score[i][j] = score[i-2][j] * HMMweight(statesIndex[i-1], statesIndex[i+1], x[j-1])
                        backtrack[j][statesIndex[i+1]] = statesIndex[i-1]
                    else:
                        M = score[i-4][j] * HMMweight(statesIndex[i-3], statesIndex[i+1], x[j-1])
                        D = score[i-3][j] * HMMweight(statesIndex[i-2], statesIndex[i+1], x[j-1])
                        I = score[i-2][j] * HMMweight(statesIndex[i-1], statesIndex[i+1], x[j-1])
                        score[i][j] = max(M, D, I)
                        if score[i][j] == M:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-3]
                        elif score[i][j] == D:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-2]
                        else:
                            backtrack[j][statesIndex[i+1]] = statesIndex[i-1]

    backtrack[len(x)+1] = {}
    E_score = max(transition[states[-4]][states[-1]], transition[states[-3]][states[-1]], transition[states[-2]][states[-1]])
    if E_score == transition[states[-4]][states[-1]]:  # M_last
        backtrack[len(x)+1]['E'] = states[-4]
    elif E_score == transition[states[-3]][states[-1]]:  # D_last
        backtrack[len(x)+1]['E'] = states[-3]
    else:       # I_last
        backtrack[len(x)+1]['E'] = states[-2]

    pi = [backtrack[len(x)+1]['E']]
    for i in range(len(x), -1, -1):
        pi.append(backtrack[i][pi[-1]])
    return pi[::-1]

if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10g.txt').readlines()
    string = lines[0].rstrip()
    thres, pseudocount = [float(value) for value in lines[2].split(' ')]
    symbols = [sym.rstrip() for sym in lines[4].split(' ')]
    MSA = [line.rstrip() for line in lines[6:]]
    TM, EM, states = ProfileHMM(MSA,thres,symbols)
    pseudoTM, pseudoEM = TransitionPseudoNormalize(TM,pseudocount), EmissionPseudoNormalize(EM, pseudocount)
    TMdict, EMdict = Matrix2Dict(pseudoTM,states), Matrix2Dict(pseudoEM,states,symbols)
    print(' '.join(ProfileHMMalignment(string,states,TMdict,EMdict)))
