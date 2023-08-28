### Implement ChromosomeToCycle ###

def ChromosomeToCycle(chromosome):
    chromosome = chromosome.lstrip("(").rstrip(")").split()
    nodes = [0] * (2*len(chromosome))
    for j in range(1, len(chromosome)+1):
        i = int(chromosome[j-1])
        if i > 0:
            nodes[2*j -2] = 2*i -1
            nodes[2*j -1] = 2*i
        else:
            nodes[2*j -2] = -2*i
            nodes[2*j -1] = -2*i -1
    return nodes

sample_chr = '(+1 -2 -3 +4)'
test_chr = '(+1 -2 +3 +4 +5 -6 -7 +8 +9 -10 -11 +12 -13 +14 +15 -16 -17 -18 -19 +20 +21 +22 +23 +24 +25 -26 -27 -28 +29 -30 -31 -32 -33 +34 -35 -36 -37 -38 +39 -40 -41 -42 -43 +44 +45 -46 +47 -48 +49 +50 +51 -52 -53 -54 +55 +56 -57 -58 -59 -60 -61 -62 -63 +64 +65 -66 +67 -68 +69 -70)'

cycles = ChromosomeToCycle(test_chr)
answer = '('
for cycle in cycles:
    answer += str(cycle) + ' '
answer += ')'
print (answer)