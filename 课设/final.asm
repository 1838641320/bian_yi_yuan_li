.model small
include io.inc
.686P
.stack 200h
.data
	p_x dw 0
	p_y dw 0
	q_x dw 0
	q_y dw 0
	x dw 0
	i dw 0
	T2 dw 0
	T4 dw 0
.code
.startup
	mov ax,0
	mov word ptr [p_x],ax
	mov ax,0
	mov word ptr [p_y],ax
	mov ax,0
	mov word ptr [q_x],ax
	mov ax,0
	mov word ptr [q_y],ax
	mov ax,9
	mov word ptr [x],ax
	mov ax,0
	mov word ptr [i],ax
	mov ax,0
	mov word ptr [i],ax
line8:
	mov ax,word ptr [i]
	cmp ax,9
	jl line13
	jmp line17
line10:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr [T2],ax
	mov ax,word ptr [T2]
	mov word ptr [i],ax
	jmp line8
line13:
	mov ax,word ptr [i]
	cmp ax,4
	je line15
	jmp line17
line15:
	mov ax,6
	mov word ptr [x],ax
	jmp line10
line17:
	mov ax,word ptr [x]
	mov bx,5
	add ax,bx
	mov word ptr [T4],ax
	mov ax,word ptr [T4]
	mov word ptr [x],ax
	mov ax,word ptr [x]
	call dispsiw
	call dispcrlf
.exit
end
