.model small
include io.inc
.686P
.stack 200h
.data
	i dw 0
	num_140 dw 0
	sum dw 0
	tb_arr_class_0_score dw 0
	tb_arr_class_1_score dw 0
	tb_arr_class_2_score dw 0
	T2 dw 0
	tb_arr_class_i_score dw 0
	T3 dw 0
	T5 dw 0
	s db "heldo",0
.code
.startup
	mov ax,0
	mov word ptr [i],ax
	mov ax,0
	mov word ptr [num_140],ax
	mov ax,0
	mov word ptr [sum],ax
	mov ax,145
	mov word ptr [tb_arr_class_0_score],ax
	mov ax,130
	mov word ptr [tb_arr_class_1_score],ax
	mov ax,149
	mov word ptr [tb_arr_class_2_score],ax
	mov ax,0
	mov word ptr [i],ax
line8:
	mov ax,word ptr [i]
	cmp ax,3
	jl line13
	jmp line20
line10:
	mov ax,word ptr [i]
	mov bx,1
	add ax,bx
	mov word ptr [T2],ax
	mov ax,word ptr [T2]
	mov word ptr [i],ax
	jmp line8
line13:
	mov ax,word ptr [sum]
	mov bx,word ptr [tb_arr_class_i_score]
	add ax,bx
	mov word ptr [T3],ax
	mov ax,word ptr [T3]
	mov word ptr [sum],ax
	mov ax,word ptr [i]
	cmp ax,140
	jl line17
	jmp line19
line17:
	mov ax,word ptr [num_140]
	mov bx,1
	add ax,bx
	mov word ptr [T5],ax
	mov ax,word ptr [T5]
	mov word ptr [num_140],ax
line19:
	jmp line10
line20:
	mov ax,word ptr [sum]
	call dispsiw
	call dispcrlf
	mov ax,word ptr [num_140]
	call dispsiw
	call dispcrlf
	mov ax,word ptr [s]
	call dispsiw
	call dispcrlf
.exit
end
