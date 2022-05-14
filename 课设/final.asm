.model small
include io.inc
.686P
.stack 200h
.data
student struct
name1 db 16 dup(0)
num dw 0
age dw 0
score dw 0
student ends
class student < "Li ping",5,18,145 >
student < "Zhang ping",4,19,131 >
student < "He fang",1,18,148 >
	i dw 0
	num_140 dw 0
	sum dw 0
	T2 dw 0
	T3 dw 0
	T5 dw 0
.code
.startup
	mov ax,0
	mov [i],ax
	mov ax,0
	mov [num_140],ax
	mov ax,0
	mov [sum],ax
	mov ax,200
	mov si,2
	imul si,type class
	mov [class[si]].score,ax
	mov ax,0
	mov [i],ax
line6:
	mov ax,[i]
	cmp ax,3
	jl line11
	jmp line18
line8:
	mov ax,[i]
	mov bx,1
	add ax,bx
	mov [T2],ax
	mov ax,[T2]
	mov [i],ax
	jmp line6
line11:
	mov ax,[sum]
	mov si,[i]
	imul si,type class
	mov bx,[class[si]].score
	add ax,bx
	mov [T3],ax
	mov ax,[T3]
	mov [sum],ax
	mov si,[i]
	imul si,type class
	mov ax,[class[si]].score
	cmp ax,140
	jl line15
	jmp line17
line15:
	mov ax,[num_140]
	mov bx,1
	add ax,bx
	mov [T5],ax
	mov ax,[T5]
	mov [num_140],ax
line17:
	jmp line8
line18:
	mov ax,[sum]
	call dispsiw
	call dispcrlf
	mov ax,[num_140]
	call dispsiw
	call dispcrlf
.exit
end
