#!/usr/bin/python3

import sys
import Bio
from Bio import SeqIO

#with open("chrom_CDS_8", "rU") as input_handle, open("chrom_CDS_8.fasta", "w") as output_handle:
    #sequences = SeqIO.parse(input_handle, "genbank")
    #count = SeqIO.write(sequences, output_handle, "fasta")
#print("Converted %i records" % count)

def get_accession(record):
    """"Given a SeqRecord, return the accession number as a string.
    e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "Z78488.1"
    """
    parts = record.id.split("|")
    assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "emb"
    return parts[3]

def get_gene_id(record):
    """"Given a SeqRecord, return the gene ID as a string.
    e.g. "gi|2765613|emb|Z78488.1|PTZ78488" -> "2765613"
    """
    parts = record.id.split("|")
    assert len(parts) == 5 and parts[0] == "gi" and parts[2] == "emb"
    return parts[1]


chrom8_accession_dict = SeqIO.to_dict(SeqIO.parse("chrom_CDS_8.fasta", "fasta"), key_function=get_accession)
chrom8_geneID_dict = SeqIO.to_dict(SeqIO.parse("chrom_CDS_8.fasta", "fasta"), key_function=get_gene_id)





# seqfile 
#filename = 'chrom_CDS_8'
#for seq_record in SeqIO.parse( filename , "genbank"):
    #print(seq_record.id)
    #print(repr(seq_record.seq))
    #print (seq_record.seq)
    #print(len(seq_record))

#import re

# read in data from file
#with open('locusAB371371', 'r') as f:
	#print('hello')
	#whole_file = f.read().splitlines()
	#space_strip = re.sub( '\s+', ' ', whole_file).strip()
	#add_comma = space_strip.replace(' ', ',')
	#print(add_comma)
	
# Gene table lists
#NEED: Gene identifiers, protein product names, Genbank accession, chromosomal location

#chrom_loc_list = []
#for line in whole_file:
	#p = re.compile(r'map=\"(.+?)\s*\"')
	#match = p.search(line)
	#if match:
	#if col[0] == "LOCUS":
 		#chrom_loc_list.append(col[1])

#accession_list = []
#for line in whole_file:
	#col = line.split(" ")
 	#p = re.compile(r'ACCESSION(.+?)\s*)
	#match = p.search(line)
	#if col[0] == "ACCESSION":
		#accession_list.append(col[1])

#product_list = []
#for line in whole_file:
 	#p = re.compile(r'product=\"(.+?)\s*\"')
 	#match = p.search(line)
 	#if match:
		#product_list.append(match.group())




#DNA table lists
#NEEDS: DNA sequence per gene, Amino Acid sequence, exon 

#Restriction table list
