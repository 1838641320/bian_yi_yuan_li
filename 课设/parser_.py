import sys
import lex2,assign

grammer=list()
first=dict()
follow=dict()
select=dict()
catergory_dict=set()

def remove_line_break(li:list):
	for i in range(len(li)):
		if li[i][-1]=='\n':li[i]=li[i][0:-1]

def read_terminal(file):# 输入终结符
	global catergory_dict
	f=open(file,"r",encoding="UTF-8")
	catergory_dict=f.readlines()
	remove_line_break(catergory_dict)
	f.close()

def read_grammer_file(file):# 输入文法
	global grammer
	f=open(file,"r",encoding="UTF-8")
	file_content=f.readlines()
	f.close()
	for line in file_content:
		temp=line.split()# 空格分隔
		temp.remove("::=")
		grammer.append(temp)
	# print(grammer)
	

def isTerminal(str):return str in catergory_dict
def isKong(str:str):return str=="eps"

def getFirst():# 课本P78
	global first
	first=dict()
	for line in grammer:
		for token in line: # 首先加入终结符
			first[token]=set()
			if isTerminal(token) or isKong(token):
				first[token].add(token)
	for cnt in range(len(grammer)+9):# bellman_ford
		update=0
		for line in grammer:
			lens=len(first[line[0]])
			addt=line[0] # 产生式行开始的终结符
			i=1 # 记录该产生式第几个符号
			for token in line[1:]:
				i+=1
				# 产生式无空或者first集有空
				if ("eps" not in first[token]) or i==len(line):
					first[addt]=first[addt].union(first[token])
					break

				t=first[token].copy()
				t.discard("eps")
				first[addt]=first[addt].union(t)

			if lens != len(first[addt]): # 有更新
				update=1
		if not update:break # 无更新,break
	# print(first)


def getFollow():# 课本P79
	global follow
	follow = {}
	for line in grammer:
		for token in line:
			if not isTerminal(token) and token != "eps":
				follow[token]=set() # 只有非终结符才有follow集
	follow['program'].add("#")

	while(1):
		update=0
		for line in grammer:
			for i in range(1,len(line)):
				if isTerminal(line[i]) or line[i] == 'eps':
					continue
				lens=len(follow[line[i]])
				fir=set()
				for j in range(i+1,len(line)):# 获取后面的first集
					if ("eps" not in first[line[j]]) or (j==len(line)-1):
						fir=fir.union(first[line[j]])
						break
					t=first[line[j]].copy()
					t.discard("eps")
					fir=fir.union(t)

				if ("eps" in fir) or len(fir)==0:
					fir=fir.union(follow[line[0]])
					fir.discard("eps") # 去除空
				follow[line[i]]=follow[line[i]].union(fir)
				if lens!=len(follow[line[i]]):
					update=1

		if not update:break
	# print(follow)


def getSelect():
	global select
	select =dict()
	for i in range(len(grammer)):
		line=grammer[i]
		j=0
		fir=set()
		for j in range(1,len(line)):# 获取产生式后面的first集
			if ("eps" not in first[line[j]]) or (j==len(line)-1):
				fir=fir.union(first[line[j]])
				break
			t=first[line[j]].copy()
			t.discard("eps")
			fir=fir.union(t)
		if ("eps" in fir):# 如果右边产生式可以为空
			fir=fir.union(follow[line[0]])# 加入终结符的follow集
		fir.discard("eps")
		select[i]=fir
	# print(select)

terminal=set()
nterminal=set()
LL_1Table=dict() # 字典里面的终结符映射到产生式 str -> int
def getLL_1Table():
	global terminal,nterminal
	for line in grammer:
		for token in line:
			if isTerminal(token) or token=="eps":
				terminal.add(token)
			else: nterminal.add(token)
	terminal.add("#")
	for nt in nterminal:
		LL_1Table[nt]=dict()
	for line in select:
		nt=grammer[line][0]
		for tem in select[line]:
			if tem not in LL_1Table[nt]:
				LL_1Table[nt][tem]=line
			else:
				print("\n\n文法错误\n\n")
				print(LL_1Table[nt])
	for nt in LL_1Table:
		print(nt)
		print(LL_1Table[nt])
	print("\n\n\n")	

def analysis(file)->bool:
	parser_list=[]
	stack2=lex2.main()
	stack2=assign.main(stack2)
	lex_result_=stack2
	stack1=["#","program"]
	stack2.append(('#',))
	index=0
	while 1:
		tk=stack2[index][0]
		X=stack1.pop()
		if isTerminal(X):
			if tk==X:
				if X=='#':return (1,parser_list,lex_result_)
				print("pop 终结符"+str(X)+'\t'+str(stack2[index]))
				index+=1
				continue
			else:
				break
		else:
			try:
				line=grammer[LL_1Table[X][tk]].copy()
				print("产生式:"+str(line))
				for i in line[-1:0:-1]:
					if i!="eps":stack1.append(i)
				parser_list.append(LL_1Table[X][tk])
			except:
				break
		# print("状态栈")
		# print(stack1[-26:])
		# print("待分析单词")
		# for i in stack2[index:index+26]:
		# 	print(i[0],end=' ')
		# print('\n\n')
	return (0,0)

def main():
	read_terminal("terminal.txt")
	read_grammer_file("grammer2.txt")
	getFirst()
	getFollow()
	getSelect()
	getLL_1Table()
	ret=analysis("Lexical_analysis_result.txt")
	if(ret[0]):
		print('\n\n分析成功\n\n')
		for i in ret[1]:print(i)
		for i in range(len(ret[2])):
			if(ret[2][i][0] in ['ID','integer','float_constant','string']):
				ret[2][i]=ret[2][i][1]
			else:
				ret[2][i]=ret[2][i][0]
		return (ret[1],ret[2])
	else:print("分析失败")


if __name__ == "__main__":
	main()
