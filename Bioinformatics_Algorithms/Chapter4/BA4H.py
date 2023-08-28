### Generate the convolution of a spectrum ###

def Convolution(spectrum):
    conv = [i - j for i in spectrum for j in spectrum if i - j > 0]

    result = []
    for mass in conv:
        if mass not in result:
            m = conv.count(mass)
            for i in range(m):
                result.append(mass)
    return result



sample_spectrum = [0,137,186,323]
#print(Convolution(sample_spectrum))

test_spectrum = []
file = open('C:/Users/anqja/Downloads/rosalind_ba4h.txt','r')
line = file.readline()
temp = line.split(' ')
for mass in temp:
    test_spectrum.append(int(mass))

conv = Convolution(test_spectrum)
answer = ''
for mass in conv:
    answer += str(mass) + ' '
answer = answer[:-1]
print(answer)