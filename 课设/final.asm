.model small
include io.inc
.686P
.stack 200h
.data
	x dw 0
	T2 dw 0
	T3 dw 0
	T5 dw 0
	T6 dw 0
	T8 dw 0
	T9 dw 0
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
	jmp line9
	mov ax,word ptr [x]
	mov bx,2
	xor dx,dx
	idiv bx
	mov word ptr [T3],ax
	mov ax,word ptr [T3]
	mov word ptr [x],ax
line9:
	mov ax,word ptr [x]
	cmp ax,7
	jl line11
	jmp line13
line11:
	mov ax,word ptr [x]
	mov bx,1
	add ax,bx
	mov word ptr [T5],ax
	mov ax,word ptr [T5]
	mov word ptr [x],ax
line13:
	jmp line16
	mov ax,word ptr [x]
	mov bx,2
	xor dx,dx
	idiv bx
	mov word ptr [T6],ax
	mov ax,word ptr [T6]
	mov word ptr [x],ax
line16:
	mov ax,word ptr [x]
	cmp ax,9
	jl line18
	jmp line20
line18:
	mov ax,word ptr [x]
	mov bx,1
	add ax,bx
	mov word ptr [T8],ax
	mov ax,word ptr [T8]
	mov word ptr [x],ax
line20:
	jmp line23
	mov ax,word ptr [x]
	mov bx,2
	xor dx,dx
	idiv bx
	mov word ptr [T9],ax
	mov ax,word ptr [T9]
	mov word ptr [x],ax
line23:
	mov ax,word ptr [x]
	call dispsiw
	call dispcrlf
.exit
end
