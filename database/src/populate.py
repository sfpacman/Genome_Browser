#!/usr/bin/python3
import mysql.connector

dbname   = "biodb"
dbhost   = "hope"
dbuser   = "sc001"   
dbpass   = "8-wh#daps"   
port     = 3306	
rest_enz = {'EcoRI':'GAATTC', 'BamHI':'GGATCC','BsuMI':'CTCGAG'}

db = mysql.connector.connect(host="hope" ,port=3306, user="sc001",db="sc001",passwd="8-wh#daps")

cursor = db.cursor()
for entry in List:
	Genbank_Accession = entry ['accession']
	Gene_name = entry['gene_name']
	Chromosome_location = entry ['chrom_loc']
	Protein_product = entry['protein_product']
	DNA_sequence = entry ['seq']
	Amino_Acid_Sequence = entry['AA_seq']
	Exon_start = entry['exon_start']
	Exon_end = entry['exon_end']
	
	sqlquery= "INSERT INTO sc001.Gene ('Gene_name', 'Genbank_Accession', 'Chromosome_location', 	 'Protein_product'),VALUES ('gene_name', 'accession', 'chrom_loc', 'protein_product');"
	nrows=cursor.execute(sqlquery)	
	db.commit
	sqlquery= "INSERT INTO sc001.Sequence ('DNA_sequence', 'Amino_Acid_Sequence', 'Gene_Accession'), VALUES ('seq', 'AA_seq', 'accession');"
	nrows=cursor.execute(sqlquery)	
	db.commit
	sqlquery= "INSERT INTO sc001.Exon ('Exon_start', 'Exon_end', 'Gene_Accession'), VALUES('start', 'end', 'gene_name');"
	nrows=cursor.execute(sqlquery)	
	db.commit

for key, value in rest_enz.items():
	sqlquery= "INSERT INTO sc001.Restriction_Enzyme(idRestriction_Enzyme, Recognition_seq) VALUES(" +chr(39)+ key+chr(39) + ","+chr(39) + value +chr(39)+");"
	nrows= cursor.execute(sqlquery)
	db.commit
