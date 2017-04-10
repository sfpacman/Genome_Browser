#!/usr/bin/python3

import sys
import Bio
from Bio import GenBank

#for the gene table
gene_name = []
accession = []
protein_product = []	
chrom_loc = []

#for the Sequence table
seq = []
AA_seq = []

#for the Exon table
exon = []

#for the Restriction_Enzyme table
#1st value is the recognition sequence read in 5' and the 2nd value is the recognition sequence read in 3' direction
Enz_name = {'EcoRI':{"GAATTC","CTTAAG"}, 'BamHI':{"GGATCC", "CCTAGG"},'BsuMI':{"CTCGAG", "GAGCTC"}}

feature = record.features
for record in GenBank.parse(open("chrom_CDS_8")):
    accession.append(record.accession)
    seq.append(record.sequence)
    for feature in record.features:
	   if feature.features == "gene":
    		for qualifier in feature.qualifiers:
			if qualifier.key =="/gene=":
				#cut off the quotation marks
				gene_name = qualifier.value[1:-1]		
    	  if record.features == "source":
		   for qualifier in feature.qualifiers:
	    		if qualifier.key =="/map=":
				     #cut off the quotation marks
				     chrom_loc = qualifier.value[1:-1]
  	 if record.features == "CDS":
		  for qualifiers in feature.qualifers:
			    if qualifier.key =="/product=":
				  protein_product = qualifier.value[1:-1]
			    if qualifier.key =="/translation=": 
				AA_seq = qualifier.value[1:-1]
		
for record in GenBank.parse(open("chrom_CDS_8")):   
     if record.feature == "exon":
	#split the two locations into seperate strings
        locations = feature.location.split("..")
        start = int(locations[0])
        end = int(locations[1]
    
