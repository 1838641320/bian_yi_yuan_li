.model small
include io.inc
.686P
.stack 200h
.data
	x dw 0
	T2 dw 0
	T4 dw 0
	T6 dw 0
.code
.startup
	mov ax,6
	mov word ptr [x],ax
	mov ax,word ptr [x]
	cmp ax,5
	jl line4
	jmp line6
line4:
	mov ax,word ptr [x]
	mov bx,1
	add ax,bx
	mov word ptr [T2],ax
	mov ax,word ptr [T2]
	mov word ptr [x],ax
line6:
	mov ax,word ptr [x]
	cmp ax,7
	jl line8
	jmp line10
line8:
	mov ax,word ptr [x]
	mov bx,1
	add ax,bx
	mov word ptr [T4],ax
	mov ax,word ptr [T4]
	mov word ptr [x],ax
line10:
	mov ax,word ptr [x]
	cmp ax,9
	jl line12
	jmp line14
line12:
	mov ax,word ptr [x]
	mov bx,1
	add ax,bx
	mov word ptr [T6],ax
	mov ax,word ptr [T6]
	mov word ptr [x],ax
line14:
	mov ax,word ptr [x]
	call dispsiw
	call dispcrlf
.exit
end
