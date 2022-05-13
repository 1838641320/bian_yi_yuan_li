.model small
include io.inc
.686P
.stack 200h
.data
	b_x dw 0
	b_y dw 0
	t_x dw 0
	t_y dw 0
	T1 dw 0
.code
.startup
	mov ax,0
	mov word ptr [b_x],ax
	mov ax,0
	mov word ptr [b_y],ax
	mov ax,0
	mov word ptr [t_x],ax
	mov ax,0
	mov word ptr [t_y],ax
	mov ax,88
	mov word ptr [b_x],ax
	mov ax,9
	mov word ptr [t_y],ax
	mov ax,word ptr [t_y]
	mov bx,word ptr [b_x]
	add ax,bx
	mov word ptr [T1],ax
	mov ax,word ptr [T1]
	mov word ptr [b_x],ax
	mov ax,word ptr [b_x]
	call dispsiw
	call dispcrlf
.exit
end
