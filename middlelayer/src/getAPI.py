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

    return;


