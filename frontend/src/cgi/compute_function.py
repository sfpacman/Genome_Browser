#!/usr/bin/python3
import jinja2
from collections import OrderedDict 

def markup(seq,pos_list,tag,encapsulate=False):
	'''Adding html markup tag for both end to the seq based on the posistion from pos_list '''
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
	def csv_export(self,header="codon,Frequency"):
		r_str=header
		for codon,freq in self.codon_d.items():
			r_str+= "\n"+codon+","+freq
			return r_str
	def make_html(self,col,row):
		templateLoader = jinja2.FileSystemLoader( searchpath="template" )
		templateEnv = jinja2.Environment( loader=templateLoader )
		tempCodontable = templateEnv.get_template( "table.html" )
		return(tempCodontable.render( row =row ,codon= self.codon_d, col=col))

b= OrderedDict({"A":"35_12","B":"42_1","C":"23_23","D":"2_12"} )
a= codon_usage(b)
print(a.make_html(3,1))
