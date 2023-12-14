### Construct a profile HMM ###

def SeedAlignment(alignment,theta):
    cols = []
    for i in range(len(alignment[0])):
        column = [seq[i] for seq in alignment]
        if column.count('-') / len(alignment) < theta:
            cols.append(i)
    return cols

def PathDict(seq,path):
    emission_dict = {}
    i = 0
    for state in path:
        if 'M' in state or 'I' in state:
            while seq[i] == '-':        # skip insertion columns
                i += 1
        if state not in ['S','E']:
            if state in emission_dict:      # insertion loop
                emission_dict[state].append(seq[i])
            else:
                emission_dict[state] = [seq[i]]
            i += 1
    return emission_dict

def normalize(matrix):
    return [[round(value / sum(row), 3) if sum(row) != 0 else 0 for value in row] for row in matrix]

def ProfileHMM(alignment,theta,symbols):
    seed_cols = SeedAlignment(alignment,theta)
    Viterbi_graph, states = {'S':['I0','M1','D1'], 'I0':['I0','M1','D1']}, ['I','M','D']
    for i in range(1, len(seed_cols)+1):
        if i < len(seed_cols):
            for state1 in states:
                Viterbi_graph['{}{}'.format(state1, i)] = ['I{}'.format(i)] + ['{}{}'.format(state2, i+1) for state2 in ['M','D']]
        else:
            for state1 in states:
                Viterbi_graph['{}{}'.format(state1, i)] = ['I{}'.format(i)]

    paths = {seq: ['S'] for seq in alignment}
    unique_alignment = list(set(alignment))
    for i in range(len(unique_alignment[0])):
        for seq in unique_alignment:
            if i in seed_cols:
                if seq[i] != '-':
                    paths[seq].append(Viterbi_graph[paths[seq][-1]][1])  # match
                else:
                    paths[seq].append(Viterbi_graph[paths[seq][-1]][2])  # deletion
            else:
                if seq[i] != '-':
                    paths[seq].append(Viterbi_graph[paths[seq][-1]][0])  # insertion
    for seq in unique_alignment:
        paths[seq].append('E')

    all_states = ['S','I0'] + ['{}{}'.format(state, i+1) for i in range(len(seed_cols)) for state in ['M','D','I']] + ['E']
    index_dict = {state: i for i, state in enumerate(all_states)}
    symbol_dict = {sym: i for i, sym in enumerate(symbols)}
    path_dict = {seq: PathDict(seq,paths[seq]) for seq in unique_alignment}

    transition_matrix = [[0 for j in range(len(all_states))] for i in range(len(all_states))]
    for seq in alignment:
        for i in range(1, len(paths[seq])):
            transition_matrix[index_dict[paths[seq][i-1]]][index_dict[paths[seq][i]]] += 1

    emission_matrix = [[0 for j in range(len(symbols))] for i in range(len(all_states))]
    for seq in alignment:
        for state in path_dict[seq]:
            if 'D' not in state:
                for sym in path_dict[seq][state]:
                    emission_matrix[index_dict[state]][symbol_dict[sym]] += 1
    return normalize(transition_matrix), normalize(emission_matrix), all_states


if __name__ == '__main__':
    lines = open('C:/Users/moveo/Downloads/rosalind_ba10e (4).txt').readlines()
    thres = float(lines[0])
    symbols = [sym.rstrip() for sym in lines[2].split('\t')]
    MSA = [line.rstrip() for line in lines[4:]]
    TM, EM, states = ProfileHMM(MSA,thres,symbols)

    print('\t'.join(states))
    for i in range(len(TM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in TM[i]]))
    print('--------')
    print('\t'.join(symbols))
    for i in range(len(EM)):
        print('{}\t'.format(states[i]) + '\t'.join([str(prob) for prob in EM[i]]))