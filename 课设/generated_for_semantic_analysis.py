
result1, result2=[],[]
def deal(x):1


# 产生式 program ::= eps
def fun_0():
	global result1, result2
	result1.pop(0)

# 产生式 program ::= struct ID { func_and_var } ; program
def fun_1():
	global result1, result2
	result1.pop(0)
	deal(2)		# struct
	deal(2)		# ID
	deal(2)		# {
	deal(1)		# func_and_var
	deal(2)		# }
	deal(2)		# ;
	deal(1)		# program

# 产生式 program ::= 全局变量 program
def fun_2():
	global result1, result2
	result1.pop(0)
	deal(1)		# 全局变量
	deal(1)		# program

# 产生式 type ::= int
def fun_3():
	global result1, result2
	result1.pop(0)
	deal(2)		# int

# 产生式 type ::= int62
def fun_4():
	global result1, result2
	result1.pop(0)
	deal(2)		# int62

# 产生式 type ::= float
def fun_5():
	global result1, result2
	result1.pop(0)
	deal(2)		# float

# 产生式 type ::= double
def fun_6():
	global result1, result2
	result1.pop(0)
	deal(2)		# double

# 产生式 type ::= void
def fun_7():
	global result1, result2
	result1.pop(0)
	deal(2)		# void

# 产生式 type ::= char *
def fun_8():
	global result1, result2
	result1.pop(0)
	deal(2)		# char
	deal(2)		# *

# 产生式 全局变量 ::= type ID 数组标识 赋值语句1
def fun_9():
	global result1, result2
	result1.pop(0)
	deal(1)		# type
	deal(2)		# ID
	deal(1)		# 数组标识
	deal(1)		# 赋值语句1

# 产生式 数组标识 ::= eps
def fun_10():
	global result1, result2
	result1.pop(0)

# 产生式 数组标识 ::= [ 常量表达式 ]
def fun_11():
	global result1, result2
	result1.pop(0)
	deal(2)		# [
	deal(1)		# 常量表达式
	deal(2)		# ]

# 产生式 赋值语句1 ::= 赋值语句 全局变量2
def fun_12():
	global result1, result2
	result1.pop(0)
	deal(1)		# 赋值语句
	deal(1)		# 全局变量2

# 产生式 赋值语句1 ::= ( 形参列表 ) { local }
def fun_13():
	global result1, result2
	result1.pop(0)
	deal(2)		# (
	deal(1)		# 形参列表
	deal(2)		# )
	deal(2)		# {
	deal(1)		# local
	deal(2)		# }

# 产生式 赋值语句 ::= eps
def fun_14():
	global result1, result2
	result1.pop(0)

# 产生式 赋值语句 ::= = 求值式
def fun_15():
	global result1, result2
	result1.pop(0)
	deal(2)		# =
	deal(1)		# 求值式

# 产生式 常量表达式 ::= integer
def fun_16():
	global result1, result2
	result1.pop(0)
	deal(2)		# integer

# 产生式 常量表达式 ::= float_constant
def fun_17():
	global result1, result2
	result1.pop(0)
	deal(2)		# float_constant

# 产生式 常量表达式 ::= ID
def fun_18():
	global result1, result2
	result1.pop(0)
	deal(2)		# ID

# 产生式 常量表达式 ::= string
def fun_19():
	global result1, result2
	result1.pop(0)
	deal(2)		# string

# 产生式 全局变量2 ::= , ID 数组标识 赋值语句 全局变量2
def fun_20():
	global result1, result2
	result1.pop(0)
	deal(2)		# ,
	deal(2)		# ID
	deal(1)		# 数组标识
	deal(1)		# 赋值语句
	deal(1)		# 全局变量2

# 产生式 全局变量2 ::= ;
def fun_21():
	global result1, result2
	result1.pop(0)
	deal(2)		# ;

# 产生式 形参列表 ::= eps
def fun_22():
	global result1, result2
	result1.pop(0)

# 产生式 形参列表 ::= type ID 形参列表2
def fun_23():
	global result1, result2
	result1.pop(0)
	deal(1)		# type
	deal(2)		# ID
	deal(1)		# 形参列表2

# 产生式 形参列表2 ::= eps
def fun_24():
	global result1, result2
	result1.pop(0)

# 产生式 形参列表2 ::= , type ID 形参列表2
def fun_25():
	global result1, result2
	result1.pop(0)
	deal(2)		# ,
	deal(1)		# type
	deal(2)		# ID
	deal(1)		# 形参列表2

# 产生式 local ::= eps
def fun_26():
	global result1, result2
	result1.pop(0)

# 产生式 local ::= 局部变量 local
def fun_27():
	global result1, result2
	result1.pop(0)
	deal(1)		# 局部变量
	deal(1)		# local

# 产生式 local ::= for语句 local
def fun_28():
	global result1, result2
	result1.pop(0)
	deal(1)		# for语句
	deal(1)		# local

# 产生式 local ::= if语句 local
def fun_29():
	global result1, result2
	result1.pop(0)
	deal(1)		# if语句
	deal(1)		# local

# 产生式 local ::= while语句 local
def fun_30():
	global result1, result2
	result1.pop(0)
	deal(1)		# while语句
	deal(1)		# local

# 产生式 local ::= do_while语句 local
def fun_31():
	global result1, result2
	result1.pop(0)
	deal(1)		# do_while语句
	deal(1)		# local

# 产生式 local ::= return 求值式 ; local
def fun_32():
	global result1, result2
	result1.pop(0)
	deal(2)		# return
	deal(1)		# 求值式
	deal(2)		# ;
	deal(1)		# local

# 产生式 local ::= repeat语句 local
def fun_33():
	global result1, result2
	result1.pop(0)
	deal(1)		# repeat语句
	deal(1)		# local

# 产生式 局部变量 ::= type ID 赋值语句 局部变量2
def fun_34():
	global result1, result2
	result1.pop(0)
	deal(1)		# type
	deal(2)		# ID
	deal(1)		# 赋值语句
	deal(1)		# 局部变量2

# 产生式 局部变量2 ::= , ID 赋值语句 局部变量2
def fun_35():
	global result1, result2
	result1.pop(0)
	deal(2)		# ,
	deal(2)		# ID
	deal(1)		# 赋值语句
	deal(1)		# 局部变量2

# 产生式 局部变量2 ::= ;
def fun_36():
	global result1, result2
	result1.pop(0)
	deal(2)		# ;

# 产生式 for语句 ::= for ( 可空求值式 ; 可空求值式 ; 可空求值式 ) 语句
def fun_37():
	global result1, result2
	result1.pop(0)
	deal(2)		# for
	deal(2)		# (
	deal(1)		# 可空求值式
	deal(2)		# ;
	deal(1)		# 可空求值式
	deal(2)		# ;
	deal(1)		# 可空求值式
	deal(2)		# )
	deal(1)		# 语句

# 产生式 语句 ::= { 语句 }
def fun_38():
	global result1, result2
	result1.pop(0)
	deal(2)		# {
	deal(1)		# 语句
	deal(2)		# }

# 产生式 语句 ::= 求值式 ;
def fun_39():
	global result1, result2
	result1.pop(0)
	deal(1)		# 求值式
	deal(2)		# ;

# 产生式 语句 ::= for语句 语句
def fun_40():
	global result1, result2
	result1.pop(0)
	deal(1)		# for语句
	deal(1)		# 语句

# 产生式 语句 ::= if语句 语句
def fun_41():
	global result1, result2
	result1.pop(0)
	deal(1)		# if语句
	deal(1)		# 语句

# 产生式 语句 ::= while语句 语句
def fun_42():
	global result1, result2
	result1.pop(0)
	deal(1)		# while语句
	deal(1)		# 语句

# 产生式 语句 ::= do_while语句 语句
def fun_43():
	global result1, result2
	result1.pop(0)
	deal(1)		# do_while语句
	deal(1)		# 语句

# 产生式 语句 ::= switch语句 语句
def fun_44():
	global result1, result2
	result1.pop(0)
	deal(1)		# switch语句
	deal(1)		# 语句

# 产生式 可空求值式 ::= eps
def fun_45():
	global result1, result2
	result1.pop(0)

# 产生式 可空求值式 ::= 求值式
def fun_46():
	global result1, result2
	result1.pop(0)
	deal(1)		# 求值式

# 产生式 求值式 ::= integer 带符号右值
def fun_47():
	global result1, result2
	result1.pop(0)
	deal(2)		# integer
	deal(1)		# 带符号右值

# 产生式 求值式 ::= float_constant 带符号右值
def fun_48():
	global result1, result2
	result1.pop(0)
	deal(2)		# float_constant
	deal(1)		# 带符号右值

# 产生式 求值式 ::= ID 带符号右值
def fun_49():
	global result1, result2
	result1.pop(0)
	deal(2)		# ID
	deal(1)		# 带符号右值

# 产生式 求值式 ::= ( 求值式 )
def fun_50():
	global result1, result2
	result1.pop(0)
	deal(2)		# (
	deal(1)		# 求值式
	deal(2)		# )

# 产生式 求值式 ::= string
def fun_51():
	global result1, result2
	result1.pop(0)
	deal(2)		# string

# 产生式 带符号右值 ::= ++
def fun_52():
	global result1, result2
	result1.pop(0)
	deal(2)		# ++

# 产生式 带符号右值 ::= --
def fun_53():
	global result1, result2
	result1.pop(0)
	deal(2)		# --

# 产生式 带符号右值 ::= eps
def fun_54():
	global result1, result2
	result1.pop(0)

# 产生式 带符号右值 ::= + 求值式
def fun_55():
	global result1, result2
	result1.pop(0)
	deal(2)		# +
	deal(1)		# 求值式

# 产生式 带符号右值 ::= - 求值式
def fun_56():
	global result1, result2
	result1.pop(0)
	deal(2)		# -
	deal(1)		# 求值式

# 产生式 带符号右值 ::= * 求值式
def fun_57():
	global result1, result2
	result1.pop(0)
	deal(2)		# *
	deal(1)		# 求值式

# 产生式 带符号右值 ::= / 求值式
def fun_58():
	global result1, result2
	result1.pop(0)
	deal(2)		# /
	deal(1)		# 求值式

# 产生式 带符号右值 ::= < 求值式
def fun_59():
	global result1, result2
	result1.pop(0)
	deal(2)		# <
	deal(1)		# 求值式

# 产生式 带符号右值 ::= > 求值式
def fun_60():
	global result1, result2
	result1.pop(0)
	deal(2)		# >
	deal(1)		# 求值式

# 产生式 带符号右值 ::= = 求值式
def fun_61():
	global result1, result2
	result1.pop(0)
	deal(2)		# =
	deal(1)		# 求值式

# 产生式 带符号右值 ::= == 求值式
def fun_62():
	global result1, result2
	result1.pop(0)
	deal(2)		# ==
	deal(1)		# 求值式

# 产生式 if语句 ::= if ( 求值式 ) if语句2
def fun_63():
	global result1, result2
	result1.pop(0)
	deal(2)		# if
	deal(2)		# (
	deal(1)		# 求值式
	deal(2)		# )
	deal(1)		# if语句2

# 产生式 if语句2 ::= 语句 if语句3
def fun_64():
	global result1, result2
	result1.pop(0)
	deal(1)		# 语句
	deal(1)		# if语句3

# 产生式 if语句3 ::= eps
def fun_65():
	global result1, result2
	result1.pop(0)

# 产生式 if语句3 ::= else 语句
def fun_66():
	global result1, result2
	result1.pop(0)
	deal(2)		# else
	deal(1)		# 语句

# 产生式 while语句 ::= while ( 求值式 ) 语句
def fun_67():
	global result1, result2
	result1.pop(0)
	deal(2)		# while
	deal(2)		# (
	deal(1)		# 求值式
	deal(2)		# )
	deal(1)		# 语句

# 产生式 do_while语句 ::= do { 语句 } while ( 求值式 ) ;
def fun_68():
	global result1, result2
	result1.pop(0)
	deal(2)		# do
	deal(2)		# {
	deal(1)		# 语句
	deal(2)		# }
	deal(2)		# while
	deal(2)		# (
	deal(1)		# 求值式
	deal(2)		# )
	deal(2)		# ;

# 产生式 repeat语句 ::= repeat do { 语句 } until 求值式
def fun_69():
	global result1, result2
	result1.pop(0)
	deal(2)		# repeat
	deal(2)		# do
	deal(2)		# {
	deal(1)		# 语句
	deal(2)		# }
	deal(1)		# until
	deal(1)		# 求值式

# 产生式 switch语句 ::= switch ( 表达式 ) { case integer : next } 语句
def fun_70():
	global result1, result2
	result1.pop(0)
	deal(2)		# switch
	deal(2)		# (
	deal(1)		# 表达式
	deal(2)		# )
	deal(2)		# {
	deal(2)		# case
	deal(2)		# integer
	deal(2)		# :
	deal(1)		# next
	deal(2)		# }
	deal(1)		# 语句

# 产生式 next ::= break ; next
def fun_71():
	global result1, result2
	result1.pop(0)
	deal(2)		# break
	deal(2)		# ;
	deal(1)		# next

# 产生式 next ::= case integer : next
def fun_72():
	global result1, result2
	result1.pop(0)
	deal(2)		# case
	deal(2)		# integer
	deal(2)		# :
	deal(1)		# next

# 产生式 next ::= 语句 next
def fun_73():
	global result1, result2
	result1.pop(0)
	deal(1)		# 语句
	deal(1)		# next

# 产生式 next ::= default : 语句
def fun_74():
	global result1, result2
	result1.pop(0)
	deal(2)		# default
	deal(2)		# :
	deal(1)		# 语句

# 产生式 next ::= eps
def fun_75():
	global result1, result2
	result1.pop(0)

