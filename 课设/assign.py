

def main(res):
	for i in range(1<<30):
		if(i>=len(res)):break
		if(res[i][0] in ['+','-','*','/'] and res[i+1][0]=='='):
			if(res[i-1][0]!=']'):
				res=res[:i]+[res[i+1],res[i-1],(res[i][0],"operator")]+res[i+2:]
			else:
				res=res[:i]+[res[i+1]]+res[i-4:i]+[(res[i][0],"operator")]+res[i+2:]
	for i in range(1<<30):
		if(i>=len(res)):break
		if(res[i][0]=='++' or res[i][0]=='--'):
			res=res[:i]+[('=',"operator"),res[i-1],(res[i][0][0],"operator"),('integer',"1")]+res[i+1:]
	for i in range(1<<30):
		if(i>=len(res)):break
		if(res[i][0]=='[' and res[i+2][0]==']' and not res[i+1][1].isdigit()):
			res=res[:i-1]+[("ID",'arr_'+res[i-1][1]+'_'+str(res[i+1][1]))]+res[i+3:]
	for i in range(1<<30):
		if(i>=len(res)):break
		if(res[i][0]=='.' and res[i+1][0]=='ID'):
			res=res[:i-1]+[("ID",'tb_'+res[i-1][1]+'_'+str(res[i+1][1]))]+res[i+2:]
	# 以下向前搜索数组赋值、数组

	f2=open("array_assign.txt","w",encoding="UTF-8")

	i=-1
	while(1):
		i+=1
		if(i>=len(res)):break
		if(res[i][0]=='=' and res[i+1][0]=='{'):
			j=i
			res_s=''
			while(j>=0 and res[j][0]!='['):j-=1
			if(j<0): # 结构体
				id=res[i-1][1]
				j=i
				while(j>=0 and res[j][0]!='struct'):
					j-=1
				sid=res[j+1][1]
				res_s=str(id)+' '+str(sid)+' < '
				j=i+2
				while(res[j][0]!='}'):
					res_s+=res[j][1] if res[j][0]!=',' else ','
					j+=1
				res_s+=' >\n'
			else:
				id=res[j-1][1]
				j=i
				while(j>=0 and res[j][0]!='struct' and res[j][0]!=';'):
					j-=1
				if(j>=0 and res[j][0]=='struct'):#结构体数组
					sid=res[j+1][1]# 结构体ID
					res_s=str(id)+' '
					j=i+3
					if(res[i-2][1].isdigit()):j+=1
					while(1):
						res_s+=str(sid)+' < '
						while(res[j][0]!='}'):
							res_s+=res[j][1] if res[j][0]!=',' else ','
							j+=1
						res_s+=' >\n'
						j+=1
						if(res[j][0]=='}'):break
						else:j+=2
						
				else:#普通数组
					res_s=str(id)+' dw '
					j=i+2
					while(res[j][0]!='}'):
						res_s+=res[j][1] if res[j][0]!=',' else ','
						j+=1
					res_s+='\n'

			assert(res[j][0]=='}')
			res=res[:i]+res[j+1:]
			i-=1
			f2.write(res_s)


	f2.flush()
	f2.close()
	# 以上结束数组赋值的向前搜索

	i=-1
	while(1):
		i+=1
		if(i>=len(res)):break
		if(res[i][0]=='struct'):
			j=i
			while(res[j][0]!=';'):j+=1
			res=res[:i]+res[j+1:]
			i-=1
	return res
if __name__=='__main__':main()