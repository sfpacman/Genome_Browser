#!/usr/bin/python3
import cgi
import cgitb
import jinja2
import getdummy
cgitb.enable()

script_path="../cgi/details.py"
form = cgi.FieldStorage()
if "search" in form:
	items = getdummy.getdummy_entry(form["search"].value)
	title = "Further information for"+ str(items["id"])
	enzyme_list = getdummy.getdummyenzyme()
	templateLoader = jinja2.FileSystemLoader( searchpath="template" )
	templateEnv = jinja2.Environment( loader=templateLoader )
	tempSummary = templateEnv.get_template( "Details.html" )
	print ("Content-Type: text/html\n")
	print(tempSummary.render(gene = items,items=enzyme_list,title=title,source_path= source_path)
elif "enzyme" in form:
	print ("Content-Type: text/html\n")
	print (form["enzyme"].value)
else:
	print ("Content-Type: text/html\n")
