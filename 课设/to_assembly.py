import hhyu2,re


def isid(s):
	res=re.search(r"^[_a-zA-Z][_a-zA-Z0-9]*",str(s))
	return res!=None and res.group(0)==s


def main():
	yvyi=hhyu2.main()
	data_seg=dict()
	code_seg=[]
	offset_tb=dict() # for array
	used_line_num=set()
	array=dict() # 没有被初始化过
	structs=dict()
	struct_type=set()
	if(1):
		f1=open("struct_save.txt","r")
		lines=f1.readlines()
		for line in lines:
			if('struct' in line):
				struct_type.add(line.split()[0])
		f1.close()
		f1=open("array_assign.txt","r")
		for line in f1.readlines():
			if('<' not in line):
				v1=line.split()
				array[v1[0]]=' '.join(v1[1:])
			elif('struct' in line):
				v1=line.split(' ')
				structs[v1[0]]=v1[1]

	def get_loc(s:str):
		nonlocal code_seg
		if(s in offset_tb): return '[{}]'.format(offset_tb[s])
		sv=s.split('_')
		if('tb_' in s and 'arr_' not in s):
			return '[{}.{}]'.format(sv[1],sv[2])
		if('arr_' in s and 'tb_' not in s):
			code_seg+=['\tmov si,{}'.format(get_loc(sv[2]))]
			code_seg+=['\timul si,type {}'.format(sv[1])]
			return '[{}[si]]'.format(sv[1])
		if('arr_' in s and 'tb_' in s):
			code_seg+=['\tmov si,{}'.format(get_loc(sv[3]))]
			code_seg+=['\timul si,type {}'.format(sv[2])]
			return '[{}[si]].{}'.format(sv[2],sv[4])
		if(s in data_seg): return '[{}]'.format(s)
		return s # numeric constant
	def get_v(s:str,regx:str='ax'):
		nonlocal code_seg
		s=str(s)
		try:# numeric constant
			rs=get_loc(s)
			if(rs[0]!='['):rs=int(float(rs))
			code_seg+=['\tmov {},{}'.format(regx,rs)]
		except:
			print("\nwhat\n\nneed\ncheck\n")
		
	for line in yvyi:# 变量定义
		if(line[0][0]=='j'):
			used_line_num.add(line[3])
		for _ in range(1,4):
			tk=line[_]
			if(not isid(tk)):continue
			if('tb_' in tk or 'arr_' in tk):continue
			if(tk in array):
				if(tk not in data_seg):
					data_seg[tk]='{}\n\tdw {} dup(?)'.format(array[tk],line[2])
				continue
			if(tk not in data_seg and tk not in offset_tb):
				if(line[0]=='[]='):# 数组
					if(line[2].isnumeric()):# 数组长度定义 / 下标
						if(line[3]==tk):# 数组引用的临时变量
							offset_tb[tk]="{}+2*{}".format(line[1],line[2])
							continue 
						data_seg[tk]="dw {} dup(?)".format(line[2])
					else:
						data_seg[tk]="db {},0".format(line[1])# string
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
			jmp_dic={'j>':'jg','j=':'je','j<':'jl','j':'jmp','j==':'je'}
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
	line_num+=1
	if(line_num in used_line_num):code_seg+=["line{}:".format(line_num)]

	# 头尾工作
	result=[".model small\ninclude io.inc\n.686P\n.stack 200h\n.data"]
	f1=open("struct_save.txt","r")
	for line in f1.readlines():result+=[line[:-1]]
	f1.close()
	f1=open("array_assign.txt","r")
	for line in f1.readlines():
		if(line.split()[0] in array):continue
		result+=[line[:-1]]
	for _ in data_seg:result+=["\t{} ".format(_)+data_seg[_]]
	result+=['.code\n.startup']
	for _ in code_seg:result+=[_]
	result+=['.exit\nend']
	f=open("final.asm",'w',encoding='UTF-8')
	for line in result:f.write(line+"\n")
	f.flush()

if __name__ == "__main__":
	main()