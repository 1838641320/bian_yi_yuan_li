.model small
include io.inc
.686P
.stack 200h
.data
	x dw 0
	b dw 20 dup(0)
	ccc dw 7 dup(0)
	ppp1 dw 0
	qqq23 dw 23 dup(0)
	y dw 0
	z dw 5 dup(0)
	T1 dw 0
.code
.startup
	mov ax,99
	mov word ptr [x],ax
	mov word ptr[b+2*0],5
	mov word ptr[b+2*1],4
	mov word ptr[b+2*2],8
	mov ax,80
	mov word ptr [ppp1],ax
	mov ax,6
	mov word ptr [x],ax
	mov ax,1
	mov word ptr [y],ax
	mov ax,word ptr [x]
	cmp ax,6
	je line14
	jmp line15
line14:
	mov ax,23
	mov word ptr [x],ax
line15:
	mov ax,word ptr [x]
	cmp ax,4
	je line17
	jmp line20
line17:
	mov ax,word ptr [x]
	mov bx,1
	sub ax,bx
	mov word ptr [T1],ax
	mov ax,word ptr [T1]
	mov word ptr [x],ax
	jmp line20
line20:
	mov ax,word ptr [x]
	call dispsiw
	call dispcrlf
.exit
end
