.model small
include io.inc
.686P
.stack 200h
.data
x dw 0
b dw 20 dup(0)
s db "hello world",0
dp dw 0
i dw 0
T2 dw 0
T3 dw 0
T6 dw 0
T7 dw 0
p dw 0
y dw 0
xx dw 0
qq dw 0
qqt dw 0
T9 dw 0
T10 dw 0
ppp dw 0
.code
.startup
line1:
	mov ax,99
	mov word ptr[x],ax
line4:
	mov ax,0
	mov word ptr[dp],ax
line5:
	mov ax,0
	mov word ptr[i],ax
line6:
	mov ax,50
	mov word ptr[i],ax
line7:
	mov ax,word ptr [i]
	mov bx,6
	cmp ax,bx
	jg line12
line8:
	jmp line15
line9:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr[T2],ax
line10:
	mov ax,word ptr [T2]
	mov word ptr[i],ax
line11:
	jmp line7
line12:
	mov ax,word ptr [i]
	mov bx,100
	sub ax,bx
	mov word ptr[T3],ax
line13:
	mov ax,word ptr [T3]
	mov word ptr[i],ax
line14:
	jmp line9
line15:
	mov ax,word ptr [i]
	mov bx,3
	cmp ax,bx
	jl line17
line16:
	jmp line19
line17:
	mov ax,2
	mov word ptr[dp],ax
line18:
	jmp line20
line19:
	mov ax,3
	mov word ptr[dp],ax
line20:
	mov ax,word ptr [i]
	mov bx,6
	cmp ax,bx
	je line22
line21:
	jmp line25
line22:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr[T6],ax
line23:
	mov ax,word ptr [T6]
	mov word ptr[i],ax
line24:
	jmp line20
line25:
	mov ax,word ptr [i]
	mov bx,9
	add ax,bx
	mov word ptr[T7],ax
line26:
	mov ax,word ptr [T7]
	mov word ptr[i],ax
line27:
	mov ax,0
	mov word ptr[p],ax
line28:
	mov ax,32
	mov word ptr[y],ax
line29:
	mov ax,1801
	mov word ptr[xx],ax
line30:
	mov ax,word ptr [y]
	mov word ptr[qq],ax
line31:
	mov ax,20
	mov word ptr[qqt],ax
line32:
	mov ax,word ptr [y]
	mov bx,214745
	add ax,bx
	mov word ptr[T9],ax
line33:
	mov ax,word ptr [xx]
	mov bx,word ptr [T9]
	add ax,bx
	mov word ptr[T10],ax
line34:
	mov ax,word ptr [T10]
	mov word ptr[ppp],ax
.exit
end
