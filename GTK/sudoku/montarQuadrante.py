#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
listaMatriz =[6, 2, 4, 0, 1, 5, 9, 0, 7, 3, 8,
 9, 7, 8, 0, 2, 6, 3, 0, 1, 5, 4,
 5, 6, 2, 0, 3, 8, 7, 0, 4, 9, 1,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 1, 5, 7, 0, 8, 3, 4, 0, 2, 6, 9,
 4, 9, 1, 0, 6, 7, 8, 0, 5, 2, 3,
 7, 8, 5, 0, 9, 1, 2, 0, 3, 4, 6,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 3, 4, 9, 0, 7, 2, 6, 0, 8, 1, 5,
 8, 3, 6, 0, 5, 4, 1, 0, 9, 7, 2,
 2, 1, 3, 0, 4, 9, 5, 0, 6]

[6, 2, 4, 1, 5, 9, 7, 3, 8,
 9, 7, 8, 2, 6, 3, 1, 5, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 9, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 1, 2, 3, 4, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7]

listaB = [5, 4, 3, 0, 7, 6, 9, 0, 8, 2, 1]

lista[len(lista)-1:-1:11]
"""
# Primeiro monta uma lista com os indices a Matriz a fim de encontrar o quadrante selecionado

listaMatriz =[6, 2, 4, 1, 5, 9, 7, 3, 8,
 9, 7, 8, 2, 6, 3, 1, 5, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 9, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 1, 2, 3, 4, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7]


"""
 6, 2, 4, 1, 5, 9, 7, 3, 8,
 9, 7, 8, 2, 6, 3, 1, 5, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 9, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 1, 2, 3, 4, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7
"""

posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]
inIndex = None
indexMatriz = 33

quadMontado = []
y = 0

for i in posFix:
	z = 0
	validarQuad =[]
	for x in range(9):

		validarQuad.append(i+z)
		z += 1
		y += 1

		if y > 2:
			y = 0
			z += 6

	if indexMatriz in validarQuad:
		inIndex = i
		break
z = 0
print validarQuad
for i in range(3):
	print "VALORES ", listaMatriz[inIndex+z:inIndex+3+z]
	z += 9
	#x += 11
"""		if y == 3:
	validarQuad.extend(listaMatriz[i+z:i+z+3])
			y = 0
			x += 8

		montarQuad.append(i+x)
		
		y += 1

	if 4 in montarQuad:
		vaux = False
	else:
		montarQuad = []
		x -= 11
		y = 0

	print montarQuad"""
"""	for i in montarQuad:
		print " --- ", i
	#quadMontado.extend(listaMatriz[montarQuad[0]+z:montarQuad[0]+3+z])
	#print "1111 ", listaMatriz[montarQuad[0]+z:montarQuad[0]+3+z]
	#z += 11
print "**************************"
print "index VALUE ", listaMatriz[0]
print montarQuad
print "--------------------------"
print quadMontado
"""
