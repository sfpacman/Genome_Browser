#!/usr/bin/python
#overall codon usage frequency

#get chromosome frequency
#calculate codon usage frequency

#use frequency codon function created previously 
def get_codon_freq (seq):
    #codonsd
    codons = (('GCT', 'GCC', 'GCA', 'GCG'), ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'), ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'), 
          ('AAA', 'AAG'), ('AAT', 'AAC'), ('GAT', 'GAC'), ('TTT', 'TTC'), ('TGT', 'TGC'), ('CCT', 'CCC', 'CCA', 'CCG'), ('CAA', 'CAG'), 
          ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'), ('GAA', 'GAG'), ('ACT', 'ACC', 'ACA', 'ACG'), ('GGT', 'GGC', 'GGA', 'GGG'), 
          ('CAT', 'CAC'), ('TAT', 'TAC'), ('ATT', 'ATC', 'ATA'), ('GTT', 'GTC', 'GTA', 'GTG'), ('TAA', 'TGA', 'TAG'))


    #separate them into list
    #insert in the list all codons that are present in the sequence
    c_list = []
    for codes in range(0, len(seq), 3):
        c_list.append(seq[codes:codes+3])


    #count codons present in the list
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
    return;


#connect to database
import myseql.connector
from collections import defaultdict

dbname   = "biodb"
dbhost   = "hope"
dbuser   = "sc001"   
dbpass   = "#########"   

sql_DNA = "SELECT DNA_sequence FROM sc001.Sequence"
#open database connection
connection = mysql.connector.connect (host=hope, user=sc001, db=biodb)
#prepare cursor
cursor = connection.cursor()
#SQL query
DNA= cursor.execute(sql_DNA)

# fetch all of the amino acid sequence
data_seq = cursor.fetchall ()

#use frequency codon function to calculate the codon frequency for the DNA sequence
tot_freq = get_codon_freq (data_seq)

#store data in a test file
file = open(“codon_freq_DNA.txt”,”w”)
file.write(tot_freq)
file.close()
