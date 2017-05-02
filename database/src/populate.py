import mysql.connector
#create parameters
dbname   = "biodb"
dbhost   = "hope"
dbuser   = "sc001"   
dbpass   = "#########"   
port     = 3306	
rest_enz = {'EcoRI':'GAATTC', 'BamHI':'GGATCC','BsuMI':'CTCGAG'}

#assign the database
db = mysql.connector.connect(host="hope" ,port=3306,user="sc001",db="sc001",passwd="#########")

#create a cursor for the database
cursor = db.cursor()
for entry in List:
	"""
	Place all entries in the main list of the parsed records to an assigned value to input into database and import via SQL queries
	"""
	#assign values to the entries in the dictionary
	Genbank_Accession = entry ['accession'][0]
	Gene_name = entry['gene_name']
	Chromosome_location = entry ['chrom_loc']
	Protein_product = entry['protein_product']
	DNA_sequence = entry ['seq']
	Amino_Acid_Sequence = entry['AA_seq']
	Exon_start = entry['exon_start']
	Exon_end = entry['exon_end']

	#import data into the Gene table
	#+chr(39)+ have ASCII characters properly translated between languages
	sqlquery1= "INSERT INTO sc001.Gene (Gene_name, Genbank_Accession, Chromosome_location, Protein_product) VALUES ("+chr(39)+Gene_name+chr(39)+", "+chr(39)+Genbank_Accession+chr(39)+", "+chr(39)+Chromosome_location+chr(39)+", "+chr(39)+Protein_product+chr(39)+") ON DUPLICATE KEY UPDATE Gene_name ="+chr(39)+Gene_name+chr(39)+";"
	nrows=cursor.execute(sqlquery1)	
	db.commit()
	
	#Import data into the sequence table
	sqlquery2= "INSERT INTO sc001.Sequence (DNA_sequence, Amino_Acid_Seq, Gene_Identifier)  VALUES ("+chr(39)+DNA_sequence+chr(39)+", "+chr(39)+Amino_Acid_Sequence+chr(39)+", "+chr(39)+Genbank_Accession+chr(39)+")ON DUPLICATE KEY UPDATE Gene_Identifier ="+chr(39)+Genbank_Accession+chr(39)+";"
	nrows=cursor.execute(sqlquery2)	
	db.commit()
	#Created a loop to insert multiple entries as needed for each gene
	for i in range(len(Exon_start)):
		sqlquery3= "INSERT INTO sc001.Exon (Exon_Start, Exon_End, Sequence_Gene_Identifier) VALUES("+chr(39)+Exon_start[i]+chr(39)+", "+chr(39)+Exon_end[i]+chr(39)+", "+chr(39)+Genbank_Accession+chr(39)+");"
		cursor.execute(sqlquery3)
		db.commit()	
	
#Inserting the restriction enzyme dictionary into the database
for key, value in rest_enz.items():
	sqlquery= "INSERT INTO sc001.Restriction_Enzyme(idRestriction_Enzyme, Recognition_seq) VALUES(" +chr(39)+ key+chr(39) + ","+chr(39) + value +chr(39)+")ON DUPLICATE KEY UPDATE idRestriction_Enzyme ="+chr(39)+key+chr(39)+";"
	nrows= cursor.execute(sqlquery)
	db.commit()
	
