### Locating restriction sites ###
from Bio import SeqIO

def ReverseComplement(string):
    basePair = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rc_string = ''
    for symbol in string:
        rc_string += basePair[symbol]
    return rc_string[::-1]

def FindPalindrome(string):
    palindromes = []
    for i in range(4,13):
        for j in range(len(string)-i+1):
            if string[j:j+i] == ReverseComplement(string)[(len(string)-j-i):(len(string)-j)]:
                palindromes.append([j+1,i])
    return palindromes



string = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_revp.txt","fasta").seq)
for answer in sorted(FindPalindrome(string)):
    print(' '.join(str(num) for num in answer))