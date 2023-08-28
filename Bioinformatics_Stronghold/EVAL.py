### Expected number of restriction site ###

def getData(filename):
    lines = open(filename).readlines()
    n,string,probs = int(lines[0].rstrip()), lines[1].rstrip(), [float(num) for num in lines[2].rstrip().split()]
    return n,string,probs


n,s,A = getData("C:/Users/anqja/Downloads/rosalind_eval.txt")
k,B = n-len(s)+1, []
for i in range(len(A)):
    pGC = {'A': (1-A[i])/2 , 'C': A[i]/2, 'G': A[i]/2, 'T': (1-A[i])/2}
    prob = 1
    for symbol in s:
        prob *= pGC[symbol]
    B.append(prob*k)
print(' '.join([str(prob) for prob in B]))