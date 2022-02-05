import hhyu2,re


def isid(s):
	res=re.search(r"^[_a-zA-Z][_a-zA-Z0-9]*",str(s))
	return res!=None and res.group(0)==s


def main():
	yvyi=hhyu2.main()
	print(yvyi)
	data_seg=dict()
	code_seg=[]
	offset_tb=dict() # for array
	used_line_num=set()
	def get_loc(s:str):
		if(s in data_seg): return 'word ptr [{}]'.format(s)
		if(s in offset_tb): return 'word ptr [{}]'.format(offset_tb[s])
		return s # constant
	def get_v(s:str,regx:str='ax'):
		nonlocal code_seg
		s=str(s)
		try:# numeric constant
			rs=get_loc(s)
			if(rs[0]!='w'):rs=int(float(rs))
			code_seg+=['\tmov {},{}'.format(regx,rs)]
		except: # string assignment
			pass
		
	for line in yvyi:# 变量定义
		if(line[0][0]=='j'):
			used_line_num.add(line[3])
		for _ in range(1,4):
			tk=line[_]
			if(isid(tk) and tk not in data_seg and tk not in offset_tb):
				if(line[0]=='[]='):# 数组
					if(line[2].isnumeric()):# 数组长度定义 / 下标
						if(line[3]==tk):# 数组引用的临时变量
							offset_tb[tk]="{}+2*{}".format(line[1],line[2])
							continue 
						data_seg[tk]="dw {} dup(0)".format(line[2])
					else:
						data_seg[tk]="db {},0".format(line[1])
					continue
				data_seg[tk]="dw 0"
	line_num=0
	for line in yvyi:# 代码生成
		line_num+=1
		if(line_num in used_line_num):
			code_seg+=["line{}:".format(line_num)]
		if(line[0]=='in'):
			code_seg+=['\tcall readsiw']
			code_seg+=['\tmov {},ax'.format(get_loc(line[3]))]
			code_seg+=['\tcall dispcrlf']
		elif(line[0]=='out'):
			get_v(line[3])
			code_seg+=['\tcall dispsiw']
			code_seg+=['\tcall dispcrlf']
		elif(line[0]=='[]='):
			if(line[3].isnumeric()):
				code_seg+=['\tmov word ptr[{}+2*{}],{}'.format(line[1],line[2],line[3])]
				continue
		elif(line[0][0]=='j'):# 跳转
			jmp_dic={'j>':'jg','j=':'je','j<':'jl','j':'jmp'}
			if(line[0]!='j'):
				get_v(line[1],'ax')
				code_seg+=['\tcmp ax,{}'.format(get_loc(line[2]))]
			code_seg+=['\t{} line{}'.format(jmp_dic[line[0]],line[3])]
			
		elif(line[0]=='='):# 赋值 
			get_v(line[1])
			code_seg+=['\tmov {},ax'.format(get_loc(line[3]))]
		else:
			# operator
			get_v(line[1],'ax')
			get_v(line[2],'bx')
			if(line[0]=='+'):code_seg+=['\tadd ax,bx']
			if(line[0]=='-'):code_seg+=['\tsub ax,bx']
			if(line[0]=='*'):code_seg+=['\timul ax,bx']
			if(line[0]=='/'):
				code_seg+=['\txor dx,dx']
				code_seg+=['\tidiv bx']
			code_seg+=['\tmov {},ax'.format(get_loc(line[3]))]
	
	# 头尾工作
	result=[".model small\ninclude io.inc\n.686P\n.stack 200h\n.data"]
	for _ in data_seg:result+=["\t{} ".format(_)+data_seg[_]]
	result+=['.code\n.startup']
	for _ in code_seg:result+=[_]
	result+=['.exit\nend']
	f=open("final.asm",'w',encoding='UTF-8')
	for line in result:f.write(line+"\n")
	f.flush()

if __name__ == "__main__":
	main()