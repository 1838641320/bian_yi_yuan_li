import sys
import re

MAXL=80
result=[]

operator=[
	"+","-","*","/","<","<=",">",">=","=","==",
   "!=",";","(",")","^",",","\"","\'","#","&",
   "&&","|","||","%","~","<<",">>","[","]","{",
   "}","\\",".","?",":","!","->","++","--"]

key_words=[
	"auto","break","case","char","const","continue","default",
	"do","double","else","enum","extern","float","for","goto","if",
	"inline","int","long","register","restrict","return","short",
	"signed","sizeof","static","struct","switch","typedef","union",
	"unsigned","void","volatile","while","int62"]

def is_blank(s:str):
	if(len(s)==0):return 0
	return s.isspace()

def find_op_or_key_words(s:str)->tuple:
	def is_break(s:str)->bool:
		if(len(s)==0):return 1
		if(s.isalnum()or s=='_'): return 0
		return 1
	mat=''
	ty=''
	for i in operator:
		if(s[:len(i)]==i and len(i)>len(mat)):
			ty,mat="operator",i
	for i in key_words:
		li=len(i)
		if(s[:li]==i and li>len(mat) and is_break(s[li:li+1])):
			ty,mat="key_words",i
	if(len(mat)==0):return (0,0)
	return (mat,ty)

is_dim=0
def find_number(s:str)->tuple:
	integer=re.search(r"^[-+]?([1-9][0-9]*|0)",s)
	floating=re.search(r"^[-+]?([1-9][0-9]*|0?)\.?[0-9]*",s)
	if(integer==None):return (0,)
	seg=floating.span()[1]
	ty='float_constant' if floating.span()[1]>integer.span()[1] else 'integer'
	if(ty=='integer' or (is_dim&4)): # for int62
		int62=re.search(r"^[-+]?([1-9a-zA-Z][0-9a-zA-Z]*|0)",s)
		if((is_dim&4) or int62.span()[1]>integer.span()[1]):
			seg=int62.span()[1]
			st=s[0:seg]
			value=0
			for c in st:
				if(c.isdigit()):value=value*62+int(c)
				elif(c.islower()):value=value*62+ord(c)-97+10
				elif(c.isupper()):value=value*62+ord(c)-ord('A')+36
			return ("integer",str(value),seg)
	return (ty,s[0:seg])

def find_string_or_char(s:str)->tuple:
	res=re.search(r'^"[^"]*"',s)
	if(res!=None):return ("string",s[0:res.span()[1]])
	res=re.search(r"'[^']'",s)
	if(res!=None):return ("integer",ord(s[1]))
	return (0,0)

id_table=[]
def find_identifier(s:str)->tuple:
	res=re.search(r"^[_a-zA-Z][_a-zA-Z0-9]*",s)
	if(res==None):return (0,0)
	id1=res.group(0)
	if id1 not in id_table:
		if((is_dim&2)==0):return (0,0)
		id_table.append(id1)
	return ("ID",s[0:res.span()[1]])

def remove_line_note(s:str):
	s=list(s)
	sta=0
	for i in range(len(s)):
		if(s[i]=='/'):sta+=1
		if(s[i]=='\n'):sta=0
		if(sta>=2):
			s[i]=' '
			if(s[i-1]=='/'):s[i-1]=' '
	return ''.join(s)

def main()->list:
	global result,is_dim
	fin =open("code.txt","r",encoding="UTF-8")
	fout=open("Lexical_analysis_result.txt","w",encoding="UTF-8")
	intp=fin.readlines()
	for i in range(1,len(intp)):intp[0]+=intp[i]
	intp=remove_line_note(intp[0])
	maxl=len(intp)
	ptr=0
	result=[]
	while(ptr<maxl):
		while(ptr<maxl and is_blank(intp[ptr])):ptr+=1
		if(ptr>=maxl):break
		nexts=intp[ptr:ptr+MAXL]
		tp=find_string_or_char(nexts)
		if(tp[0]!=0):
			print(tp)
			result.append(tp)
			ptr+=3 if(tp[0]=="integer") else len(tp[1])
			continue
		tp=find_op_or_key_words(nexts)
		if(tp[0]!=0):
			print(tp)
			result.append(tp)
			ptr+=len(tp[0])
			if(tp[0] in ['int62','int','float','double','void','char']):is_dim=3
			if(tp[0]=='int62'):is_dim|=4
			if(tp[0]==';'):is_dim=0
			if(tp[0]=='='):is_dim&=2
			if(tp[0]==','):is_dim|=1
			continue
		tp=find_identifier(nexts)
		if(tp[0]!=0):
			print(tp)
			result.append(tp)
			ptr+=len(tp[1])
			continue
		tp=find_number(nexts)
		if(tp[0]!=0):
			print(tp)
			result.append(tp)
			ptr+=len(tp[1]) if len(tp)==2 else tp[2]
			continue

	for i in result:
		fout.write("{:18}{:}\n".format(i[0],i[1]))
	fout.flush()
	fout.close()
	return result

if __name__ =='__main__':main()
