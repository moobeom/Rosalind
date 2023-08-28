### Implement CycleToChromosome ###

def CycleToChromosome(nodes):
    nodes = nodes.lstrip("(").rstrip(")").split()
    chromosome = [''] * (len(nodes)//2)
    for j in range(1,len(nodes)//2 +1):
        if int(nodes[2*j -2]) < int(nodes[2*j -1]):
            chromosome[j-1] = '+' + str(int(nodes[2*j -1])//2)
        else:
            chromosome[j-1] = '-' + str(int(nodes[2*j -2])//2)
    return chromosome

sample_nodes = '(1 2 4 3 6 5 7 8)'
test_nodes = '(2 1 3 4 5 6 7 8 10 9 12 11 13 14 15 16 17 18 19 20 22 21 23 24 26 25 28 27 30 29 31 32 34 33 36 35 38 37 40 39 41 42 44 43 46 45 47 48 50 49 52 51 54 53 55 56 57 58 60 59 61 62 63 64 65 66 68 67 69 70 72 71 74 73 75 76 78 77 79 80 81 82 83 84 86 85 87 88 89 90 92 91 93 94 96 95 97 98 99 100 101 102 103 104 105 106 108 107 110 109 111 112 113 114 116 115 117 118 119 120 121 122 124 123 125 126 128 127 129 130 132 131 134 133)'
chromosomes = CycleToChromosome(test_nodes)
answer = '('
for chr in chromosomes:
    answer += chr + ' '
answer = answer[:-1]
answer += ')'
print(answer)