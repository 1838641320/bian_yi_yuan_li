#include<iostream>
#include<cstring>
#include<queue>
#include<map>
#include<cassert>
using namespace std;
const static string key_words[]={
	"auto","break","case","char","const","continue","default",
	"do","double","else","enum","extern","float","for","goto","if",
	"inline","int","long","register","restrict","return","short",
	"signed","sizeof","static","struct","switch","typedef","union",
	"unsigned","void","volatile","while"};
const static char operator_or_delimiter[][3]={
   "+","-","*","/","<","<=",">",">=","=","==",
   "!=",";","(",")","^",",","\"","\'","#","&",
   "&&","|","||","%","~","<<",">>","[","]","{",
   "}","\\",".","\?",":","!","->","++","--"
};
int find_op(const char *s){
	auto op_table=operator_or_delimiter;
	int len=0,tlen,ret=-1,lengthof=sizeof(operator_or_delimiter)/sizeof(operator_or_delimiter[0]);
	if(isdigit(*s)||isalpha(*s)) return ret;
	for(int i=0;i<lengthof;i++){
		tlen=strlen(op_table[i]);
		if(strncmp(op_table[i],s,tlen)==0&&tlen>len){
			ret=i;
		}
	}
	if(isdigit(*(s+1))&&*op_table[ret]=='.') ret=-1;
	return ret;
}
struct {
	int tr[999][26],sz,ed[999],fa[999];
	int sta;
	void init(){
		memset(tr,0,sizeof(tr));
		memset(ed,-1,sizeof(ed));
		memset(fa,0,sizeof(fa));
	}
	void insert(const char *s,int num){
		int u=0,c,len=strlen(s);
		for(int i=0;i<len;i++){
			c=s[i]-'a';
			if(!tr[u][c]) tr[u][c]=++sz;
			u=tr[u][c];
		}
		ed[u]=num;
	}
	void build(){
		int q[999],l=0,r=0;
		for(int i=0;i<26;i++) if(tr[0][i])
			q[r++]=tr[0][i];
		while(l<r){
			int u=q[l++];
			for(int i=0;i<26;i++) {
				int ne=tr[u][i];
				if(ne) fa[ne]=tr[fa[u]][i],q[r++]=ne;
				else tr[u][i]=tr[fa[u]][i];
			}
		}
	}
	int get_next_status(const char *s){
		int p=*s,t;
		if(p<'a'||p>'z'||sta==-1) return sta=-1;
		else sta=tr[sta][p-'a'];
		if(sta==0) return sta=-1;
		p=*(s+1);
		if(!isalpha(p)&&p!='_'&&!isdigit(p)) t=0;
		return t==0?ed[sta]:-1;
	}
}find_key_words;
struct {
	map<string,int> str_to_id;
	vector<string> ids;
	string token;
	int sta;
	char trans[2][3]={0,1,0,0,1,1};
	int char_type(int c){
		if(c=='_'||isalpha(c)) return 1;
		if(isdigit(c)) return 2;
		return 0;
	}
	void init(){sta=0;}
	int extend_char(const char *s){
		int c=char_type(*s),ret=-1;
		sta=trans[sta][c];
		if(sta) token.push_back(*s);
		else token.clear();
		if(char_type(*(s+1))==0) {
			if(token.size()){
				if(!str_to_id.count(token))
					ids.push_back(token),
					str_to_id[token]=ids.size()-1;
				ret=str_to_id[token];
			}
			token.clear();
			sta=0;
		}
		return ret;
	}
}find_id;
struct {
	string token;
	//null,int part,dot,frac part
	char trans[3][3]={{0,1,2},{0,1,2},{0,2,0}};
	int sta;
	int char_type(int c){
		if(isdigit(c)) return 1;
		if(c=='.') return 2;
		return 0;
	}
	void init(){token.clear();}
	string extend_char(const char *s){
		int c=char_type(*s),ci=char_type(*(s+1));
		string ret;
		sta=trans[sta][c];
		if(sta) token.push_back(*s);
		else token.clear();
		if(trans[sta][ci]==0){
			ret=token;
			token.clear();
		}
		return ret;
	}
}find_float;
struct {
	string token;
	void init(){token.clear();}
	string extend_char(const char *s){
		string ret;
		if(!isdigit(*s)) return ret;
		else {
			token.push_back(*s);
			if(!isdigit(*(s+1))) 
				ret=token,
				token.clear();
		}
		return ret;
	}
}find_int;
struct {
	string str;
	int sta=0;
	int extend_char(const char *s){
		if(sta==1){
			str.push_back(*s);
			if(*s=='\"'&&*(s-1)!='\\')
				return !(sta=0);
		}
		else {
			str.clear();
			if(*s=='\"') sta=1;
		}
		return 0;
	}
}find_str;
vector<string> main2(){
	find_id.init();
	find_int.init();
	find_float.init();
	find_key_words.init();
	for(int i=0;i<34;i++)
		find_key_words.insert(key_words[i].c_str(),i);
	find_key_words.build();
	string inp;
	char buf[999];
	while(fgets(buf,999,stdin))
		inp+=string(buf);
	string i1,f1;
	int k1,id,op1,sz=inp.size(),line=1,col=0;
	const char *p=inp.c_str();
	vector<string> answer;
	for(int i=0;i<sz;i++,p++,col++){
		if(find_str.extend_char(p)){
			// printf("\"%s\t\t%d,%d\tstring constant\n",find_str.str.c_str(),line,col);
			answer.push_back("string");
			find_str.str.clear();
			continue;
		}
		if(*p=='\n') {line++,col=0;continue;}
		if(*p==' '||*p=='\t'||find_str.sta) continue;
		op1=find_op(p);
		k1=find_key_words.get_next_status(p);
		id=find_id.extend_char(p);
		f1=find_float.extend_char(p);
		i1=find_int.extend_char(p);
		if(op1!=-1){
			auto res=operator_or_delimiter[op1];
			// printf("%s\t\t%d,%d\t\t\t\t%d\n",res,line,col,1000+op1);
			answer.push_back(res+string("\n"));
			if(strlen(res)==2) i++,p++;
			find_key_words.sta=0;
		}
		else if(k1!=-1){
			// printf("%s\t\t%d,%d\tkey words\t\t%d\n",key_words[k1].c_str(),line,col,k1);
			answer.push_back(key_words[k1]+string("\n"));
		}
		else if(id!=-1){
			// printf("%s\t\t%d,%d\tidentifier\t\t%d\n",find_id.ids[id].c_str(),line,col,id+2000);
			answer.push_back("ID\t"+find_id.ids[id]+"\n");
		}
		else if(i1==f1&&i1.size()){
			// printf("%s\t\t%d,%d\tinteger constant\n",i1.c_str(),line,col);
			answer.push_back("integer\t"+i1+"\n");
		}
		else if(f1.size()){
			// printf("%s\t\t%d,%d\tfloat value constant\n",f1.c_str(),line,col);
			answer.push_back("float_constant\t"+f1+"\n");
		}
	}
	return answer;
}
int main(){
	freopen("code.txt","r",stdin);
	freopen("Lexical_analysis_result.txt","w",stdout);
	auto res=main2();
	for(auto i:res) cout<<i;
}