import sys

grammer=set()
first=dict()
follow=dict()
select=dict()
catergory_dict=set()

def read_grammer_file(file):
    global grammer
    f=open(file,"r",encoding="UTF-8")
    grammer=f.readlines()
    f.close()
    line_count=0
    for line in grammer:
        grammer=line.splite()
        grammer[line_count].remove('::=')
        line_count+=1

def isTerminal(str):
    return str in catergory_dict
def isKong(str:str):return str=="eps"

