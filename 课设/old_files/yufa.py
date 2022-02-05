from typing import Dict, List, Any
import sys

sys.setrecursionlimit(10000)
grammer = list()
terminal = list()
result = tuple()
result_list = list()
first = dict()
follow = dict()
select = dict()
table = dict()
VN = dict()


def remove_blank(lst: list):
    for l in lst:
        if l[-1] == '\n':
            index = lst.index(l)
            lst[index] = lst[index][0:-1]


def read_grammer(file: str):
    f = open(file, 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split()
        line.remove("::=")
        grammer.append(line)


def read_result(file: str):
    global result
    result = tuple()
    f = open(file, 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    remove_blank(lines)
    temp = list()
    for line in lines:
        l = line.split()
        result_list.append(l[0])
        temp.append(l)
    result = tuple(temp)  # 单词与种类号


def read_terminal(file: str):
    global terminal
    f = open(file, 'r', encoding='UTF-8')
    lines = f.readlines()
    f.close()
    remove_blank(lines)
    terminal = lines


def is_kong(s: str) -> bool:
    return s == 'eps'


def is_terminal(s: str) -> bool:
    return s in terminal


def is_VN(s: str) -> bool:
    for g in grammer:
        if s == g[0]:
            return True
    return False


def get_first(s) -> set:
    for g in grammer:
        if s == g[0]:
            flag = True  # 记录first集中是否包含空串
            for g_i in g[1:]:
                if s == g_i:
                    flag = False
                    break
                if not is_terminal(g_i) and not is_kong(g_i) and not VN[g_i]:  # 这是一个文法符号并且没有求过
                    get_first(g_i)
                    VN[g_i] = True
                if is_terminal(g_i) or 'eps' not in first[g_i]:
                    first[s] = first[s].union(first[g_i])
                    flag = False
                    break
                else:
                    fc = first[g_i].copy()
                    fc.discard("eps")
                    first[s] = first[s].union(fc)
            if flag:
                first[s].add("eps")
    return first[s]


def get_follow(s: str) -> set:
    if VN[s]:  # 已经求出follow集
        return follow[s]
    for g in grammer:
        index = 1
        for g_i in g[1:]:
            if g_i == s:
                if index == len(g) - 1 and g[0] != s:  # 最后一个符号
                    follow[s] = follow[s].union(get_follow(g[0]))
                    break
                fir = set()
                i = index + 1
                # 求xAy中y的first
                for gram in g[index + 1:]:
                    fir = fir.union(first[gram])
                    if 'eps' not in first[gram]:
                        break
                    elif i != len(g) - 1:
                        fir.discard('eps')
                    i += 1
                follow[s] = follow[s].union(fir)
                follow[s].discard('eps')
                if 'eps' in fir and g[0] != s:  # first集中包含空串
                    follow[s] = follow[s].union(get_follow(g[0]))
                VN[s] = True
            index += 1
    return follow[s]


def select_set():
    for g in grammer:
        se = set()
        flag = True
        i = 1
        for g_i in g[1:]:
            se = se.union(first[g_i])
            if 'eps' not in first[g_i]:
                break
            i += 1
        if 'eps' in se and i == len(g):  # first集中包含空串
            se.discard('eps')
            se = se.union(follow[g[0]])
        temp = g.copy()
        temp.insert(1, '::=')
        select[''.join(temp)] = se


def ananlyze_table():
    head = terminal.copy()
    head.append('#')  # 分析表的表头
    zuo = list()
    keys = select.keys()  # 规则
    for v in VN.keys():
        d = dict()
        for key in keys:
            temp = key.split('::=')
            if temp[0] == v:
                for h in head:
                    if h in select[key]:
                        d[h] = key
        table[v].update(d)
    print("分析表:")
    print(table)

    '''print("LL分析表:")
    print("\t\t\t", end='')
    for i in head:
        print("%3s\t\t\t" % i, end='')
    print()
    for key in table.keys():
        print("%-4s" % key, end='')
        key_in = table[key].keys()
        for h in head:
            if h in key_in:
                print('%12s' % (table[key][h]), end='')
            else:
                print("%12s" % 'empty', end='')
        print()'''


def analyze(s1: list, s2: str):
    global result_semanic, result_grammer  # 语义分析栈以及语法分析过程中用到的表达式
    stack1 = list('#')
    stack1.append(s2)  # 分析栈
    stack2 = s1.copy()
    stack2.append('#')  # 待输入符号串
    result_semanic, result_grammer = [], []
    i = 0
    index = 0  # 匹配到第index个产生式
    while True:
        if is_terminal(stack1[-1]):
            print('步骤' + str(i) + ':')
            print('分析栈: ' + ' '.join(stack1))
            print('待输入符号串: ' + ' '.join(stack2))
            if stack1[-1] == stack2[0]:
                print('下一步动作: ' + '弹出' + stack1[-1] + ',''指针后一个符号')
                if stack1[-1] == 'ID' or stack1[-1] == 'integer' or stack1[-1] == 'int62' or stack1[-1] == 'float_constant':
                    result_semanic.append(result[index][1])
                else:
                    result_semanic.append(result[index][0])
                stack1.pop()
                stack2.pop(0)
                index += 1
            else:
                print('下一步动作: ')
                print('分析失败!')
                break
        elif is_VN(stack1[-1]):
            print('步骤' + str(i) + ':')
            print('分析栈: ' + ' '.join(stack1))
            print('待输入符号串: ' + ' '.join(stack2))
            try:
                c = table[stack1[-1]][stack2[0]]  # 下一步分析用到的产生式
                for g in grammer:
                    temp = g.copy()
                    temp.insert(1, '::=')
                    if c == ''.join(temp):
                        print(c)
                        result_grammer += str(grammer.index(g))
                        if g[1] == 'eps':
                            print('下一步动作: 弹出 ' + stack1[-1])
                            stack1.pop()
                        else:
                            print('下一步动作: 弹出 ' + stack1[-1] + ',产生式' + c + '右部逆序入栈')
                            stack1.pop()
                            temp.reverse()
                            for v in temp[:len(temp) - 2]:
                                stack1.append(v)
                        break
            except OSError:
                print('下一步动作: ')
                print('分析失败!')
                break
        elif stack1[-1] == stack2[0] and stack1[-1] == '#':
            print('步骤' + str(i) + ':')
            print('分析栈:' + ' '.join(stack1))
            print('待输入符号串' + ' '.join(stack2))
            print('下一步动作:接受')
            print('分析成功!')
            break
        i += 1
        print()


def initial_set(s: str):
    for g in grammer:
        temp = g.copy()
        temp.insert(1, '::=')
        select[''.join(temp)] = set()
        table[g[0]] = dict()
        VN[g[0]] = False
        for g_i in g:
            follow[g_i] = set()
            first[g_i] = set()
            if is_terminal(g_i) or is_kong(g_i):
                first[g_i].add(g_i)
    # 初始化first集合
    for g in grammer:
        if not VN[g[0]]:
            get_first(g[0])
        VN[g[0]] = True
    print("first集:")
    print(first)
    # 初始化follow集合
    for key in VN.keys():
        VN[key] = False
    follow[s].add('#')
    for key in VN.keys():
        get_follow(key)
    print("follow集:")
    print(follow)
    # 初始化select集合
    select_set()
    print("select集合:")
    print(select)


def main():
    file1 = 'F:\pythonProject\\grammer2.txt'
    file2 = 'F:\pythonProject\\terminal.txt'
    file3 = 'F:\pythonProject\\Lexical_analysis_result.txt'
    read_grammer(file1)
    print("规则:")
    print(grammer)
    read_terminal(file2)
    print("终结符:")
    print(terminal)

    read_result(file3)
    print("待分析串:")

    print(result)
    print(result_list)

    initial_set('program')  # 初始化数据结构

    ananlyze_table()  # 构建分析表
    print('\n分析过程:')
    analyze(result_list, 'program')  # 构建分析过程,第一个为待分析串，第二个为起始符号
    print(result_grammer)
    print(result_semanic)
    return result_grammer, result_semanic

if __name__ == '__main__':
    main()
