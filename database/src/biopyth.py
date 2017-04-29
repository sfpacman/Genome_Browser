#!/usr/bin/python3
import sys
import Bio
from Bio import GenBank
from Bio import SeqIO

#for the Restriction_Enzyme table
#1st value is the recognition sequence read in 5' and the 2nd value is the recognition sequence read in 3' direction
Enz_name = {'EcoRI':{"GAATTC","CTTAAG"}, 'BamHI':{"GGATCC", "CCTAGG"},'BsuMI':{"CTCGAG", "GAGCTC"}}

#create parser
parser = GenBank.RecordParser()
record = parser.parse(open("chrom_CDS_8"))
#create empty list to put all information into
List = []
#create empty dictionary to insert values from each gene one at a time
Insert = {}
for record in GenBank.parse(open("chrom_CDS_8")):
	Insert['accession'] = record.accession
	Insert['seq'] = record.sequence
	#create flags for genes without information in entry
	has_gene=0
	has_loc=0
	has_pp=0
	has_ex_strt=0
	has_ex_end = 0
	has_aa = 0 
	#create empty lists to allow for multiple entries of exons
	exon_start_list = []
	exon_end_list = []
	for feature in record.features:		
		if feature.key == "gene":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/gene=":
					#cut off the quotation marks
					Insert["gene_name"] =qualifier.value[1:-1]
					has_gene = 1		
		if feature.key == "source":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/map=":
					Insert["chrom_loc"] = qualifier.value[1:-1]
					has_loc = 1
		if feature.key == "CDS":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/product=":
					Insert["protein_product"] = qualifier.value[1:-1] 
					has_pp = 1
				if qualifier.key =="/translation=":
					Insert["AA_seq"] = qualifier.value[1:-1]
					has_aa = 1 				
		if feature.key == "exon":
			locations = feature.location.split("..")
			#split the two locations
			exon_start_list.append(locations[0]) 
			Insert["exon_start"] = exon_start_list
			has_ex_strt =1
			exon_end_list.append(locations[1])
			Insert["exon_end"] = exon_end_list
			has_ex_end =1
	#If values are not included in the entry, put in N/A as the value
	if has_gene ==0:
		Insert["gene_name"] = ("N/A")
	if has_loc ==0:
		Insert["chrom_loc"] = ("N/A")
	if has_pp ==0:
		Insert["protein_product"] = ("N/A")
	if has_ex_strt ==0:
		exon_start_list.append("N/A")
		Insert["exon_start"] = exon_start_list
	if has_ex_end ==0:
		exon_end_list.append("N/A")
		Insert["exon_end"] = exon_end_list
	if has_aa == 0:
		Insert["AA_seq"] = ("N/A")
	#Add gene info to the main list
	List.append(Insert)
	#Clear th information to start again for the next entry
	exon_start_list =[]
	exon_end_list = []
	Insert={}
