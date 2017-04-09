import mysql.connector

dbname   = "biodb"
dbhost   = "hope"
dbuser   = "sc001"   
dbpass   = "8-wh#daps"   
port     = 3306	

db=mysql.connector.connect(host="hope", port=3306, user="sc001", db="sc001", passwd="8-wh#daps")
for entry in gene:
	sqlquery= "INSERT INTO sc001.Gene ('Identifier', 'Genbank_Accession', 'Chromosome_location', 	 	'Protein_product'), VALUES('gene_name', 'accession', 'chrom_loc', 'protein_product')
	cursor = db.cursor()
	nrows= cursor.excute(sqlquery)
	db.commit
for entry in Sequence:
	sqlquery= "INSERT INTO sc001.Sequence ('DNA_sequence', 'Amino_Acid_Sequence', 'Gene_Identifier'), VALUES('seq', 'AA_seq', 'gene_name')
	cursor = db.cursor()
	nrows= cursor.excute(sqlquery)
	db.commit
for entry in Exon:
	sqlquery= "INSERT INTO sc001.Exon ('Exon_start', 'Exon_end', 'Gene_Identifier'), VALUES('start', 'end', 'gene_name')
	cursor = db.cursor()
	nrows= cursor.excute(sqlquery)
	db.commit
for entry in Restriction_Enzyme:
	sqlquery= "INSERT INTO sc001.Restriction_Enzyme ('iRestriction_Enzyme', 'Recognition_seq'), VALUES('Enz_name[0]', 'Enz_name[1]')
	cursor = db.cursor()
	nrows= cursor.excute(sqlquery)
	db.commit
