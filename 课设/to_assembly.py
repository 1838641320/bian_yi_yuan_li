import hhyu2,re


def isid(s):
	res=re.search(r"^[_a-zA-Z][_a-zA-Z0-9]*",str(s))
	return res!=None and res.group(0)==s

yvyi={
1:      ['=', '99', '-', 'x'],
2:      ['[]=', 'b', '20', '-'],
3:      ['[]=', '"hello world"', '-', 's'],
4:      ['=', '0.5', '-', 'dp'],
5:      ['=', 0, '-', 'i'],
6:      ['=', '50', '-', 'i'],
7:      ['j>', 'i', '6', 12],
8:      ['j', '-', '-', 15],
9:      ['+', 'i', 1, 'T2'],
10:     ['=', 'T2', '-', 'i'],
11:     ['j', '-', '-', 7],
12:     ['-', 'i', '100', 'T3'],
13:     ['=', 'T3', '-', 'i'],
14:     ['j', '-', '-', 9],
15:     ['j<', 'i', '3', 17],
16:     ['j', '-', '-', 19],
17:     ['=', '2', '-', 'dp'],
18:     ['j', '-', '-', 20],
19:     ['=', '3', '-', 'dp'],
20:     ['j=', 'i', '6', 22],
21:     ['j', '-', '-', 25],
22:     ['+', 'i', '1', 'T6'],
23:     ['=', 'T6', '-', 'i'],
24:     ['j', '-', '-', 20],
25:     ['+', 'i', '9', 'T7'],
26:     ['=', 'T7', '-', 'i'],
27:     ['=', '0', '-', 'p'],
28:     ['=', '32', '-', 'y'],
29:     ['=', '1801', '-', 'xx'],
30:     ['=', 'y', '-', 'qq'],
31:     ['=', '20', '-', 'qqt'],
32:     ['+', 'y', '214745', 'T9'],
33:     ['+', 'xx', 'T9', 'T10'],
34:     ['=', 'T10', '-', 'ppp']
}

def main():
	# yvyi=hhyu2.main()
	# print(yvyi)
	data_seg=dict()
	code_seg=[]
	def get_v(s:str,regx:str='ax'):
		nonlocal code_seg
		if(s in data_seg):code_seg+=['\tmov {},word ptr [{}]'.format(regx,s)]
		else:
			try:code_seg+=['\tmov {},{}'.format(regx,int(float(s)))]
			except:pass # string assignment
		
	for _ in yvyi:# 变量定义
		line=yvyi[_]
		for _ in range(1,4):
			tk=line[_]
			if(isid(tk) and tk not in data_seg):
				if(line[0]=='[]='):# 数组
					if(line[2].isnumeric()):
						data_seg[tk]="dw {} dup(0)".format(line[2])
					else:
						data_seg[tk]="db {},0".format(line[1])
					continue
				data_seg[tk]="dw 0"
	
	for _ in yvyi:# 代码生成
		line=yvyi[_]
		if(_>1 and code_seg[-1][-1]==':'):
			code_seg.pop(-1)
		code_seg+=["line{}:".format(_)]
		if(line[0]=='[]='):
			pass
		elif(line[0][0]=='j'):# 跳转
			jmp_dic={'j>':'jg','j=':'je','j<':'jl','j':'jmp'}
			if(line[0]!='j'):
				get_v(line[1],'ax')
				get_v(line[2],'bx')
				code_seg+=['\tcmp ax,bx']
			code_seg+=['\t{} line{}'.format(jmp_dic[line[0]],line[3])]
			
		elif(line[0]=='='):# 赋值 
			get_v(line[1])
			code_seg+=['\tmov word ptr[{}],ax'.format(line[3])]
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
			code_seg+=['\tmov word ptr[{}],ax'.format(line[3])]
	
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