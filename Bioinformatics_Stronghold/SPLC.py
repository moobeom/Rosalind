### RNA splicing ###
from Bio import SeqIO

def getData(filename):
    strings = [str(string.seq) for string in SeqIO.parse(filename,"fasta")]
    return strings

def Transcribe(string):
    return string.replace('T','U')

def Translate(pattern):
    codonTable = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
"UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S",
"CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S","CCC" : "P", "ACC" : "T","GCC" : "A", "UCA" : "S", "CCA" : "P",
"ACA" : "T", "GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N",
"GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "*", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
"UAG" : "*", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C",
"CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "*", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R",
"AGG" : "R", "GGG" : "G"}
    peptide,i = '',0
    while i < len(pattern):
        triplet = pattern[i:i+3]
        peptide += codonTable[triplet]
        i += 3
    if '*' in peptide:
        peptide = peptide[:(peptide.index('*'))]
    return peptide


def Splice(string,introns):
    loclens = {}
    for intron in introns:
        for i in range(len(string)-len(intron)+1):
            if string[i:i+len(intron)] == intron:
                loclens[i] = len(intron)
    exon = ''
    i = 0
    while i < len(string):
        if i not in loclens:
            exon += string[i]
            i += 1
        else:
            i += loclens[i]
    return Translate(Transcribe(exon))

strings = getData("C:/Users/anqja/Downloads/rosalind_splc.txt")
string, introns = strings[0], strings[1:]
print(Splice(string,introns))