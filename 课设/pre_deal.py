
import re

type_info=['int','char','long','float','double','short','signed','unsigned']
fin =open("code.txt","r",encoding="UTF-8")
text=fin.readlines()
for i in range(1,len(text)):text[0]+=text[i]
text=str(text[0])
result=''

def mysplite(s:str,sep:str,del_:str)->list:
	res=[]
	tk=''
	for i in range(len(s)):
		if(s[i] in sep):
			res.append(tk)
			if(s[i] not in del_):res.append(s[i])
			tk=''
		else:tk+=s[i]
	res=[x for x in res if x]
	return res

def remove_struct():
	global result,text
	struct_type={}
	i=0
	while 1:
		try:
			i=text.index('struct ')
			s2=mysplite(text[i:i+500],' ,}{;\n\t',' \n\t')
			name=s2[1]
			field={}
			if(s2[2]=='{'):# 定义 
				s2=s2[2:]
				ty=[]
				ids=[]
				for tk in s2:
					if(tk=='}'):
						s=i
						while(text[i]!='}'):i+=1# 使指针后移出结构体
						text=text[0:s]+text[i+2:] # 删除结构体定义
						struct_type[name]=field
						i=0
						break
					if(tk==',' or tk=='{'):continue
					if(tk==';'):# pop 所有类型
						ty1=' '.join(ty)
						ty.clear()
						for id in ids:field[id]=ty1
						ids.clear()
						continue
					if(tk in type_info):# 存下类型
						ty.append(tk)
						continue
					ids.append(tk)

			else:# 变量定义
				sty=s2[1]
				fd=struct_type[sty]
				s2=s2[2:]
				for tk in s2:
					if(tk==';'):break
					if(tk==','):continue
					for v in fd:result+='{} {}_{};'.format(fd[v],tk,v)
				s=i
				while(text[i]!=';'):i+=1
				text=text[0:s]+text[i+1:] # 删除结构体变量定义
				i=0

		except:break

	i=0
	while(1):
		if(i>=len(text)):break
		if(text[i]=='.' and (not text[i+1].isdigit())):
			text=text[0:i]+'_'+text[i+1:]
		i+=1
	result=result+text

def main():

	remove_struct()
	fout=open("code2.txt","w",encoding="UTF-8")
	fout.write(result)
	fout.close()


if __name__=='__main__':main()