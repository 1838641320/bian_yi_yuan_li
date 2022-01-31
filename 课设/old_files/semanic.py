import parser
# import yvfa

# 语法分析的结果
result1 = list()  # 产生式
result2 = list()  # 待分析串
terminal = list()  # 终结符
table = dict()  # {符号名: 0:类型 ,1:num ,2:值}  0: 一般变量, 1:数组 , 2 : 函数
four = list()  # 四元式
struct = dict()  # 结构体定义集合{结构体名:变量1，变量2...}
analyze = list()  # 语义分析栈
label = 1  # 四元式暂存的结果
note = list()  # 暂存返回值
comp = {'bool': 0, 'int': 1, 'float': 1, 'double': 2}  # 用于类型转换


def deal(a: int):
    global analyze
    if a == 2:  # 终结符
        temp = result2[0]
        analyze += [result2[0]]
        result2.pop(0)
        return temp
    else:
        g = result1[0]
        grammer = 'fun_' + str(g + 1) + '()'
        return eval(grammer)


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
    return deal(2)  # int


# 产生式 type ::= int62
def fun_5():
    global result1, result2
    result1.pop(0)
    return deal(2)  # int62


# 产生式 type ::= float
def fun_6():
    global result1, result2
    result1.pop(0)
    return deal(2)  # float


# 产生式 type ::= double
def fun_7():
    global result1, result2
    result1.pop(0)
    return deal(2)  # double


# 产生式 type ::= void
def fun_8():
    global result1, result2
    result1.pop(0)
    deal(2)  # void
    return 0


# 产生式 type ::= char *
def fun_9():
    global result1, result2
    result1.pop(0)
    deal(2)  # char
    deal(2)  # *
    return 0


# 产生式 全局变量 ::= type ID 数组标识 赋值语句1
def fun_10():
    global result1, result2, table, four
    result1.pop(0)
    ty = deal(1)  # type
    name = deal(2)  # ID
    no, long = deal(1)  # 数组标识
    table[name] = [ty, not no, 0] # 值先设为为默认，求值之后再回填
    value = deal(1)  # 赋值语句1
    if no:  # 如果这不是一个数组
        if(len(value)):table[name][2] = [ty, 0, value]
        four += [('=', value, '-', name)]
    else:
        table[name] = [ty, 1, value]
        for i in range(len(value)):  # int a[5] ; int a[5]={1,2}
            four += [('[]=', name, i, value[i])]
        if len(value) == 0:
            four += [('[]=', name, long, '-')]
    return name


# 产生式 数组标识 ::= eps
def fun_11():
    global result1, result2
    result1.pop(0)
    return 1, 0


# 产生式 数组标识 ::= [ 常量表达式 ]
def fun_12():
    global result1, result2,analyze
    result1.pop(0)
    deal(2)  # [
    analyze.pop()
    long = deal(1)  # 常量表达式
    deal(2)  # ]
    analyze.pop()
    return 0, long


# 产生式 赋值语句1 ::= 赋值语句 全局变量2
def fun_13():
    global result1, result2
    result1.pop(0)
    value = deal(1)  # 赋值语句
    deal(1)  # 全局变量2
    return value


# 产生式 赋值语句1 ::= ( 形参列表 ) { local }
def fun_14():
    global result1, result2
    result1.pop(0)
    deal(2)  # (
    value = deal(1)  # 形参列表
    deal(2)  # )
    deal(2)  # {
    deal(1)  # local
    deal(2)  # }
    return value


# 产生式 赋值语句 ::= eps
def fun_15():
    global result1, result2
    result1.pop(0)
    return []


# 产生式 赋值语句 ::= = 求值式
def fun_16():
    global result1, result2
    result1.pop(0)
    deal(2)  # =
    analyze.pop()
    value = deal(1)  # 求值式
    return value


# 产生式 常量表达式 ::= integer
def fun_17():
    global result1, result2
    result1.pop(0)
    deal(2)  # integer
    analyze.pop()
    return 'int'


# 产生式 常量表达式 ::= float_constant
def fun_18():
    global result1, result2
    result1.pop(0)
    deal(2)  # float_constant
    analyze.pop()
    return 'float'


# 产生式 常量表达式 ::= ID
def fun_19():
    global result1, result2
    result1.pop(0)
    x = deal(2)  # ID
    analyze.pop()
    try:
        if table[x][1] != 0:
            print('类型不匹配，不能赋值!')  # 都为数值
    except:
        print('用于赋值的变量未定义!')
    else:
        return table[x]  # 查看变量类型是否匹配，否则进行类型转换,返回一个带信息的值好处理
    return 'unknown'


# 产生式 常量表达式 ::= string
def fun_20():
    global result1, result2
    result1.pop(0)
    deal(2)  # string
    return 'string'


# 产生式 全局变量2 ::= , ID 数组标识 赋值语句 全局变量2
def fun_21():
    global result1, result2
    result1.pop(0)
    deal(2)  # ,
    ty=analyze[-1]
    name=deal(2)  # ID
    no,long=deal(1)  # 数组标识
    table[name] = [ty, not no, 0] # 值先设为为默认，求值之后再回填
    deal(1)  # 赋值语句
    deal(1)  # 全局变量2
    return 0


# 产生式 全局变量2 ::= ;
def fun_22():
    global result1, result2
    result1.pop(0)
    deal(2)  # ;
    return 0


# 产生式 形参列表 ::= eps
def fun_23():
    global result1, result2
    result1.pop(0)
    return 0


# 产生式 形参列表 ::= type ID 形参列表2
def fun_24():
    global result1, result2
    result1.pop(0)
    deal(1)  # type
    deal(2)  # ID
    deal(1)  # 形参列表2
    return 0


# 产生式 形参列表2 ::= eps
def fun_25():
    global result1, result2
    result1.pop(0)
    return 0


# 产生式 形参列表2 ::= , type ID 形参列表2
def fun_26():
    global result1, result2
    result1.pop(0)
    deal(2)  # ,
    deal(1)  # type
    deal(2)  # ID
    deal(1)  # 形参列表2
    return 0


# 产生式 local ::= eps
def fun_27():
    global result1, result2
    result1.pop(0)
    return 0


# 产生式 local ::= 局部变量 local
def fun_28():
    global result1, result2
    result1.pop(0)
    deal(1)  # 局部变量
    deal(1)  # local
    return 0


# 产生式 local ::= for语句 local
def fun_29():
    global result1, result2
    result1.pop(0)
    deal(1)  # for语句
    deal(1)  # local
    return 0


# 产生式 local ::= if语句 local
def fun_30():
    global result1, result2
    result1.pop(0)
    deal(1)  # if语句
    deal(1)  # local
    return 0


# 产生式 local ::= while语句 local
def fun_31():
    global result1, result2
    result1.pop(0)
    deal(1)  # while语句
    deal(1)  # local
    return 0


# 产生式 local ::= do_while语句 local
def fun_32():
    global result1, result2
    result1.pop(0)
    deal(1)  # do_while语句
    deal(1)  # local
    return 0


# 产生式 local ::= return 求值式 ; local
def fun_33():
    global result1, result2
    result1.pop(0)
    deal(2)  # return
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


# 产生式 局部变量 ::= type ID 赋值语句 局部变量2
def fun_35():
    global result1, result2
    result1.pop(0)
    deal(1)  # type
    deal(2)  # ID
    deal(1)  # 赋值语句
    deal(1)  # 局部变量2
    return 0


# 产生式 局部变量2 ::= , ID 赋值语句 局部变量2
def fun_36():
    global result1, result2
    result1.pop(0)
    deal(2)  # ,
    deal(2)  # ID
    deal(1)  # 赋值语句
    deal(1)  # 局部变量2
    return 0


# 产生式 局部变量2 ::= ;
def fun_37():
    global result1, result2
    result1.pop(0)
    deal(2)  # ;
    return 0


# 产生式 for语句 ::= for ( 可空求值式 ; 可空求值式 ; 可空求值式 ) 语句
def fun_38():
    global result1, result2
    result1.pop(0)
    deal(2)  # for
    deal(2)  # (
    deal(1)  # 可空求值式
    deal(2)  # ;
    deal(1)  # 可空求值式
    deal(2)  # ;
    deal(1)  # 可空求值式
    deal(2)  # )
    deal(1)  # 语句


# 产生式 语句 ::= { 语句 }
def fun_39():
    global result1, result2
    result1.pop(0)
    deal(2)  # {
    deal(1)  # 语句
    deal(2)  # }


# 产生式 语句 ::= 求值式 ;
def fun_40():
    global result1, result2
    result1.pop(0)
    deal(1)  # 求值式
    deal(2)  # ;


# 产生式 语句 ::= for语句 语句
def fun_41():
    global result1, result2
    result1.pop(0)
    deal(1)  # for语句
    deal(1)  # 语句


# 产生式 语句 ::= if语句 语句
def fun_42():
    global result1, result2
    result1.pop(0)
    deal(1)  # if语句
    deal(1)  # 语句


# 产生式 语句 ::= while语句 语句
def fun_43():
    global result1, result2
    result1.pop(0)
    deal(1)  # while语句
    deal(1)  # 语句


# 产生式 语句 ::= do_while语句 语句
def fun_44():
    global result1, result2
    result1.pop(0)
    deal(1)  # do_while语句
    deal(1)  # 语句


# 产生式 语句 ::= switch语句 语句
def fun_45():
    global result1, result2
    result1.pop(0)
    deal(1)  # switch语句
    deal(1)  # 语句


# 产生式 可空求值式 ::= eps
def fun_46():
    global result1, result2
    result1.pop(0)


# 产生式 可空求值式 ::= 求值式
def fun_47():
    global result1, result2
    result1.pop(0)
    deal(1)  # 求值式


# 产生式 求值式 ::= integer 带符号右值
def fun_48():
    global result1, result2
    result1.pop(0)
    num = deal(2)  # integer
    info = deal(1)  # 带符号右值 info=[值，类型, 操作符]
    if info[1] == 'default':  # 带符号右值 ::= eps
        return [num, 'int']
    elif info[1] == 'int':
        value = eval(str(num) + info[2] + str(info[0]))
        return [value, 'int']
    elif info[1] == 'double':
        value = eval(str(num) + info[2] + str(info[0]))
        return [value, 'double']
    else:
        print('请先进行强制转换!')


# 产生式 求值式 ::= float_constant 带符号右值
def fun_49():
    global result1, result2, label, four
    result1.pop(0)
    num = deal(2)  # float_constant
    info = deal(1)  # 带符号右值
    if info[1] == 'default':
        return [num, table[num][0]]
    elif info[1] == 'float':
        four += [(info[2], num, info[0], 'T' + str(label))]
        label += 1
        value = eval(str(num) + info[2] + str(info[0]))
        return [value, 'int']
    elif info[1] == 'double':
        four += [(info[2], num, info[0], 'T' + str(label))]
        label += 1
        value = eval(str(num) + info[2] + str(info[0]))
        return [value, 'double']
    else:
        print('请先进行强制转换!')


# 产生式 求值式 ::= ID 带符号右值
def fun_50():
    global result1, result2, four, label
    result1.pop(0)
    num = deal(2)  # ID
    info = deal(1)  # 带符号右值
    try:
        if info[1] == 'default':
            return [num, table[num][0]]
        elif table[num][1] != 0:
            print('变量不是数值类型!')
        elif info[1] == table[num][0]:  # 数值类型相同
            four += [(info[2], num, info[0], 'T' + str(label))]
            label += 1
            value = eval(str(num) + info[2] + str(info[0]))
            return [value, info[1]]
        elif {'float', 'double'} == {info[1], table[num][0]} or {'int', 'double'} == {info[1], table[num][0]}:
            four += [(info[2], num, info[0], 'T' + str(label))]
            label += 1
            value = eval(str(num) + info[2] + str(info[0]))
            return [value, 'double']
        else:
            print('请先进行强制转换!')
    except:
        print('变量未定义!')


# 产生式 求值式 ::= ( 求值式 )
def fun_51():
    global result1, result2
    result1.pop(0)
    deal(2)  # (
    value = deal(1)  # 求值式
    deal(2)  # )
    return value


# 产生式 求值式 ::= string
def fun_52():
    global result1, result2
    result1.pop(0)
    num = deal(2)  # string
    return [num, 'string']


# 产生式 带符号右值 ::= ++
def fun_53():
    global result1, result2
    result1.pop(0)
    deal(2)  # ++
    return [1, 'int', '+']


# 产生式 带符号右值 ::= --
def fun_54():
    global result1, result2
    result1.pop(0)
    deal(2)  # --
    return [1, 'int', '-']


# 产生式 带符号右值 ::= eps
def fun_55():
    global result1, result2
    result1.pop(0)
    return [0, 'default', '+']


# 产生式 带符号右值 ::= + 求值式
def fun_56():
    global result1, result2
    result1.pop(0)
    deal(2)  # +
    value = deal(1)  # 求值式
    return [value[0], value[1], '+']


# 产生式 带符号右值 ::= - 求值式
def fun_57():
    global result1, result2
    result1.pop(0)
    deal(2)  # -
    value = deal(1)  # 求值式 ,求值式return[值，类型]
    return [value[0], value[1], '-']


# 产生式 带符号右值 ::= * 求值式
def fun_58():
    global result1, result2
    result1.pop(0)
    deal(2)  # *
    value = deal(1)  # 求值式
    return [value[0], value[1], '*']


# 产生式 带符号右值 ::= / 求值式
def fun_59():
    global result1, result2
    result1.pop(0)
    deal(2)  # /
    value = deal(1)  # 求值式
    return [value[0], value[1], '/']


# 产生式 带符号右值 ::= < 求值式
def fun_60():
    global result1, result2
    result1.pop(0)
    deal(2)  # <
    value = deal(1)  # 求值式
    return [value[0], value[1], '<']


# 产生式 带符号右值 ::= > 求值式
def fun_61():
    global result1, result2
    result1.pop(0)
    deal(2)  # >
    value = deal(1)  # 求值式
    return [value[0], value[1], '>']


# 产生式 带符号右值 ::= = 求值式
def fun_62():
    global result1, result2
    result1.pop(0)
    deal(2)  # =
    value = deal(1)  # 求值式
    return [value[0], value[1], '=']


# 产生式 带符号右值 ::= == 求值式
def fun_63():
    global result1, result2
    result1.pop(0)
    deal(2)  # ==
    value = deal(1)  # 求值式
    return [value[0], value[1], '==']


# 产生式 if语句 ::= if ( 求值式 ) if语句2
def fun_64():
    global result1, result2, four
    result1.pop(0)
    deal(2)  # if
    deal(2)  # (
    choice = deal(1)  # 求值式
    deal(2)  # )
    deal(1)  # if语句2


# 产生式 if语句2 ::= 语句 if语句3
def fun_65():
    global result1, result2
    result1.pop(0)
    deal(1)  # 语句
    deal(1)  # if语句3


# 产生式 if语句3 ::= eps
def fun_66():
    global result1, result2
    result1.pop(0)


# 产生式 if语句3 ::= else 语句
def fun_67():
    global result1, result2
    result1.pop(0)
    deal(2)  # else
    deal(1)  # 语句


# 产生式 while语句 ::= while ( 求值式 ) 语句
def fun_68():
    global result1, result2
    result1.pop(0)
    deal(2)  # while
    deal(2)  # (
    deal(1)  # 求值式
    deal(2)  # )
    deal(1)  # 语句


# 产生式 do_while语句 ::= do { 语句 } while ( 求值式 ) ;
def fun_69():
    global result1, result2
    result1.pop(0)
    deal(2)  # do
    deal(2)  # {
    deal(1)  # 语句
    deal(2)  # }
    deal(2)  # while
    deal(2)  # (
    deal(1)  # 求值式
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


# 产生式 switch语句 ::= switch ( 表达式 ) { case integer : next } 语句
def fun_71():
    global result1, result2
    result1.pop(0)
    deal(2)  # switch
    deal(2)  # (
    deal(1)  # 表达式
    deal(2)  # )
    deal(2)  # {
    deal(2)  # case
    deal(2)  # integer
    deal(2)  # :
    deal(1)  # next
    deal(2)  # }
    deal(1)  # 语句


# 产生式 next ::= break ; next
def fun_72():
    global result1, result2
    result1.pop(0)
    deal(2)  # break
    deal(2)  # ;
    deal(1)  # next


# 产生式 next ::= case integer : next
def fun_73():
    global result1, result2
    result1.pop(0)
    deal(2)  # case
    deal(2)  # integer
    deal(2)  # :
    deal(1)  # next


# 产生式 next ::= 语句 next
def fun_74():
    global result1, result2
    result1.pop(0)
    deal(1)  # 语句
    deal(1)  # next


# 产生式 next ::= default : 语句
def fun_75():
    global result1, result2
    result1 = result1[1:]
    deal(2)  # default
    deal(2)  # :
    deal(1)  # 语句


# 产生式 next ::= eps
def fun_76():
    global result1, result2
    result1.pop(0)


def main():
    # 语义分析
    # 中间代码生成
    global result1, result2, four
    result1, result2 = parser.main()
    deal(1)
    count = 1
    for f in four:
        print(str(count) + ':', end='\t')
        print(f)
        count += 1


if __name__ == "__main__":
	main()
