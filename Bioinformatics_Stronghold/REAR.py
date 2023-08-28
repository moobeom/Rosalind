### Reversal distance ###

def getData(filename):
    lines = open(filename).readlines()
    perms = [[[int(num) for num in lines[3*i].rstrip().split(' ')],[int(num) for num in lines[3*i+1].rstrip().split(' ')]] for i in range(len(lines)//3 +1)]
    return perms

def CountBreakpoints(p):
    return sum(abs(p[i] - p[i-1]) != 1 for i in range(1, len(p)))

def FindStrips(p):
    n = len(p)
    upstrips,downstrips = [],[]
    temp = []
    for i in range(n-1):
        if abs(p[i] - p[i+1]) == 1:
            temp.append(p[i])
        else:
            if p[i] == 0:
                upstrips.append([p[i]])
            else:
                if len(temp) > 0:
                    temp.append(p[i])
                    if temp[0] + 1 == temp[1]:
                        upstrips.append(temp)
                    else:
                        downstrips.append(temp)
                else:
                    downstrips.append([p[i]])
                temp = []
    if p[-1] -1 in upstrips[-1]:
        upstrips[-1].append(p[-1])
    else:
        upstrips.append([p[-1]])
    return upstrips,downstrips

def ImprovedBreakpointReversalSort(p,s):
    s_dict = {s[i]: i+1 for i in range(len(s))}     # consider the permutation 's' be the identity permutation
    pp = [s_dict[p[i]] for i in range(len(p))]      # convert the permutation 'p' for transformation into identity permutation
    breakpoints = CountBreakpoints([0]+pp+[len(pp)+1])
    reversal = 0
    while breakpoints > 0:
        n = len(pp)
        pp = [0] + pp + [n+1]
        upstrips,downstrips = FindStrips(pp)
        if len(downstrips) > 0:
            k = min(sum(downstrips,[]))
            l,r = pp.index(k-1), pp.index(k)
            if l > r:
                l, r = r, l
            pp = pp[:l+1] + pp[l+1:r+1][::-1] + pp[r+1:]
        else:
            upstrip = [upstrip for upstrip in upstrips if 0 not in upstrip and n+1 not in upstrip][0]
            l,r = pp.index(upstrip[0]), pp.index(upstrip[-1])
            pp = pp[:l] + pp[l:r+1][::-1] + pp[r+1:]        # transform any increasing strip into decreasing strip
        pp = pp[1:n+1]
        reversal += 1
        breakpoints = CountBreakpoints(pp)
    return reversal

perms = getData("C:/Users/anqja/Downloads/rosalind_rear (2).txt")
reversals = []
for p,s in perms:
    reversals.append(ImprovedBreakpointReversalSort(p,s))
print(' '.join(str(num) for num in reversals))
