#!/usr/bin/python3
import cgi
import cgitb
import jinja2
import random
cgitb.enable()

def getdummyenzyme():
	enzyme=["ABC","DEF","CGI"]
	return enzyme    
def getdummy_entry(name):
	i=int(random.uniform(1, 26))
	translation= "ERENEVISSAELRLFREQVDQGPDWERGFHRINIYEVMKPPAEVVPGHLITRLLDTRLVHHNVTRWETFDVSPAVLRWTREKQPNYGLAIEVTHLHQTRTHQGQHVRISRSLPQGSGNWAQLRPLLVTFGHDGRGHALTRRRRAKRSPKHHSQRARKKNKNCRRHSLYVDFSDVGWNDWIVAPPGYQAFYCHGDCPFPLADHLNSTNHAIVQTLVNSVNSSIPKACCVPTELSAISMLYLDEYDKV"
	DNA="GGAGGGGCCGCCGGGGAAGAGGAGGAGGAAGGAAAGAAAGAAAGCGAGGGAGGGAAAGAGGAGGAAGGAAGATGCGAGAAGGCAGAGGAGGAGGGAGGGAGGGAAGGAGCGCGGAGCCCGGCCCGGAAGCTAGGTGAGTGTGGCATCCGAGCTGAGGGACGCGAGCCTGAGACGCCGCTGCTGCTCCGGCTGAGTATCTAGCTTGTCTCCCCGATGGGATTCCCGTCCAAGCTATCTCGAGCCTGCAGCGCCACAGTCCCCGGCCCTCGCCCAGGTTCACTGCAACCGTTCAGAGGTCCCCAGGAGCTGCTGCTGGCGAGCCCGCTACTGCAGGGACCTATGGAGCCATTCCGTAGTGCCATCCCGAGCAACGCACTGCTGCAGCTTCCCTGAGCCTTTCCAGCAAGTTTGTTCAAGATTGGCTGTCAAGAATCATGGACTGTTATTATATGCCTTGTTTTCTGTCAAGACACCATGATTCCTGGTAACCGAATGCTGATGGTCGTTTTATTATGCCAAGTCCTGCTAGGAGGCGCGAGCCATGCTAGTTTGATACCTGAGACGGGGAAGAAAAAAGTCGCCGAGATTCAGGGCCACGCGGGAGGACGCCGCTCAGGGCAGAGCCATGAGCTCCTGCGGGACTTCGAGGCGACACTTCTGCAGATGTTTGGGCTGCGCCGCCGCCCGCAGCCTAGCAAGA"  
	items = dict( id=name, p_name=chr(97+i)+"_object", ga= chr(97+i)+str(i*1000), location = "unkown", DNA=DNA, Protein = translation , DNA_C="???")
	return items
def getdummy(type,n):
	items=[]
	for i in range(0,n):
		x = i -26 *int(i/26) if i > 26 else i
		insert = dict( id=1000+i, name=chr(97+i)+"_object", an= chr(97+i)+str(i*1000), location = "unkown" )
		items.append(insert)
	return items

form = cgi.FieldStorage()
if "search" in form:
	items = getdummy_entry(form["search"].value")
	title = "Further information for"+ str(items["id"])
	enzyme_list = getdummyenzyme()
	templateLoader = jinja2.FileSystemLoader( searchpath="template" )
	templateEnv = jinja2.Environment( loader=templateLoader )
	tempSummary = templateEnv.get_template( "Details.html" )
	print ("Content-Type: text/html\n")
	print(tempSummary.render(gene = items,items=enzyme_list,title=title))
elif "enzyme" in form:
	print ("Content-Type: text/html\n")
	print (form["enzyme"].value)
else:
	print ("Content-Type: text/html\n")
#items=getdummy(10)

