#!/usr/bin/python3
import sys
import Bio
from Bio import GenBank
from Bio import SeqIO

#for the Restriction_Enzyme table
#1st value is the recognition sequence read in 5' and the 2nd value is the recognition sequence read in 3' direction
Enz_name = {'EcoRI':{"GAATTC","CTTAAG"}, 'BamHI':{"GGATCC", "CCTAGG"},'BsuMI':{"CTCGAG", "GAGCTC"}}

parser = GenBank.RecordParser()
record = parser.parse(open("chrom_CDS_8"))
List = []
Insert = {}
count =0
for record in GenBank.parse(open("chrom_CDS_8")):
	Insert['accession'] = record.accession
	Insert['seq'] = record.sequence
	has_gene=0
	has_loc=0
	has_pp=0
	has_ex_strt=0
	has_ex_end = 0
	has_aa = 0 
	for feature in record.features:		
		if feature.key == "gene":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/gene=":
					#cut off the quotation marks
					Insert["gene_name"] =qualifier.value[1:-1]
					#gene_name.append(count)
					#count+=1
					has_gene = 1		
		if feature.key == "source":
			for qualifier in feature.qualifiers:
				if qualifier.key =="/map=":
					Insert["chrom_loc"] = qualifier.value[1:-1]
					#chrom_loc.append(count)
					#count+=1
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
			Insert["exon_start"] = (locations[0])
			has_ex_strt =1
			Insert["exon_end"] = (locations[1])
			has_ex_end =1
	if has_gene ==0:
		Insert["gene_name"] = ("N/A")
		count+=1
	if has_loc ==0:
		Insert["chrom_loc"] = ("N/A")
		count+=1
	if has_pp ==0:
		Insert["protein_product"] = ("N/A")
		count+=1
	if has_ex_strt ==0:
		Insert["exon_start"] = ("N/A")
		count+=1
	if has_ex_end ==0:
		Insert["exon_end"] = ("N/A")
		count+=1
	if has_aa == 0:
		Insert["AA_seq"] = "N/A"
	List.append(Insert)
	Insert={}

    
