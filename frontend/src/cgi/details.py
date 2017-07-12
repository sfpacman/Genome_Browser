#!/usr/bin/python3
'''
Script developed by Pak Hin Yu 
This script is a collection of all get methods for deatils page 
search: to create detail html page
enzyme: to create a string of enzyme with ^ tag
codon : to create codon frequency table  
'''

import cgi
import cgitb
import jinja2
import getdummy
import compute_function
#the API folder (/middlelayer/src/) needed to be moved to the forntend folder  
import findAPI
import REnz
import codon_freq
from collections import OrderedDict 

cgitb.enable()
form = cgi.FieldStorage()
source_path= "../cgi/details.py"

if "search" in form:
	ga=form["search"].value	
	#items = getdummy.getdummy_entry(form["search"].value)
	#items["ga"] = ga
	items = findAPI.find_all(ga,"ga")
	pos_list=findAPI.find_exon(items[ga])
	#pos_list = [1,5,10,20]
	title = "Further information for Gene"+ str(items["id"])
	items["DNA_C"]= compute_function.markup(items["DNA"],pos_list,"<mark>",True)
	#enzyme_list = getdummy.getdummyenzyme()
	enzyme_list =["EcoRI","BamHI","BsuMi"]
	templateLoader = jinja2.FileSystemLoader( searchpath="template" )
	templateEnv = jinja2.Environment( loader=templateLoader )
	tempSummary = templateEnv.get_template( "Details.html" )
	print ("Content-Type: text/html\n")
	print(tempSummary.render(gene = items,items=enzyme_list,title=title,source_path= source_path))
elif "enzyme" in form:
	#for enzyme html section 
	print ("Content-Type: text/html\n")
	seq=form["seq"].value
	enzyme = form["enzyme"].value
	
	if enzyme= "EcoRI":
		pos_list = REnz.find_EcoRi(seq)
	elif enzyme = "BsuMi":
		pos_list = REnz.find_BsuMi(seq)
	elif enzyme = "BamHi":
		pos_list= REnz.find_BamHi(seq)
	enzyme = compute_function.markup(seq,pos_list,"^")
	print ("<br> ^ indictaes digestion site </br>"+ enzyme)
elif "codon" in form:
	#Codon Frequency Table
	''' 
	freq=codon_freq.get_codon_freq(form["codon"].value)
	'''
	print ("Content-Type: text/html\n")
	freq=OrderedDict({"A":"35_12","B":"42_1","C":"23_23","D":"2_12"}
	display=compute_function.codon_usage(freq)
	print(display.make_html(2,2))
	#print(display.make_html(16,4))
else:
	print ("Content-Type: text/html\n")
