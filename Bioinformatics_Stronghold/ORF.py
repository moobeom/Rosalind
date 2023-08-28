### Open reading frames ###
from Bio import SeqIO

def Transcribe(string):
    return string.replace('T','U')

def ReverseComplement(string):
    basepair = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    rc_string = ''
    for base in string:
        rc_string += basepair[base]
    return rc_string[::-1]

def FindFrames(string):
    codonTable = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
"UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S",
"CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S","CCC" : "P", "ACC" : "T","GCC" : "A", "UCA" : "S", "CCA" : "P",
"ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N",
"GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
"UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C",
"CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
"AGG" : "R", "GGG" : "G"}
    peptides, i = [], 0
    while i < len(string):
        codon = string[i:i+3]
        if codon == "AUG":
            peptide = ''
            for j in range(i,len(string)-2,3):
                if string[j:j+3] not in ["UAA", "UAG", "UGA"]:
                    peptide += codonTable[string[j:j+3]]
                else:
                    peptides.append(peptide)
                    break
        i += 1
    return peptides

string = str(SeqIO.read("C:/Users/anqja/Downloads/rosalind_orf.txt","fasta").seq)
subpeptides = set(FindFrames(Transcribe(string)) + FindFrames(Transcribe(ReverseComplement(string))))
for subpeptide in subpeptides:
    print(subpeptide)


