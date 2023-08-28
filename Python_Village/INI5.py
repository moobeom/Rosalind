lines = open("C:/Users/anqja/Downloads/rosalind_ini5.txt").readlines()
for i in range(len(lines)//2):
    print(lines[2*i+1].rstrip('\n'))