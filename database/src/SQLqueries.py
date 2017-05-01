#!/usr/bin/env python3
import mysql.connector

# Set parameters
dbname   = "biodb"
dbhost   = "hope"
dbuser   = "sc001"     
dbpass   = "xxxxxx"     
port     = 3306

# Create SQL statement to find information for genes queried from webpage

cursor = db.cursor()

for data in cursor:
#For the basic information on the index page
	sql = "Select * FROM Gene WHERE SOURCE = 'INPUT QUERY HERE';"
	nrows  = cursor.execute(sql)

#For the details page
	sql = "Select Gene_name, Chromosome_location, Protein_product, Genbank_Accession, DNA_sequence, Amino_Acid_Sequence FROM Gene, Sequence WHERE SOURCE = 'INPUT QUERY HERE';"
	nrows  = cursor.execute(sql)

#For the Restriction Enzyme
	sql = "Select * FROM Restriction_Enzyme WHERE SOURCE = 'INPUT QUERY HERE';"
	nrows  = cursor.execute(sql)
#For exon boundaries
	sql = "Select * FROM Exon WHERE SOURCE = 'INPUT QUERY HERE';"
