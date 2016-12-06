#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Verificação de repetição no eixo das abscissas

indexMatriz =  46 # Index da matriz passado no click

i = indexMatriz

dicAbscissas = {} # Key é o index da listaMatriz, value é o existe ou não

listaMatriz = [6, 2, 4, 1, 5, 9, 7, 6, 8,
 9, 7, 8, 2, 6, 3, 1, 9, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 9, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 7, 2, 3, 7, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7]


while i % 9 != 0: # Encontra o primeiro número index da linha
		i -= 1

listaMatriz[indexMatriz] = 1

listaAbscissasTMP = listaMatriz[i:i+9] # lista da linha pesquisada. Index inicial = 0


print listaAbscissasTMP
print "------------------------"
for ii, indexO in enumerate(range(i, i+9)):
# Verifica se há outras repetições na linha
	vaux = listaAbscissasTMP[ii]	# valor do elemento a conferido mais de uma repetição
	listaAbscissasTMP[ii] = None	# Substituição do valor pesquisado
				
	print listaAbscissasTMP

	if vaux in listaAbscissasTMP:
		dicAbscissas[indexO] = True

	else:

		dicAbscissas[indexO] = False

	#raw_input("Press Enter to continue...")
	listaAbscissasTMP[ii] = vaux # Retorna o valor original
print "---------------------"
print dicAbscissas.values()