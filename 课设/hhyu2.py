import parser_

# 语法分析的结果
result1 = list()  # 产生式
result2 = list()  # 待分析串
terminal = list()  # 终结符
table = dict()  # {符号名: 0:类型 ,1:flag ,2:值}  flag0: 一般变量, 1:数组 , 2 : 函数, 3:字符串，4：结构体)
# 结构体的 {s:student,4,null}
four = list()  # 四元式
struct = dict()  # 结构体定义集合{结构体名:变量1，变量2...}
strcut_value = dict()  # 结构体值{变量名:值}
analyze = list()  # 分析栈
analyze_1 = list()  # 保护分析栈
label = 1  # 四元式暂存的结果
note = list()  # 暂存返回值
comp = {'bool': 0, 'int': 1, 'float': 1, 'double': 2}  # 用于类型转换
word = 0


def deal(a: int):
	global analyze
	if a == 2:  # 终结符
		temp = result2[0]
		result2.pop(0)
		# print(result2)
		return temp
	else:
		g = result1[0] + 1
		# print(g)
		grammer = 'fun_' + str(g) + '()'
		return eval(grammer)


def fun_0(name: str, no: int, long: int):  # 包括了赋值语句,赋值语句的deal在这里
	global analyze, analyze_1, four, table, comp, word
	analyze_1 = analyze.copy()
	analyze.clear()
	word = name
	deal(1)  # 赋值语句
	if len(analyze):
		value = analyze.pop()  # [类型，0，(值，Ti)] ; [类型,0,值]
	else:
		value = []
	analyze = analyze_1.copy()
	if len(value) == 0:
		if no:
			four.append(['=', 0, '-', name])
		elif table[name][0] == 'string':
			four.append(['[]=', name, long, '-'])
			four.append(['=', "", '-', name])
		else:
			four.append(['[]=', name, long, '-'])
		return
	if value[0] == table[name][0] or comp[value[0]] != comp[table[name][0]]:
		if no:  # 不是数组
			if not isinstance(value[2], tuple):
				table[name][2] = value[2]
				four.append(['=', value[2], '-', name])
			else:
				table[name][2] = value[2][0]
				four.append(['=', value[2][1], '-', name])
		elif value[0] == 'string':
			table[name][2] = value[2]
			four.append(['[]=', value[2], '-', name])
		else:
			table[name][2] = (long, value[2])
			four.append(['[]=', name, long, '-'])
			for i in range(len(value[2])):  # int a[5] ; int a[5]={1,2}
				four.append(['[]=', name, i, value[2][i]])
	else:
		print('错误提示:赋值号两边类型不匹配!')


# 产生式 program ::= eps
def fun_1():
	global result1, result2
	result1.pop(0)
	return 0


# 产生式 program ::= struct ID { func_and_var } ; program
def fun_2():
	global result1, result2
	result1.pop(0)
	deal(2)  # struct
	name = deal(2)  # ID
	deal(2)  # {
	define = deal(1)  # program
	deal(2)  # }
	deal(2)  # ;
	struct[name] = define
	deal(1)  # program
	return 0


# 产生式 program ::= 全局变量 program
def fun_3():
	global result1, result2
	result1.pop(0)
	deal(1)  # 全局变量
	deal(1)  # program


# 产生式 type ::= int
def fun_4():
	global result1, result2
	result1.pop(0)
	deal(2)  # int
	return 'int'


# 产生式 type ::= int62
def fun_5():
	global result1, result2
	result1.pop(0)
	deal(2)  # int62
	return 'int'


# 产生式 type ::= float
def fun_6():
	global result1, result2
	result1.pop(0)
	deal(2)  # float
	return 'float'


# 产生式 type ::= double
def fun_7():
	global result1, result2
	result1.pop(0)
	deal(2)  # double
	return 'double'


# 产生式 type ::= void
def fun_8():
	global result1, result2
	result1.pop(0)
	deal(2)  # void
	return 'void'


# 产生式 type ::= char *
def fun_9():
	global result1, result2
	result1.pop(0)
	deal(2)  # char
	deal(2)  # *
	return 'char *'


# 产生式 全局变量 ::= type ID 数组标识 赋值语句1
def fun_10():
	global result1, result2, table, four, analyze, analyze_1
	result1.pop(0)
	ty = deal(1)  # type
	analyze.append(ty)
	name = deal(2)  # ID
	temp = deal(1)  # 数组标识
	no = temp[0]
	long = temp[1]
	table[name] = [ty, int(not no), long]  # 值先设为默认
	if ty == 'char *':
		table[name][1] = 1
		table[name][0] = 'string'
		no = 0
	analyze.append((name, no, long))
	deal(1)  # 赋值语句1 返回数据与函数的判断结果，值用analyze返回
	if len(analyze): analyze.pop()  # 弹出本次定义变量的类型


# 产生式 数组标识 ::= eps
def fun_11():
	global result1, result2
	result1.pop(0)
	return list([1, 0])


# 产生式 数组标识 ::= [ 常量表达式 ]
def fun_12():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # [
	l = deal(1)  # 常量表达式
	long = l[-1]
	if(not str(long).isnumeric()):
		four.append(['arr_',analyze[-2],long,'T150'])
	analyze.pop()
	deal(2)  # ]
	return list([0, long])


# 产生式 赋值语句1 ::= 赋值语句 全局变量2
def fun_13():
	global result1, result2, analyze, analyze_1, four
	result1.pop(0)
	temp = analyze[-1]  # (name,no,long)
	name = temp[0]
	no = temp[1]
	long = temp[2]

	fun_0(name, no, long)
	analyze.pop()
	deal(1)  # 全局变量2


# 产生式 赋值语句1 ::= ( 形参列表 ) { local }
def fun_14():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	deal(2)  # (
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 形参列表
	can = analyze.copy()
	analyze = analyze_1.copy()

	temp = analyze[-1]  # (name,no,long)
	name = temp[0]
	table[name][1] = 2
	table[name][2] = can
	analyze.pop()
	deal(2)  # )
	deal(2)  # {
	analyze.pop()
	deal(1)  # local
	deal(2)  # }


# 产生式 赋值语句 ::= eps
def fun_15():
	global result1, result2
	result1.pop(0)


# 产生式 赋值语句 ::= = 初始化赋值
def fun_16():
	global result1, result2
	result1.pop(0)
	deal(2)  # =
	deal(1)  # 初始化赋值


# 产生式 常量表达式 ::= integer
def fun_17():
	global result1, result2, analyze
	result1.pop(0)
	analyze.append(['int', 0, result2[0]])
	v = deal(2)  # integer
	return list(['int', v])


# 产生式 常量表达式 ::= float_constant
def fun_18():
	global result1, result2, analyze
	result1.pop(0)
	analyze.append(['float', 0, result2[0]])
	v = deal(2)  # float_constant
	return list(['float', v])


# 产生式 常量表达式 ::= ID
def fun_19():
	global result1, result2, analyze
	result1.pop(0)
	x = deal(2)  # ID
	try:
		if table[x][1] != 0:
			print('错误提示:类型不匹配，不能赋值!')  # 都为数值
		else:
			analyze.append(table[x])  # 查看变量类型是否匹配，否则进行类型转换,返回一个带信息的值好处理
			return x
	except:
		print('错误提示:用于赋值的变量未定义!')
		analyze.append(['unkonwn', 0, 0])


# 产生式 常量表达式 ::= string
def fun_20():
	global result1, result2, analyze
	result1.pop(0)
	v = deal(2)  # string
	analyze.append(['string', 0, v])


# 产生式 全局变量2 ::= , ID 数组标识 赋值语句 全局变量2
def fun_21():
	global result1, result2, analyze, analyze_1, four
	result1.pop(0)
	deal(2)  # ,
	ty = analyze[-1]
	name = deal(2)  # ID
	n = deal(1)  # 数组标识
	no = n[0]
	long = n[1]
	table[name] = [ty, int(not no), long]  # 值先设为为默认，求值之后再回填
	if ty == 'char *':
		table[name][1] = 1
		table[name][0] = 'string'
		no = 0
	fun_0(name, no, long)
	deal(1)  # 全局变量2


# 产生式 全局变量2 ::= ;
def fun_22():
	global result1, result2
	result1.pop(0)
	deal(2)  # ;


# 产生式 形参列表 ::= eps
def fun_23():
	global result1, result2, analyze
	result1.pop(0)


# 产生式 形参列表 ::= type ID 形参列表2
def fun_24():
	global result1, result2, analyze
	result1.pop(0)
	ty = deal(1)  # type
	name = deal(2)  # ID
	analyze.append((ty, name))
	deal(1)  # 形参列表2


# 产生式 形参列表2 ::= eps
def fun_25():
	global result1, result2
	result1.pop(0)


# 产生式 形参列表2 ::= , type ID 形参列表2
def fun_26():
	global result1, result2
	result1.pop(0)
	deal(2)  # ,
	ty = deal(1)  # type
	name = deal(2)  # ID
	analyze.append((ty, name))
	deal(1)  # 形参列表2


# 产生式 local ::= eps
def fun_27():
	global result1, result2
	result1.pop(0)


# 产生式 local ::= 局部变量 local
def fun_28():
	global result1, result2
	result1.pop(0)
	deal(1)  # 局部变量
	deal(1)  # local


# 产生式 local ::= for语句 local
def fun_29():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	deal(1)  # for语句
	deal(1)  # local


# 产生式 local ::= if语句 local
def fun_30():
	global result1, result2
	result1.pop(0)
	deal(1)  # if语句
	deal(1)  # local


# 产生式 local ::= while语句 local
def fun_31():
	global result1, result2
	result1.pop(0)
	deal(1)  # while语句
	deal(1)  # local


# 产生式 local ::= do_while语句 local
def fun_32():
	global result1, result2
	result1.pop(0)
	deal(1)  # do_while语句
	deal(1)  # local


# 产生式 local ::= return 求值式 ; local
def fun_33():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	deal(2)  # return
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 求值式
	deal(2)  # ;
	deal(1)  # local
	return 0


# 产生式 local ::= repeat语句 local
def fun_34():
	global result1, result2
	result1.pop(0)
	deal(1)  # repeat语句
	deal(1)  # local
	return 0


# 产生式 局部变量 ::= type ID 数组标识 赋值语句 局部变量2
def fun_35():
	global result1, result2, table, analyze
	result1.pop(0)
	ty = deal(1)  # type
	analyze.append(ty)
	name = deal(2)  # ID
	n = deal(1)  # 数组标识
	no = n[0]
	long = n[1]
	table[name] = [ty, int(not no), long]  # 值先设为默认
	if ty == 'char *':
		table[name][1] = 1
		table[name][0] = 'string'
		no = 0
	fun_0(name, no, long)
	# deal(1)  # 赋值语句
	deal(1)  # 局部变量2
	analyze.pop()


# 产生式 局部变量2 ::= , ID 数组标识 赋值语句 局部变量2
def fun_36():
	global result1, result2
	result1.pop(0)
	deal(2)  # ,
	ty = analyze[-1]
	name = deal(2)  # ID
	n = deal(1)  # 数组标识
	no = n[0]
	long = n[1]
	table[name] = [ty, int(not no), long]  # 值先设为为默认，求值之后再回填
	if ty == 'char *':
		table[name][1] = 1
		table[name][0] = 'string'
		no = 0
	fun_0(name, no, long)
	# deal(1)  # 赋值语句
	deal(1)  # 局部变量2


# analyze.pop()


# 产生式 局部变量2 ::= ;
def fun_37():
	global result1, result2
	result1.pop(0)
	deal(2)  # ;


# 产生式 for语句 ::= for ( 可空求值式1 ; 可空求值式2 ; 可空求值式3 ) 语句
''' 可空求值式1
	k:if 可空求值式12 == true:
		do 语句
		可空求值式3
		goto k
'''


def fun_38():
	global result1, result2, analyze, analyze_1, table, label, four
	result1.pop(0)
	flist = ['j', '-', '-', -1]  # 假出口
	deal(2)  # for
	deal(2)  # (
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 可空求值式1
	deal(2)  # ;

	analyze.clear()
	l1 = len(four) + 1
	deal(1)  # 可空求值式2
	tlist = four.pop()
	tlist[0] = 'j' + tlist[0]
	tlist[3] = -1
	four.append(tlist)
	tindex = len(four) - 1  # 该下标的四元式等待回填真出口
	four.append(flist)
	findex = tindex + 1
	deal(2)  # ;

	analyze.clear()
	l2 = len(four) + 1
	deal(1)  # 可空求值式3
	four.append(['j', '-', '-', l1])
	deal(2)  # )

	four[tindex][3] = len(four) + 1
	deal(1)  # 语句
	four.append(['j', '-', '-', l2])
	four[findex][3] = len(four) + 1

	analyze = analyze_1.copy()


# 产生式 语句 ::= { local }
def fun_39():
	global result1, result2
	result1.pop(0)
	deal(2)  # {
	deal(1)  # local
	deal(2)  # }


# 产生式 语句 ::= 求值式 ;
def fun_40():
	global result1, result2
	result1.pop(0)
	deal(1)  # 求值式
	deal(2)  # ;


# 初始化赋值 ::= 数组赋值
def fun_41():
	global result1, result2
	result1.pop(0)
	deal(1)  # 数组赋值


# 初始化赋值 ::= 求值式
def fun_42():
	global result1, result2
	result1.pop(0)
	deal(1)  # 求值式

def print_table(res_:list[list]):
	res=res_.copy()
	for i in range(len(res_)):res[i]=res_[i].copy()
	i=-1
	while(1):
		i+=1
		if(i>=len(res)):break
		cnt=0
		for j in range(4):
			x=res[i][j]
			if(not isinstance(x,str)):continue
			if('tb_' in x or 'arr_' in x):
				xv=x.split('_')
				if('tb_' in x and 'arr_' in x):
					res.insert(i,['arr_',str(xv[2]),str(xv[3]),'T150{}'.format(j)])
					i+=1
					res.insert(i,['tb_','T150{}'.format(j),str(xv[4]),'T100{}'.format(j)])
					i+=1
					cnt+=2
				if('tb_' in x and 'arr_' not in x):
					res.insert(i,['tb_',str(xv[1]),str(xv[2]),'T100{}'.format(j)])
					i+=1
					cnt+=1
				if('tb_' not in x and 'arr_' in x):
					res.insert(i,['arr_',str(xv[1]),str(xv[2]),'T100{}'.format(j)])
					i+=1
					cnt+=1
				res[i][j]='T100{}'.format(j)
		for k in range(0,len(res)):
			if(res[k][0][0]=='j' and res[k][3]>=i):res[k][3]+=cnt
	for l in res:print(l)
	


# 数组赋值 ::= { 常量表达式  赋值数列 }
def fun_43():
	global result1, result2, analyze, analyze_1, word
	result1.pop(0)
	deal(2)  # {
	name = word
	ty = table[name][0]

	value = list()
	value.append(table[name][0])

	value.append('1')
	x = deal(1)  # 常量表达式
	analyze.clear()

	if x[0] == ty:
		analyze.append(x[1])
	else:
		print('错误提示:元素类型与数组类型不符!')
	analyze.append(ty)
	deal(1)  # 赋值数列
	deal(2)  # }
	analyze.pop()  # 弹出ty
	v = analyze.copy()
	value.append(v)
	analyze = analyze_1.copy()
	analyze.append(value)


# 赋值数列 ::= , 常量表达式 赋值数列
def fun_44():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	deal(2)  # ,
	ty = analyze.pop()
	x = deal(1)  # 常量表达式
	analyze.pop()
	if x[0] == ty:
		analyze.append(x[1])
	else:
		print('错误提示:元素类型与数组类型不符!')
	analyze.append(ty)
	deal(1)  # 赋值数列


# 赋值数列 ::= eps
def fun_45():
	global result1, result2
	result1.pop(0)


# 产生式 可空求值式 ::= eps
def fun_46():
	global result1, result2
	result1.pop(0)


# 产生式 可空求值式 ::= 求值式
def fun_47():
	global result1, result2
	result1.pop(0)
	deal(1)  # 求值式


# 带符号右值
def fun(num1: str, no: int):# no 标志表示数组
	global four, label
	t = label
	if not no:
		label += 1

	deal(1)  # 带符号右值
	info = analyze.pop()
	try:
		if not no:
			if info[1] == 'default':
				analyze.append([info[1], 0, 'T' + str(t)])
			elif info[2] == '=':
				pass
				# four.append(['=', info[0], '-', 'T' + str(t)])
			else:# 数组和常量相加
				analyze.append([info[1], 0, 'T' + str(label)])
				pass
				# four.append([info[2], 'T' + str(t), info[0], 'T' + str(t + 1)])
			return
		# ID = t
		if info[2] == '=':
			four.append(['=', info[0], '-', num1])
		# x = ID 带符号右值
		elif info[1] == 'default':
			temp = table[num1][:2] if num1 in table else ['int',0]
			temp.append(num1)
			analyze.append(temp)
		elif num1 in table and table[num1][1] != 0:
			print('错误提示:变量不是数值类型!')
		elif num1 not in table or info[1] == table[num1][0]:  # 数值类型相同
			if info[2] == '++' or info[2] == '--':
				temp = table[num1][:2] if num1 in table else ['int',0]
				temp.append(num1)
				analyze.append(temp)  # a = i++;
				four.append([info[2][0], num1, info[0], 'T' + str(label)])
				four.append(['=', 'T' + str(label), '-', num1])
				label += 1
			else:
				four.append([info[2], num1, info[0], 'T' + str(label)])
				label += 1
				analyze.append([info[1], 0, 'T' + str(t)])
		# should be dead code
		elif comp[table[num1][0]] < comp[info[1]]:
			four.append([info[2], num1, info[0], 'T' + str(label)])
			label += 1
			analyze.append([info[1], 0, 'T' + str(t)])
		elif comp[table[num1][0]] > comp[info[1]]:
			four.append([info[2], num1, info[0], 'T' + str(label)])
			label += 1
			analyze.append([table[num1][0], 0, 'T' + str(t)])
		else:
			print('错误提示:请先进行强制转换!')
	except KeyError:
		print('错误提示:变量未定义!')
		exit(1)
	finally:
		return info


# 产生式 求值式 ::= integer 带符号右值
def fun_48():
	global result1, result2, analyze, comp, four, label, word
	result1.pop(0)
	num1 = deal(2)  # integer
	word = num1
	deal(1)  # 带符号右值 info=[值，类型, 操作符]
	info = analyze.pop()
	t = label
	if info[2] == '++' or info[2] == '--':
		print('错误提示:运算符号不可用!')
	if info[1] == 'default':  # 带符号右值 ::= eps
		analyze.append(['int', 0, num1])
	elif info[1] == 'int':
		four.append([info[2], num1, info[0], 'T' + str(label)])
		label += 1
		# value = eval(str(num1) + info[2] + str(info[0]))
		analyze.append(['int', 0, 'T' + str(t)])
	elif info[1] == 'double':
		four.append([info[2], num1, info[0], 'T' + str(label)])
		label += 1
		# value = eval(str(num1) + info[2] + str(info[0]))
		analyze.append(['double', 0, 'T' + str(t)])
	else:
		print('错误提示:请先进行强制转换!')


# 产生式 求值式 ::= float_constant 带符号右值
def fun_49():
	global result1, result2, analyze, comp, four, label, word
	result1.pop(0)
	num1 = deal(2)  # float_constant
	word = num1
	deal(1)  # 带符号右值
	info = analyze.pop()
	t = label  # 暂存四元式中中间结果T的下标
	if info[2] == '++' or info[2] == '--':
		print('错误提示:运算符号不可用!')
	if info[1] == 'default':
		analyze.append(['float', 0, num1])
	elif info[1] == 'float':
		four.append([info[2], num1, info[0], 'T' + str(label)])
		label += 1
		# value = eval(str(num1) + info[2] + str(info[0]))
		analyze.append(['float', 0, 'T' + str(t)])
	elif info[1] == 'double':
		four.append([info[2], num1, info[0], 'T' + str(label)])
		label += 1
		# value = eval(str(num1) + info[2] + str(info[0]))
		analyze.append(['double', 0, 'T' + str(t)])
	else:
		print('错误提示:请先进行强制转换!')


# 产生式 求值式 ::= ID 数组标识 带符号右值
def fun_50():
	global result1, result2, analyze, comp, four, label, word
	result1.pop(0)
	num1 = deal(2)  # ID
	word = num1
	t = label
	[no, long] = deal(1)  # 数组标识
	try:
		if not no:  # 是数组
			l = table[num1][2]  # (long,value)
			if int(long) < int(l):
				four.append(['[]=', num1, long, 'T' + str(t)])
				op = fun(num1, no)
				if (len(analyze)): analyze[-1][0] = 'int'
				if (op[1] != 'default'):
					if (op[2] == '='):
						four.append(['=', op[0], '-', 'T' + str(t)])
					else:
						four.append([op[2], 'T' + str(t), str(op[0]), 'T' + str(label)])
						label += 1
			else:
				print('错误提示:数组越界!')
			return
		else:
			fun(num1, no)
	except KeyError:
		print('错误提示:变量未定义!')


# 产生式 求值式 ::= ( 求值式 )
def fun_51():
	global result1, result2
	result1.pop(0)
	deal(2)  # (
	deal(1)  # 求值式
	deal(2)  # )


# 产生式 求值式 ::= string
def fun_52():
	global result1, result2, analyze
	result1.pop(0)
	num = deal(2)  # string
	analyze.append(['string', 0, num])


# 产生式 带符号右值 ::= ++
def fun_53():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # ++
	analyze.append([1, 'int', '++'])


# 产生式 带符号右值 ::= --
def fun_54():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # --
	analyze.append([1, 'int', '--'])


# 产生式 带符号右值 ::= eps
def fun_55():
	global result1, result2, analyze, word
	result1.pop(0)
	analyze.append([word, 'default', '+'])


# 产生式 带符号右值 ::= + 求值式
def fun_56():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # +
	deal(1)  # 求值式 [类型，0，值]
	value = analyze.pop()
	analyze.append([value[-1], value[0], '+'])


# 产生式 带符号右值 ::= - 求值式
def fun_57():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # -
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '-'])


# 产生式 带符号右值 ::= * 求值式
def fun_58():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # *
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '*'])


# 产生式 带符号右值 ::= / 求值式
def fun_59():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # /
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '/'])


# 产生式 带符号右值 ::= < 求值式
def fun_60():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # <
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '<'])


# 产生式 带符号右值 ::= > 求值式
def fun_61():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # >
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '>'])


# 产生式 带符号右值 ::= = 求值式
def fun_62():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # =
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '='])


# 产生式 带符号右值 ::= == 求值式
def fun_63():
	global result1, result2, analyze
	result1.pop(0)
	deal(2)  # ==
	deal(1)  # 求值式
	value = analyze.pop()
	analyze.append([value[-1], value[0], '=='])


# 产生式 if语句 ::= if ( 求值式 ) if语句2
def fun_64():
	global result1, result2, four, analyze, analyze_1
	result1.pop(0)
	deal(2)  # if
	deal(2)  # (
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 求值式
	analyze.clear()
	tlist = four.pop()
	tlist[0] = 'j' + tlist[0]
	tlist[3] = len(four) + 3
	four.append(tlist)
	four.append(['j', '-', '-', -1])
	analyze.append(len(four) - 1)
	deal(2)  # )
	deal(1)  # if语句2
	index = len(four) + 1
	for i in analyze:
		four[i][3] = index
	analyze = analyze_1.copy()


# 产生式 if语句2 ::= 语句 if语句3
def fun_65():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	findex = analyze.pop()
	deal(1)  # 语句
	four[findex][3] = len(four) + 1
	deal(1)  # if语句3


# 产生式 if语句3 ::= eps
def fun_66():
	global result1, result2
	result1.pop(0)


# 产生式 if语句3 ::= else 语句
def fun_67():
	global result1, result2
	result1.pop(0)
	four.append(['j', '-', '-', -1])  # 结束if语句
	analyze.append(len(four) - 1)
	deal(2)  # else
	deal(1)  # 语句


# 产生式 while语句 ::= while ( 求值式 ) 语句
def fun_68():
	global result1, result2, analyze, analyze_1, four
	result1.pop(0)
	deal(2)  # while
	deal(2)  # (
	analyze_1 = analyze.copy()
	analyze.clear()

	begin = len(four) + 1
	deal(1)  # 求值式
	tlist = four.pop()
	tlist[0] = 'j' + tlist[0][0]
	tlist[3] = len(four) + 3
	four.append(tlist)
	four.append(['j', '-', '-', -1])
	f = len(four) - 1
	analyze = analyze_1.copy()
	deal(2)  # )
	deal(1)  # 语句
	four.append(['j', '-', '-', begin])
	four[f][3] = len(four) + 1


# 产生式 do_while语句 ::= do { 语句 } while ( 求值式 ) ;
def fun_69():
	global result1, result2, analyze, analyze_1, four
	result1.pop(0)
	deal(2)  # do
	deal(2)  # {
	begin = len(four) + 1
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 语句
	analyze = analyze_1.copy()
	deal(2)  # }
	deal(2)  # while
	deal(2)  # (
	analyze_1 = analyze.copy()
	analyze.clear()
	deal(1)  # 求值式
	tlist = four.pop()
	tlist[0] = 'j' + tlist[0]
	tlist[3] = begin
	analyze = analyze_1.copy()
	deal(2)  # )
	deal(2)  # ;


# 产生式 repeat语句 ::= repeat do { 语句 } until 求值式
def fun_70():
	global result1, result2
	result1.pop(0)
	deal(2)  # repeat
	deal(2)  # do
	deal(2)  # {
	deal(1)  # 语句
	deal(2)  # }
	deal(1)  # until
	deal(1)  # 求值式


# 产生式 switch语句 ::= switch ( id ) { case integer : next }
def fun_71():
	global result1, result2, analyze, analyze_1, four
	result1.pop(0)
	deal(2)  # switch
	deal(2)  # (
	name = deal(2)  # id
	try:
		deal(2)  # )
		deal(2)  # {
		deal(2)  # case
		i = deal(2)  # integer
		four.append(['j=', name, i, len(four) + 3])  # if name == i:
		four.append(['j', '-', '-', -1])

		deal(2)  # :
		analyze_1 = analyze.copy()
		analyze.clear()
		analyze.append([name, len(four) - 1])
		deal(1)  # next

		temp = analyze.pop()
		l = len(four) + 1
		if len(temp) > 1:
			four[temp[1]][3] = l
		for index in analyze:
			four[index][3] = l
		analyze = analyze_1.copy()
		deal(2)  # }
	except:
		print('错误提示:该变量未定义!')


# 产生式 next ::= break ; next
def fun_72():
	global result1, result2, four, analyze
	result1.pop(0)

	deal(2)  # break
	value = analyze.pop()  # 把value放在栈顶
	four.append(['j', '-', '-', -1])
	analyze.append(len(four) - 1)  # break 的回填
	analyze.append(value)

	deal(2)  # ;
	deal(1)  # next


# 产生式 next ::= case integer : next
def fun_73():
	global result1, result2, four
	result1.pop(0)
	deal(2)  # case
	i = deal(2)  # integer

	value = analyze.pop()
	four[value[1]][3] = len(four) + 1
	four.append(['j=', value[0], i, len(four) + 3])
	four.append(['j', '-', '-', -1])
	value.pop()
	value.append(len(four) - 1)
	analyze.append(value)
	deal(2)  # :
	deal(1)  # next


# 产生式 next ::= 语句 next
def fun_74():
	global result1, result2, analyze
	result1.pop(0)

	a = analyze.copy()
	analyze.clear()
	deal(1)  # 语句

	analyze = a
	deal(1)  # next


# 产生式 next ::= default : 语句
def fun_75():
	global result1, result2, analyze, four
	result1 = result1[1:]
	value = analyze.pop()
	four[value[1]][3] = len(four) + 1
	value.pop()
	deal(2)  # default
	deal(2)  # :
	a = analyze.copy()
	analyze.clear()
	deal(1)  # 语句
	analyze = a
	analyze.append(value)


# 产生式 next ::= eps
def fun_76():
	global result1, result2
	result1.pop(0)


# 产生式 local ::= switch语句 local
def fun_77():
	global result1, result2
	result1.pop(0)
	deal(1)  # switch 语句
	deal(1)  # local


# local ::= 语句 local
def fun_78():
	global result1, result2, analyze, analyze_1
	result1.pop(0)
	deal(1)  # 语句
	deal(1)  # local


# 产生式 local ::= scanf ( string , & ID 输入参数 ) ; local
def fun_79():
	global result1, result2, four
	result1.pop(0)
	deal(2)  # scanf
	deal(2)  # (
	deal(2)  # string
	deal(2)  # ,
	deal(2)  # &
	four.append(['in', '-', '-', result2[0]])
	deal(2)  # ID
	deal(1)  # 输入参数
	deal(2)  # )
	deal(2)  # ;
	deal(1)  # local


# 产生式 local ::= printf ( string , ID 输出参数 ) ; local
def fun_80():
	global result1, result2
	result1.pop(0)
	deal(2)  # printf
	deal(2)  # (
	deal(2)  # string
	deal(2)  # ,
	four.append(['out', '-', '-', result2[0]])
	deal(2)  # ID
	deal(1)  # 输出参数
	deal(2)  # )
	deal(2)  # ;
	deal(1)  # local


# 产生式 输入参数 ::= eps
def fun_81():
	global result1, result2
	result1.pop(0)


# 产生式 输入参数 ::= , & ID 输入参数
def fun_82():
	global result1, result2
	result1.pop(0)
	deal(2)  # ,
	deal(2)  # &
	four.append(['in', '-', '-', result2[0]])
	deal(2)  # ID
	deal(1)  # 输入参数


# 产生式 输出参数 ::= eps
def fun_83():
	global result1, result2
	result1.pop(0)


# 产生式 输出参数 ::= , ID 输出参数
def fun_84():
	global result1, result2
	result1.pop(0)
	deal(2)  # ,
	four.append(['out', '-', '-', result2[0]])
	deal(2)  # ID
	deal(1)  # 输出参数

struct_types=dict[dict()]
struct_value=dict()
struct_value2=dict[dict()]
struct_const_val=[]

# 产生式 program ::= 结构体定义 program
def fun_85():
	global result1, result2
	result1.pop(0)
	deal(1)		# 结构体定义
	deal(1)		# program

# 产生式 结构体定义 ::= struct ID { 局部变量 局部变量2 } ;
def fun_86():
	global result1, result2,table
	result1.pop(0)
	deal(2)		# struct
	struct_id_now=deal(2)		# ID
	ttable=table
	deal(2)		# {
	deal(1)		# 局部变量
	deal(1)		# 局部变量2
	deal(2)		# }
	deal(2)		# ;
	for x in table:
		if(x not in ttable):  # 表示新定义的变量
			struct_types[struct_id_now][x]=table[x]
	table=ttable

# 产生式 local ::= 结构体变量定义 local
def fun_87():
	global result1, result2
	result1.pop(0)
	deal(1)		# 结构体变量定义
	deal(1)		# local

# 产生式 结构体变量定义 ::= struct ID ID 结构体初始化 结构体变量定义2
def fun_88():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# struct
	id1=deal(2)		# ID
	analyze.append(id1)
	id2=deal(2)		# ID
	struct_value[id2]=id1
	deal(1)		# 结构体初始化
	j=0
	for i in struct_types[id1]:
		struct_value2[id2][i]=struct_const_val[j]
		j+=1
	struct_const_val.clear()
	deal(1)		# 结构体变量定义2
	analyze.pop(-1)

# 产生式 结构体初始化 ::= eps
def fun_89():
	global result1, result2
	result1.pop(0)


# 产生式 结构体初始化 ::= { 求值式 结构体内部表达式 }
def fun_90():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# {
	deal(1)		# 求值式
	struct_const_val.append(analyze[-1])
	analyze.pop(-1)
	deal(1)		# 结构体内部表达式
	deal(2)		# }

# 产生式 结构体初始化 ::= = { 求值式 结构体内部表达式 }
def fun_91():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# =
	deal(2)		# {
	deal(1)		# 求值式
	struct_const_val.append(analyze[-1])
	analyze.pop(-1)
	deal(1)		# 结构体内部表达式
	deal(2)		# }

# 产生式 结构体内部表达式 ::= eps
def fun_92():
	global result1, result2
	result1.pop(0)

# 产生式 结构体内部表达式 ::= , 求值式 结构体内部表达式
def fun_93():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# ,
	deal(1)		# 求值式
	struct_const_val.append(analyze[-1])
	analyze.pop(-1)
	deal(1)		# 结构体内部表达式

# 产生式 结构体变量定义2 ::= ;
def fun_94():
	global result1, result2
	result1.pop(0)
	deal(2)		# ;

# 产生式 结构体变量定义2 ::= , ID 结构体初始化 结构体变量定义2
def fun_95():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# ,
	id2=deal(2)		# ID
	struct_value[id2]=analyze[-1]
	deal(1)		# 结构体初始化
	deal(1)		# 结构体变量定义2

# 产生式 带符号右值 ::= . ID
def fun_96():
	global result1, result2,analyze
	result1.pop(0)
	deal(2)		# .
	deal(2)		# ID
	value = analyze.pop()
	analyze.append([value[-1], value[0], '.'])
	four.append(['tb_','T150',value,-1])

# 产生式 常量表达式 ::= 结构体初始化
def fun_97():
	global result1, result2
	result1.pop(0)
	deal(1)		# 结构体初始化

def main():
	# 语义分析
	# 中间代码生成
	global result1, result2, four, table
	result1, result2 = parser_.main()
	print()
	deal(1)
	print_table(four)
	return four


if __name__ == "__main__":
	main()
