from collections import defaultdict

seq = "AAAAAAGCC"


#codonsd
codons = (('GCU', 'GCC', 'GCA', 'GCG'), ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'), ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'), ('AAA', 'AAG'), ('AAU', 'AAC'), ('GAU', 'GAC'), ('UUU', 'UUC'), ('UGU', 'UGC'), ('CCU', 'CCC', 'CCA', 'CCG'), ('CAA', 'CAG'), ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'), ('GAA', 'GAG'), ('ACU', 'ACC', 'ACA', 'ACG'), ('GGU', 'GGC', 'GGA', 'GGG'), ('CAU', 'CAC'), ('UAU', 'UAC'), ('AUU', 'AUC', 'AUA'), ('GUU', 'GUC', 'GUA', 'GUG'), ('UAA', 'UGA', 'UAG'))


#separate them into list
#insert in the list all codons that are present in the sequence
c_list = []
for codes in range(0, len(seq), 3):
    c_list.append(seq[codes:codes+3])


#count codons present in the list
count = defaultdict(int)
for codon in c_list:
    count[codon] += 1

    
    ________________________________________________________________
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
