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
	y dw 0
	xx dw 0
	qq dw 0
	qqt dw 0
	T17 dw 0
	T18 dw 0
	ppp dw 0
.code
.startup
	mov ax,99
	mov word ptr[x],ax
	mov word ptr[b+2*0],5
	mov word ptr[b+2*1],4
	mov word ptr[b+2*2],8
	mov ax,0
	mov word ptr[dp],ax
	mov ax,0
	mov word ptr[i],ax
	mov ax,50
	mov word ptr[i],ax
line11:
	mov ax,word ptr [i]
	mov bx,6
	cmp ax,bx
	jg line16
	jmp line20
line13:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr[T2],ax
	mov ax,word ptr [T2]
	mov word ptr[i],ax
	jmp line11
line16:
	mov ax,word ptr [i]
	mov bx,100
	sub ax,bx
	mov word ptr[T3],ax
	mov ax,33
	mov bx,word ptr [T3]
	add ax,bx
	mov word ptr[T4],ax
	mov ax,word ptr [T4]
	mov word ptr[i],ax
	jmp line13
line20:
	mov ax,word ptr [i]
	mov bx,3
	cmp ax,bx
	jl line22
	jmp line24
line22:
	mov ax,2
	mov word ptr[dp],ax
	jmp line25
line24:
	mov ax,3
	mov word ptr[dp],ax
line25:
	mov ax,word ptr [i]
	mov bx,6
	cmp ax,bx
	je line27
	jmp line30
line27:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr[T7],ax
	mov ax,word ptr [T7]
	mov word ptr[i],ax
	jmp line25
line30:
	mov ax,word ptr [i]
	mov bx,9
	add ax,bx
	mov word ptr[T8],ax
	mov ax,word ptr [T8]
	mov word ptr[i],ax
	mov ax,9
	mov word ptr[ccc+2*5],ax
	mov ax,word ptr [ccc+2*3]
	mov bx,49
	sub ax,bx
	mov word ptr[T14],ax
	mov ax,7
	mov bx,word ptr [T14]
	add ax,bx
	mov word ptr[T15],ax
	mov ax,word ptr [ccc+2*0]
	mov bx,word ptr [T15]
	add ax,bx
	mov word ptr[T16],ax
	mov ax,word ptr [T16]
	mov word ptr[b+2*1],ax
	mov ax,0
	mov word ptr[p],ax
	mov ax,32
	mov word ptr[y],ax
	mov ax,1801
	mov word ptr[xx],ax
	mov ax,word ptr [y]
	mov word ptr[qq],ax
	mov ax,20
	mov word ptr[qqt],ax
	mov ax,word ptr [y]
	mov bx,214745
	add ax,bx
	mov word ptr[T17],ax
	mov ax,word ptr [xx]
	mov bx,word ptr [T17]
	add ax,bx
	mov word ptr[T18],ax
	mov ax,word ptr [T17]
	mov word ptr[ppp],ax
.exit
end
