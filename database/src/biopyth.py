#!/usr/bin/python3
#import pandas as pd
import sys
import Bio
from Bio import GenBank
from Bio import SeqIO
#dataframe = pd.DataFrame(gene_name, accession, protein_product, chrom_loc)
#for the gene table
gene_name = ()
accession = []
protein_product = []	
chrom_loc = []

#for the Sequence table
seq = []
AA_seq = []

#for the Exon table
exon = ()
start = []
end = []

#for the Restriction_Enzyme table
#1st value is the recognition sequence read in 5' and the 2nd value is the recognition sequence read in 3' direction
Enz_name = {'EcoRI':{"GAATTC","CTTAAG"}, 'BamHI':{"GGATCC", "CCTAGG"},'BsuMI':{"CTCGAG", "GAGCTC"}}

unavailable = ("NA")
parser = GenBank.RecordParser()
record = parser.parse(open("chrom_CDS_8"))


for record in GenBank.parse(open("chrom_CDS_8")):
	accession.append(record.accession)
	seq.append(record.sequence)
	for feature in record.features:
		if feature.key == "gene":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/gene=":
					#cut off the quotation marks
					gene_name =  qualifier.value[1:-1]
				#else qualifier.key !="/gene=":
					#gene name += 'NA'		
		if feature.key == "source":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/map=":
					chrom_loc = qualifier.value[1:-1]
		if feature.key == "CDS":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/product=":
					protein_product = qualifier.value[1:-1] 
				if qualifier.key =="/translation=": 
					AA_seq = qualifier.value[1:-1] 
		if feature.key == "exon":
			locations = feature.location.split("..")
			#split the two locations 
			start = (locations[0])
			end = (locations[1])
	
print(gene_name)
    
