
grammar_file="grammer.txt"
terminal_file="terminal.txt"
result_file="generated_for_semantic_analysis.py"

def remove_line_break(li:list):
	for i in range(len(li)):
		if li[i][-1]=='\n':li[i]=li[i][0:-1]

f=open(terminal_file,"r",encoding="UTF-8")
catergory_dict=f.readlines()
remove_line_break(catergory_dict)
f.close()

def isTerminal(str):return str in catergory_dict
def isKong(str:str):return str=="eps"

grammar=[]
f=open(grammar_file,"r",encoding="UTF-8")
file_content=f.readlines()
f.close()
for line in file_content:
	temp=line.split()# 空格分隔
	temp.remove("::=")
	grammar.append(temp)

f=open(result_file,"w",encoding="UTF-8")

f.write('''
result1, result2=[],[]
def deal(x):1\n\n
''')

index=-1

for line in grammar:
	index+=1
	f.write("# 产生式 "+str(line[0])+" ::= "+' '.join(line[1:])+'\n')
	f.write("def fun_"+str(index)+"():"+'\n')
	f.write("\tglobal result1, result2"+'\n')
	f.write("\tresult1.pop(0)"+'\n')
	for i in range(1,len(line)):
		if(isKong(line[i])):
			continue
		if(isTerminal(line[i])):
			f.write("\tdeal(2)")
		else:
			f.write("\tdeal(1)")
		f.write("\t\t# "+str(line[i])+'\n')
	f.write('\n')
	
f.close()