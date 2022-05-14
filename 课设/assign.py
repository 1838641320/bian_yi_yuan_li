def main(result):
	i=-1
	while(1):# remove +=
		i+=1
		if(i>=len(result)):break
		if(result[i][0] in ['+','-','*','/'] and result[i+1][0]=='='):
			result=result[:i]+[result[i+1],result[i-1],(result[i][0],"operator")]+result[i+2:]
	i=-1
	while(1):# remove ++
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='++' or result[i][0]=='--'):
			result=result[:i]+[('=',"operator"),result[i-1],(result[i][0][0],"operator"),('integer',"1")]+result[i+1:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='[' and result[i+2][0]==']' and not result[i+1][1].isdigit()):
			result=result[:i-1]+[("ID",'arr_'+result[i-1][1]+'_'+str(result[i+1][1]))]+result[i+3:]
	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='.' and result[i+1][0]=='ID'):
			result=result[:i-1]+[("ID",'tb_'+result[i-1][1]+'_'+str(result[i+1][1]))]+result[i+2:]
	# 以下向前搜索数组赋值、数组

	f2=open("array_assign.txt","w",encoding="UTF-8")

	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='=' and result[i+1][0]=='{'):
			j=i
			res=''
			while(j>=0 and result[j][0]!='['):j-=1
			if(j<0): # 结构体
				id=result[i-1][1]
				j=i
				while(j>=0 and result[j][0]!='struct'):
					j-=1
				sid=result[j+1][1]
				res=str(id)+' '+str(sid)+'<'
				j=i+2
				while(result[j][0]!='}'):
					res+=result[j][1] if result[j][0]!=',' else ','
					j+=1
				res+='>\n'
			else:
				id=result[j-1][1]
				j=i
				while(j>=0 and result[j][0]!='struct' and result[j][0]!=';'):
					j-=1
				if(j>=0 and result[j][0]=='struct'):#结构体数组
					sid=result[j+1][1]# 结构体ID
					res=str(id)+' '
					j=i+2
					if(result[i-2][1].isdigit()):j+=1
					while(1):
						res+=str(sid)+'<'
						while(result[j][0]!='}'):
							res+=result[j][1] if result[j][0]!=',' else ','
							j+=1
						res+='>\n'
						j+=1
						if(result[j][0]=='}'):break
						else:j+=2
						
				else:#普通数组
					res=str(id)+' dw '
					j=i+2
					while(result[j][0]!='}'):
						res+=result[j][1] if result[j][0]!=',' else ','
						j+=1
					res+='\n'

			assert(result[j][0]=='}')
			result=result[:i]+result[j+1:]
			i-=1
			f2.write(res)


	f2.flush()
	f2.close()
	# 以上结束数组赋值的向前搜索

	i=-1
	while(1):
		i+=1
		if(i>=len(result)):break
		if(result[i][0]=='struct'):
			j=i
			while(result[j][0]!=';'):j+=1
			result=result[:i]+result[j+1:]
			i-=1
	return result
if __name__=='__main__':main()