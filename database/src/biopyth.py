#!/usr/bin/python3

import sys
import Bio
from Bio import SeqIO
from Bio import GenBank

Enz_name = {'EcoRI':{"GAATTC","CTTAAG"}, 'BamHI':{"GGATCC", "CCTAGG"},'BsuMI':{"CTCGAG", "GAGCTC"}}

seq = []
AA_seq = []
exon = []
locus = []
features = []
accession = []
protein_product = []	
chrom_loc = []
for record in GenBank.parse(open("chrom_CDS_8")):
    locus.append(record.locus)
    AA_seq.append(record.sequence)
    accession.append(record.accession)
    seq.append(record.sequence)
    for feature in record.features:
	  if feature.key == "gene":
    		for qualifier in feature.qualifiers:
		if qualifier.key =="/gene=":
				gene_name = qualifier.value[1:-1]		
    if record.features == "source"
		   for qualifier in feature.qualifiers:
	    		if qualifier.key =="/map=":
				     chrom_loc = qualifier.value[1:-1]
  	if record.features == "CDS"
		  for qualifiers in feature.qualifers:
			    if qualifier.key =="/product="
				  protein_product = qualifier.value[1:-1]
		
for record in GenBank.parse(open("chrom_CDS_8")):   
     if record.feature == "exon":
        locations = feature.location.split("..")
        start = int(locations[0])
        end = int(locations[1]
    
