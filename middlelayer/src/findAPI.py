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
