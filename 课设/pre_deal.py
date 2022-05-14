
import re

type_info=['int','char','*','char*','long','float','double','short','signed','unsigned']
fin =open("code.txt","r",encoding="UTF-8")
text=fin.readlines()
while(text[0][0]=='#'):text=text[1:]
for i in range(1,len(text)):text[0]+=text[i]

def remove_line_note(s:str):
	s=list(s)
	sta=0
	for i in range(len(s)):
		if(s[i]=='/'):sta+=1
		if(s[i]=='\n'):sta=0
		if(sta>=2):
			s[i]=' '
			if(s[i-1]=='/'):s[i-1]=' '
	return ''.join(s)

text=remove_line_note(text[0])
text=text.replace('name','name1')
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

struct_type={}
def remove_struct():
	global result,text
	i=0
	while 1:
		try:
			i=text.index('struct ',i)
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
				while(text[i]!=';'):i+=1

		except:break

	result=result+text

def main():

	remove_struct()
	fout=open("struct_save.txt","w",encoding="UTF-8")
	for k in struct_type:
		v=struct_type[k]
		fout.write("{} struct\n".format(k))
		for a in v:
			b=v[a]
			fout.write("{} {}\n".format(a,'db 16 dup(0)' if b in ['char *','char*'] else 'dw 0'))
		fout.write("{} ends\n".format(k))

	fout.close()
	fout=open("code2.txt","w",encoding="UTF-8")
	fout.write(result)
	fout.close()


if __name__=='__main__':main()