from Bio import motifs



record = motifs.parse("C:/Users/anqja/Downloads/rosalind_meme_result.txt","meme")       # XML format MEME file
motif = record[0].instances
regex = ''


for i in range(len(motif[0])):
    symbols = set(motif[j][i] for j in range(len(motif)))
    if len(symbols) > 1:
            regex += '[' + ''.join(symbols) + ']'
    else:
        regex += list(symbols)[0]
print(regex)