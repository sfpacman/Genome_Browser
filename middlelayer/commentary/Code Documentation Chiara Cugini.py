#### Biocomputing II Project: Code documentation
### Chiara Cugini

#Data access routines

#In here there are different functions that I created to access the database.
#The first function just gets the DNA sequence from the database and prints it out. It can be used if only the DNA sequence is needed for the query.

#!/usr/bin/python
import mysql.connector

def get_DNAseq (DNA):
    "Retrieve DNA sequence from the database"
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

    for row in cursor:
        DNA_sequence = DNA[0]

    #close cursor and connection
    cursor.close ()
    connection.close ()
    
    #print findings
    print ( DNA_sequence, " ")

    return;

#The next function retrieves both the amino acid and the DNA sequence. This function can be used if both sequences want to be retrieved at the same time 

def get_AAseq (aa, cDNA):
    "Retrieve amino acid sequence and DNA from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"  

    sql_aa = "SELECT Amino_Acid_Seq, DNA_sequence FROM sc001.Sequence"
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    #prepare cursor
    cursor = connection.cursor()
    #SQL query
    aa_DNA = cursor.execute(sql_aa)

    #retrieve data
    for row in cursor:
        Amino_Acid_Seq = aa_DNA[0]
        DNA_sequence = aa_DNA[1]
    
    #close cursor and connection
    cursor.close ()
    connection.close ()
    
    #print findings
    print ( Amino_Acid_Seq, " ", DNA_sequence, " ")

    return; 
#This function retrieves exon sequence from the database

def get_exon (seq):
    "Retrieve exon position from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"  
    
    # translate front end variables to database variables    

    sql_exon = "SELECT Exon_Start, Exon_End FROM sc001.Exon
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    #prepare cursor
    cursor = connection.cursor()
    #SQL query
    exon_seq = cursor.execute(sql_exon)

    #retrieve data 

    for row in cursor:
        Exon_Start = exon_seq[0]
        Exon_End = exon_seq[1]
       
    #close cursor and connection
    cursor.close ()
    #print findings
    print (Exon_Start, " ", Exon_End, " ")
    return; 

#This function gets the gene details from the database. If the protein product, chromosome location and gene name wants to be retrieved at the same time, this function can be used.

def get_genedetails (gene):
    "Retrieve gene details from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"   

    sql_gene_det = "SELECT Protein_product, Chromosome_location, Gene_name FROM sc001.Gene"
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    # prepare cursor
    cursor = connection.cursor()
    #SQL query
    gene_det = cursor.execute(sql_gene_det)

    for row in cursor:
        Protein_product = gene_det[0]
        Chromosome_location = gene_det[1]
        Gene_name = gene_det[2]
        
    #close cursor and connection
    cursor.close ()
    connection.close ()
    
    #print findings
    print ( Protein_product, " ",  Chromosome_location, " ", Gene_name, " ")

####################

#The function represented below is the function that I created to calculate the codon frequency of a given sequence. Firstly I inserted the all the codons that were present in the sequence in a list and after that counted the frequency for each codon. I inserted all the codon frequencies in a dictionary so it is easier to visualise it and I made sure that if a ZeroDivisionError occur, to just substitute the error with “0” meaning that the frequency for that codon is null.


from collections import defaultdict

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

#I then used this function to calculate the overall frequency of the codons present in the database DNA. I retrieved the sequences from the database, carried out my function and saved all my data in a file so it is easier to retrieve it and the website does not have to carry it out every time that is looking for it

#!/usr/bin/python
#overall codon usage frequency

#get chromosome frequency
#calculate codon usage frequency

#use frequency codon function created previously 

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

###################################################


#Restriction Enzyme Site Finding function
#For locating the restriction enzyme sites of the different enzymes I created three different functions, one for each exam (BamHI, EcoHI and BsuMI). 
#For the function of the restriction enzyme BamHI I have used Biopython and extracted Bio.Restriction form it. I used toheBamHI.search function to find the site of the enzyme in the sequence and then added 4 to the position to show the two sticky ends that the enzyme forms. Both were appended to the list pos.

#!/usr/bin/python
from Bio.Restriction import BamHI
from Bio.Restriction import EcoRI
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
amb = IUPACAmbiguousDNA()

def find_BamHi (DNA_sequence):
    "Find BamHi restriction site and give position of sticky ends"
    pos=[] 
    bam_start= BamHi.search(DNA_sequence)
    for entry in bam_start:
        bam_end = entry + 4
        bam.append(entry)
        pos.append(bam_end)
    return(pos);

#The same thing was done for EcoRI restriction site
def find_EcoRi (DNA_sequence):
    "Find EcoRi restriction site and give position of sticky ends"
    pos=[]
    eco_start= EcoRI.search(DNA_sequence)
    for entry in eco_start:
        eco_end = entry + 4
        pos.append(entry)
        pos.append(eco_end)
    return(pos);

#For BsuMI, instead, I used regular expression to find the restriction site for the enzyme and cut it. I knew that it would give blunt ends instead of sticky therefore only one position of the cut was needed.

import re
def find_BsuMi (DNA_sequence):
    "Find BsuMi restriction site and give position on the cut"
    bsumi = re.search(r"CTCGAG", DNA_sequence)
    #start of the recognition site on the sequence
    bsu_start = bsumi.start()
    #cut of the enzyme on the sequence
    bsu_cut = bsu_start + 3
    return(bsu_cut);

#################################

#Business logic
#Here I have actually created functions that would retrieve different part of the database according to the input from the website. All the functions have the same backbone structure and only the variables for each part retrieved changes.
#The first function reads what type of input was inserted in the website and retrieves GeneBank accession, the name of the gene, the protein product, the chromosome location and the DNA sequence. First of all the variables get translated from the front end to the database end so they can communicate. Then a SQL query is carried out to get the different data and it gets inserted inside a list which then is inserted into a dictionary. 
#The same layout is carried out for: getting Genebank accession, gene name, protein product and chromosome location; the exon start sequence position and end and finally the last function is to retrieve the DNA and amino acid sequence.

#!/usr/bin/python
import mysql.connector



def find_all (gene, types)
    "Retrieve everything from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"
    
    # translate front end variables to database variables
    if types ="ga":
        col = "Genbank_Accession"
    if types = "gid":
        col = "Gene_name"
    if types = "protein":
        col = "Protein_product"
    if types = "cl":
        col = "Chromosome_location"
    if types = "DNA":
        col = "DNA_sequence"

    sql_all = "SELECT DNA_sequence, Protein_product, Chromosome_location, Gene_name, Genbank_Accession FROM sc001.Gene as g join sc001.Sequence as s on s.Gene_Identifier = g.Genbank_Accession WHERE "+ col + "=" + gene +";"
    #open database connection
    connection = mysql.connector.connect (host=hope, user=sc001, db=biodb)
    #prepare cursor
    cursor = connection.cursor()
    #SQL query
    everything= cursor.execute(sql_all)
    
    all_list = []
    for row in cursor:
        DNA_sequence = everything[0]
        Protein_product = everything[1] 
        Chromosome_location = everything[2] 
        Gene_name = everything[3]
        Genbank_Accession = everything[4]
        all_list.append(DNA_sequence)
        all_list.append(Protein_product)
        all_list.append(Chromosome_locatio)
        all_list.append(Gene_name)
        all_list.append(Genbank_Accession)
    
    #insert in a dictionary
    all_dict = {DNA = everything[0], Protein= gene_det[1], location= gene_det[2], id= gene_det[3], ga= gene_det[4]}
    all_list.append(all_dict)

    #close cursor and connection
    cursor.close ()
    connection.close ()

    return(all_list);



def find_summary (gene,types):
    "Retrieve gene details from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########" 
    
    #translate front end variables from the website to database col
    
    if types ="ga":
        col = "Genbank_Accession"
    if types = "gid":
        col = "Gene_name"
    if types = "protein":
        col = "Protein_product"
    if types = "cl":
        col = "Chromosome_location"
        
    sql_summ = "SELECT Protein_product, Chromosome_location, Gene_name, Genbank_Accession FROM sc001.Gene WHERE "+ col + "=" + gene +";" 
    
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    # prepare cursor
    cursor = connection.cursor()
    #SQL query
    gene_det = cursor.execute(sql_summ)
    
    #insert a list of dictionary of gene summary data for cgi to parse on index page
    result_list= []
    for row in cursor:
        Protein_product = gene_det[0]
        Chromosome_location = gene_det[1]
        Gene_name = gene_det[2]
        Genbank_Accession = gene_det[3]
        
    #insert in dictionary
    result_dict= {p_name= gene_det[0], location= gene_det[1], id= gene_det[2], ga= gene_det[3]}
    result_list.append(result_dict)
        
    #close cursor and connection
    cursor.close ()
    connection.close ()

    return (result_list);



def find_exon (gene, types):
    "Retrieve exon position from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"  
    
    # translate front end variables to database variables    
    if types = "es":
        col = "Exon_start"
    if types = "ee":
        col = "Exon_End"

    sql_exon = "SELECT Exon_Start, Exon_End FROM sc001.Exon WHERE "+ col + ""
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    #prepare cursor
    cursor = connection.cursor()
    #SQL query
    exon_seq = cursor.execute(sql_exon)

    #retrieve data and insert it into a list
    exon_list = []
    for row in cursor:
        Exon_Start = exon_seq[0]
        Exon_End = exon_seq[1]
        exon_list.append(Exon_Start)
        exon_list.append(Exon_End)
       
    #close cursor and connection
    cursor.close ()
    connection.close ()
    
    return(exon.list); 
    
    

def find_AAseq (aa, cDNA):
    "Retrieve amino acid sequence and DNA from the database"
    dbname   = "biodb"
    dbhost   = "hope"
    dbuser   = "sc001"   
    dbpass   = "#########"  

    if aa ="DNA":
        col = "DNA_sequence"
    if types = "aa":
        col = "Amino_Acid_Seq"
        
    sql_aa = "SELECT Amino_Acid_Seq, DNA_sequence FROM sc001.Sequence WHERE "+ col + "=" + cDNA +";"
    #open database connection
    connection = myseql.connector.connect (host=hope, user=sc001, db=biodb)
    #prepare cursor
    cursor = connection.cursor()
    #SQL query
    aa_DNA = cursor.execute(sql_aa)

    #retrieve data and insert it into a lsit
    aa_list = []
    for row in cursor:
        Amino_Acid_Seq = aa_DNA[0]
        DNA_sequence = aa_DNA[1]
        aa_list.append(Amino_Acid_Seq)
        aa_list.append(DNA_sequence)
    
    #close cursor and connection
    cursor.close ()
    connection.close ()

    return(aa_list); 



    return;
