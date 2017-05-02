#!/usr/bin/python3
'''
Script developed by Pak Hin Yu
This script will create a html summary table with a link-out for detail information for a particular gene  
'''
import cgi
import cgitb
import jinja2
import getdummy
#the API folder (/middlelayer/src/) needed to be moved to the forntend folder  
import findAPI
cgitb.enable()


form = cgi.FieldStorage()
templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

tempSummary = templateEnv.get_template( "Summary.html" )
source_path = "../cgi/details.py"
#retrving input from the website 
a=form["query"].value.lower()
entry=a.split(":")
query_size = len(entry)
#action definition 
action_item= ["gid","protein","ga","cl","Show All"]

#generating html page
if query size > 1:
#if the input in not found in the action item list , error msg will show up  
	if entry[0] in action_item:
		action = entry[0]
		search_item = entry[1]
		findAPI.find_all(action,search_item)
		#items= getdummy.getdummy(10)
		print ("Content-Type: text/html\n")
		print (entry[0])
		print(tempSummary.render(items = items,source_path=source_path))
	else:
		print ("Content-Type: text/html\n")
		print('<p><span class="glyphicon glyphicon-alert"></span>Error: not an valid action  </p>')



