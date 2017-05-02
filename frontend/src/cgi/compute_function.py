#!/usr/bin/python3
'''
Script developed by Pak Hin Yu 
'''
import jinja2
from collections import OrderedDict 

def markup(seq,pos_list,tag,encapsulate=False):
	'''Adding html markup tag for both end to the seq based on the posistion from pos_list
	   seq + pos_list +tag -> string  
	   '''
	if encapsulate:
		assert len(pos_list)%2 == 0,"missing position information"
		end_tag = tag[:1]+"/"+tag[1:]
	else:
		end_tag=tag
	tag_list=[tag,end_tag]
	new_seq= None 
	for n, char in enumerate(seq): 
		first= True if new_seq == None else False
		try:
			i=pos_list.index(n)		
			new_seq = tag_list[i%2]+ char if first else new_seq+tag_list[i%2]+ char  
		except ValueError:   
			new_seq = char if first else new_seq+char
	return new_seq

class codon_usage:
	'''This class is used for displaying condon_usage from a dictionary/dictionary-like object '''
	def __init__(self,codon_dict):
		self.codon_d = codon_dict
	def csv_export(self,header="codon,Frequency,Average Frequency on Chromosome 8"):
		'''  To export codon table to csv string '''
		r_str=header
		for codon,freq in self.codon_d.items():
			freq_type= freq.split("_")
			r_str = r_str+ "\n"+codon+","+freq_type[0]+","+freq_type[1]
		return r_str
	def make_html(self,col,row):
		'''  To export codon table to html page based on table.html '''
		templateLoader = jinja2.FileSystemLoader( searchpath="template" )
		templateEnv = jinja2.Environment( loader=templateLoader )
		tempCodontable = templateEnv.get_template( "table.html" )
		return(tempCodontable.render( row =row ,codon= self.codon_d, col=col))

