import sys
import re
import pre_deal

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
	"unsigned","void","volatile","while","int62","scanf","printf"]

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

def find_number(s:str)->tuple:
	integer=re.search(r"^[-+]?([1-9][0-9]*|0)",s)
	floating=re.search(r"^[-+]?([1-9][0-9]*|0?)\.?[0-9]*",s)
	# if(integer==None):return (0,)
	seg=floating.span()[1]
	ty='integer' if integer==None or floating.span()[1]<=integer.span()[1] else 'float_constant'
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
	pre_deal.main()
	global result,is_dim
	fin =open("code2.txt","r",encoding="UTF-8")
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
			result.append(tp if tp[0]!='int62' else ('int',tp[1]))
			ptr+=len(tp[0])
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

	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='+' and result[i+1][0]=='='):
			result=result[:i]+[result[i+1],result[i-1],('+',"operator")]+result[i+2:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='++'):
			result=result[:i]+[('=',"operator"),result[i-1],('+',"operator"),('integer',"1")]+result[i+1:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='--'):
			result=result[:i]+[('=',"operator"),result[i-1],('+',"operator"),('integer',"1")]+result[i+1:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='[' and result[i+2][0]==']'):
			result=result[:i-1]+[("ID",'arr_'+result[i-1][1]+'_'+str(result[i+1][1]))]+result[i+3:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='.' and result[i+1][0]=='ID'):
			result=result[:i-1]+[("ID",'tb_'+result[i-1][1]+'_'+str(result[i+1][1]))]+result[i+2:]

	for i in result:
		fout.write("{:18}{:}\n".format(i[0],i[1]))
	fout.flush()
	fout.close()
	return result

if __name__ =='__main__':main()
