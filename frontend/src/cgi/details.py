#!/usr/bin/python3
import cgi
import cgitb
import jinja2
import getdummy
import compute_function 
cgitb.enable()

script_path="../cgi/details.py"
form = cgi.FieldStorage()
if "search" in form:
	an=form["search"].value
	items = getdummy.getdummy_entry(form["search"].value)
	#items = get_real_stuff(an)
	title = "Further information for"+ str(items["id"])
	items["DNA_C"]= compute_function.markup(items["DNA"],pos_list,"<mark>")
	enzyme_list = getdummy.getdummyenzyme()
	templateLoader = jinja2.FileSystemLoader( searchpath="template" )
	templateEnv = jinja2.Environment( loader=templateLoader )
	tempSummary = templateEnv.get_template( "Details.html" )
	print ("Content-Type: text/html\n")
	print(tempSummary.render(gene = items,items=enzyme_list,title=title,source_path= source_path))
elif "enzyme" in form:
	#for enzyme html section 
	print ("Content-Type: text/html\n")
	#get_pos_enzyme(seq, form["enzyme"].value)
	enzyme = compute_function.markup(,pos_list,"^")
	print (enzyme)
elif "codon" in form:
	#Codon Frequency Table 
	#freq=getcodon(form["codon"].value)
	print(compute_function.codon_usage(freq))
else:
	print ("Content-Type: text/html\n")
