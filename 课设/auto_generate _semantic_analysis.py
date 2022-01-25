
grammar_file="grammer.txt"
terminal_file="terminal.txt"
result_file="generated_for_semantic_analysis.txt"

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

index=0

for line in grammar:
	index+=1
	print("# 产生式 "+str(line[0])+" ::= "+' '.join(line[1:]))
	print("def fun_"+str(index)+"():")
	print("\tglobal result1, result2")
	print("\tresult1 = result1[1:]")
	for i in range(1,len(line)):
		if(isKong(line[i])):
			continue
		if(isTerminal(line[i])):
			print("\tdeal(2)",end='')
		else:
			print("\tdeal(1)",end='')
		print("\t\t# "+str(line[i]))
	print('')
	
