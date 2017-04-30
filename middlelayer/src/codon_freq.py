from collections import defaultdictDict 

#codon list 
#include TAA, TAG, TGA stop codons

codons = ("TTC", "TTT", "TTA", "TTG", "CTT", "CTC", "CTA", "CTG", "ATT", "ATC", "ATA", "ATG", "GTT", "GTC", "GTA", "GTG", "TCT", "TCC", "TCA", "TCG", "CCT", "CCC", "CCA", "CCG", "ACT", "ACC", "ACA", "ACG", "GCT", "GCC", "GCA", "GCG", "TAT", "TAC", "TAA", "TAG", "CAT", "CAC", "CAA", "CAG", "AAT", "AAC", "AAA", "AAG", "GAT", "GAC", "GAA", "GAG", "TGT", "TGC", "TGA", "TGG", "CGT", "CGC", "CGA", "CGG", "AGT", "AGC", "AGA", "AGG", "GGT", "GGC", "GGA", "GGG")
seq = "GATGACCGTACGTGACGGCTAACCTGTGAGACGTGACGCGTGAGACGCTAGCTATCGTTAACGTAGC"

dic = {}
for x in codons:
    for codon in x:
        dic[codon] = x

#add number to each
#seq is the cDNA

for n in range(0, len(seq), 3):
    query = seq(n=n+3)

#count how many
count=defaultdict(list)
total = 0

for codon in query:
    total += counts[codon]


#calculate frequencies

freq = {}
for codon in query:
    if codon in dic:
        tot = sum(counts[y] for y in dic[codon])
        frequency = float(counts[codon]) / tot
    else:
        frequency = 0.00

    freq[codon] = frequency

#print

for codon, frequency in freq.iteritems():
    print (codon, frequency)
    
    
    
    
    ---------------------
    
from collections import defaultdict

seq = "AAAAAA"


#codonsd
codons = (('GCU', 'GCC', 'GCA', 'GCG'),
          ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'),
          ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
          ('AAA', 'AAG'), ('AAU', 'AAC'), ('GAU', 'GAC'),
          ('UUU', 'UUC'), ('UGU', 'UGC'), ('CCU', 'CCC', 'CCA', 'CCG'),
          ('CAA', 'CAG'), ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'),
          ('GAA', 'GAG'), ('ACU', 'ACC', 'ACA', 'ACG'),
          ('GGU', 'GGC', 'GGA', 'GGG'), ('CAU', 'CAC'), ('UAU', 'UAC'),
          ('AUU', 'AUC', 'AUA'), ('GUU', 'GUC', 'GUA', 'GUG'),
          ('UAA', 'UGA', 'UAG'))


#separate them into list
#get different start ORFs
c_list = []
for codes in range(0, len(seq), 3):
    c_list.append(seq[codes:codes+3])

#count codons
#always integer
count = defaultdict(int)
for codon in c_list:
    count[codon] += 1

#calculate frequencies
#create dictionary for freqs

frequency = {}
for aaa in codons:
    total = float(sum(count[codon] for codon in aaa))
    for codon in aaa:
        try:
            frequency[codon] = count[codon] / total
        except ZeroDivisionError:
            frequency[codon] = 0

print(frequency)

    
