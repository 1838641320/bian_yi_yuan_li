.model small
include io.inc
.686P
.stack 200h
.data
	x dw 0
	b dw 20 dup(0)
	ccc dw 7 dup(0)
	s db "hello world",0
	dp dw 0
	i dw 0
	T2 dw 0
	T3 dw 0
	T4 dw 0
	T7 dw 0
	T8 dw 0
	T14 dw 0
	T15 dw 0
	T16 dw 0
	p dw 0
.code
.startup
	mov ax,99
	mov word ptr [x],ax
	mov word ptr[b+2*0],5
	mov word ptr[b+2*1],4
	mov word ptr[b+2*2],8
	mov ax,0
	mov word ptr [dp],ax
	mov ax,0
	mov word ptr [i],ax
	call readsiw
	mov word ptr [i],ax
	call dispcrlf
line11:
	mov ax,word ptr [i]
	cmp ax,6
	jg line16
	jmp line21
line13:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr [T2],ax
	mov ax,word ptr [T2]
	mov word ptr [i],ax
	jmp line11
line16:
	mov ax,word ptr [i]
	mov bx,100
	sub ax,bx
	mov word ptr [T3],ax
	mov ax,33
	mov bx,word ptr [T3]
	add ax,bx
	mov word ptr [T4],ax
	mov ax,word ptr [T4]
	mov word ptr [i],ax
	mov ax,word ptr [i]
	call dispsiw
	call dispcrlf
	jmp line13
line21:
	mov ax,word ptr [i]
	cmp ax,3
	jl line23
	jmp line25
line23:
	mov ax,2
	mov word ptr [dp],ax
	jmp line26
line25:
	mov ax,3
	mov word ptr [dp],ax
line26:
	mov ax,word ptr [i]
	cmp ax,6
	je line28
	jmp line31
line28:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr [T7],ax
	mov ax,word ptr [T7]
	mov word ptr [i],ax
	jmp line26
line31:
	mov ax,word ptr [i]
	call dispsiw
	call dispcrlf
	mov ax,word ptr [x]
	call dispsiw
	call dispcrlf
	mov ax,word ptr [i]
	mov bx,9
	add ax,bx
	mov word ptr [T8],ax
	mov ax,word ptr [T8]
	mov word ptr [i],ax
	mov ax,9
	mov word ptr [ccc+2*5],ax
	mov ax,word ptr [ccc+2*3]
	mov bx,49
	sub ax,bx
	mov word ptr [T14],ax
	mov ax,7
	mov bx,word ptr [T14]
	add ax,bx
	mov word ptr [T15],ax
	mov ax,word ptr [ccc+2*0]
	mov bx,word ptr [T15]
	add ax,bx
	mov word ptr [T16],ax
	mov ax,word ptr [T16]
	mov word ptr [b+2*1],ax
	mov ax,0
	mov word ptr [p],ax
.exit
end
