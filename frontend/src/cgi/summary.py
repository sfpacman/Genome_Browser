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

items= getdummy.getdummy(10)
print ("Content-Type: text/html\n")

print(tempSummary.render(items = items))
