### Find all shared k-mers of a pair of strings ###

def SharedKmers(k,v,w):
    v_kmers, w_kmers = [v[i:i+k] for i in range(len(v)-k+1)], [w[j:j+k] for j in range(len(v)-k+1)]
    pairs = []
    for i in range(len(v_kmers)):
        for j in range(len(w_kmers)):
            if v_kmers[i] == w_kmers[j]:
                pairs.append((i,j))
            elif RC(v_kmers[i]) == w_kmers[j]:
                pairs.append((i,j))
    return  pairs

def RC(string):
    basepair = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rc_string = ''
    for base in string:
        rc_string += basepair[base]
    return rc_string[::-1]

sample_v, sample_w = 'AAACTCATC','TTTCAAATC'
file = open('C:/Users/anqja/Downloads/rosalind_ba6e.txt','r')
line = file.readlines()
test_v, test_w = line[1].rstrip(),line[2].rstrip()
results = SharedKmers(17,test_v,test_w)

answer = ''
for result in results:
    answer += str(result) + '\n'
print(answer)