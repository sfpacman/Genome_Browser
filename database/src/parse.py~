import re

# read in data from file
with open(chrom_CDS_8.gz, 'r') as f:
	whole_file = f.read().splitlines()
# Gene table lists
#NEED: Gene identifiers, protein product names, Genbank accession, chromosomal location

chrom_loc_list = []
for line in whole_file:
	p = re.compile(r'map=\"(.+?)\s*\"')
	match = p.search(line)
	if match:
 		chrom_loc_list.append(match.group())

accession_list = []
for line in whole_file:
 	p = re.compile(r'ACCESSION(.+?)\s*)
 	match = p.search(line)
 	if match:
		accession_list.append(match.group())

product_list = []
for line in whole_file:
 	p = re.compile(r'product=\"(.+?)\s*\"')
 	match = p.search(line)
 	if match:
		product_list.append(match.group())







#DNA table lists
#NEEDS: DNA sequence per gene, Amino Acid sequence, exon 

#Restriction table list
