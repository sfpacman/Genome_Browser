#!/usr/bin/python3
import cgi
import cgitb
import jinja2
import getdummy
cgitb.enable()


form = cgi.FieldStorage()
templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

tempSummary = templateEnv.get_template( "Summary.html" )
#retrving input from the website 
a=form["query"].value.lower()
entry=a.split(":")
query_size = len(entry)
#action definition 
action_item= ["gid","protein","ga","cl"]

#generating html page
if query size > 1:
#if the input in not found in the action item list , error msg will show up  
	if entry[0] in action_item:
		action = entry[0]
		search_item = entry[1]
		#getrealstuff(action_itme,search_item)
		items= getdummy.getdummy(10)
		print ("Content-Type: text/html\n")
		print(tempSummary.render(items = items))
	else:
		print ("Content-Type: text/html\n")
		print('<p><span class="glyphicon glyphicon-alert"></span>Error: not an valid action  </p>')



