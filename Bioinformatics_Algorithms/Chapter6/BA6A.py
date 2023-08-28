### Implement GreedySorting ###

# the input permutation should be converted into a string first
def GreedySorting(p):
    p = listed(p)
    # approxReversalDistance = 0
    process = []
    for k in range(1, len(p)+1):
        if k != int(p[k-1]):
            p = K_sorting(p,k)
            # approxReversalDistance += 1
            process.append(p)
            if p[k-1] == '-{}'.format(k):
                p = K_sorting(p,k)
                # approxReversalDistance += 1
                process.append(p)
    return process

def listed(p):
    return p.lstrip("(").rstrip(")").split()

def K_sorting(Plist,k):
    noSignedPlist = [int(e[1:]) for e in Plist]
    r = noSignedPlist.index(k)
    reversed_p = []
    for e in Plist[k-1:r+1][::-1]:
        if int(e) < 0:
            reversed_p.append('+' + str(-1*int(e)))
        else:
            reversed_p.append(str(-1*int(e)))
    return Plist[:k-1] + reversed_p + Plist[r+1:]


sample_P = "(-3 +4 +1 +5 -2)"
test_P = '(+37 -52 -88 -108 +35 +54 -40 -28 +55 -12 -46 +110 -96 +65 -80 -64 +45 -31 +72 -122 +48 -57 -62 +51 -49 -70 -125 -43 +4 +118 -10 +5 -2 -101 +50 +41 +104 +44 +106 +7 -66 -34 +116 +75 -36 -42 +92 +126 -95 -18 +22 +69 +30 -117 -124 +91 +111 +59 +15 -29 +9 -23 +53 +87 +73 -21 +85 -99 -93 -11 -114 +89 -105 +27 -83 -113 +60 -26 +97 -63 +8 -47 +103 +76 +109 -25 +123 +112 +90 +16 -100 +32 +77 +119 -81 +61 -20 +94 +86 +17 +74 +102 -58 +79 -121 -107 +3 -14 -98 +84 -120 +115 -19 +67 +78 -56 -82 +24 -38 +33 +6 +13 +39 +68 -71 +1)'
sorting = GreedySorting(test_P)
answer = ''
for permutation in sorting:
    answer += '(' + ' '.join(permutation)+ ')' + '\n'
print(answer)