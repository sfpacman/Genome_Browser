#!/usr/bin/python3

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

str="hello,itisme.californiadreamingsomethingIforget"
pos_tag=[0,4,5,12,40,56]
print(markup(str,pos_tag,"<br>",True))	
