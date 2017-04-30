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
