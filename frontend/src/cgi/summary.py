#!usr/bin/python3
import cgi
import cgitb
import jinja2
cgitb.enable()

def getdummy(n):
	items=[]
	for i in range(0,n):
		x = i -26 *int(i/26) if i > 26 else i
		insert = dict( id=1000+i, name=chr(97+i)+"_object", an= chr(97+i)+str(i*1000), location = "unkown" )
		items.append(insert)
	return items



templateLoader = jinja2.FileSystemLoader( searchpath="template" )
templateEnv = jinja2.Environment( loader=templateLoader )

tempSummary = templateEnv.get_template( "Summary.html" )

items=getdummy(10)
print(tempSummary.render(items = items))
