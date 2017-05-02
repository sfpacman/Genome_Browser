#!/usr/bin/python3
import cgi
import cgitb
import jinja2
import getdummy
import compute_function
from collections import OrderedDict 

'''
form={}
form["search"] = "GW2345"
form["codon"] = "Hello"
freq=OrderedDict({"A":"35_12","B":"42_1","C":"23_23","D":"2_12"} )
'''
cgitb.enable()
form = cgi.FieldStorage()
source_path= "../cgi/details.py"
if "search" in form:
	#an=form["search"]
	#items = getdummy.getdummy_entry(form["search"])
	ga=form["search"].value	
	items = getdummy.getdummy_entry(form["search"].value)
	items["ga"] = ga
	#items = findAPI.find_all(ga,"ga")
	#pos_list=findAPI.find_exon(items[ga])
	pos_list = [1,5,10,20]
	title = "Further information for"+ str(items["id"])
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
	seq=form[sequence]
	#get_pos_enzyme(seq, form["enzyme"].value)
	enzyme = compute_function.markup(seq,pos_list,"^")
	print (enzyme)
elif "codon" in form:
	#Codon Frequency Table 
	#freq=getcodon(form["codon"].value)
	display=compute_function.codon_usage(freq)
	print(display.make_html(2,2))
	#print(display.make_html(16,4))
else:
	print ("Content-Type: text/html\n")
