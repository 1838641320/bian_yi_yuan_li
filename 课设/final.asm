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
aa student < > 
	i dw 0
	num_140 dw 0
	sum dw 0
	T2 dw 0
	T3 dw 0
	T5 dw 0
	vv dw
	dw 12 dup(?)
	xvlu dw 6,4,2
	dw 9 dup(?)
	T8 dw 0
	T11 dw 0
.code
.startup
	mov ax,0
	mov [i],ax
	mov ax,0
	mov [num_140],ax
	mov ax,0
	mov [sum],ax
	mov ax,1000
	mov si,2
	imul si,type class
	mov [class[si]].score,ax
	mov ax,234
	mov [aa.age],ax
	mov ax,0
	mov [i],ax
line7:
	mov ax,[i]
	cmp ax,3
	jl line12
	jmp line19
line9:
	mov ax,[i]
	mov bx,1
	add ax,bx
	mov [T2],ax
	mov ax,[T2]
	mov [i],ax
	jmp line7
line12:
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
	jl line16
	jmp line18
line16:
	mov ax,[num_140]
	mov bx,1
	add ax,bx
	mov [T5],ax
	mov ax,[T5]
	mov [num_140],ax
line18:
	jmp line9
line19:
	mov ax,[sum]
	call dispsiw
	call dispcrlf
	mov ax,[num_140]
	call dispsiw
	call dispcrlf
	mov ax,[aa.age]
	call dispsiw
	call dispcrlf
	mov ax,7
	mov [vv+2*3],ax
	mov ax,565
	mov si,[i]
	imul si,type xvlu
	mov [xvlu[si]],ax
	mov ax,0
	mov [i],ax
line28:
	mov ax,[i]
	cmp ax,7
	jl line33
	jmp line38
line30:
	mov ax,[i]
	mov bx,1
	add ax,bx
	mov [T8],ax
	mov ax,[T8]
	mov [i],ax
	jmp line28
line33:
	mov ax,[vv+2*0]
	mov si,[i]
	imul si,type vv
	mov bx,[vv[si]]
	add ax,bx
	mov [T11],ax
	mov ax,[T11]
	mov [vv+2*0],ax
	jmp line30
line38:
	mov ax,[vv+2*0]
	mov [i],ax
	mov ax,[i]
	call dispsiw
	call dispcrlf
.exit
end
