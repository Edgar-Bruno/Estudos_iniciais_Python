#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Verificação de repetição no eixo das abscissas

indexMatriz =  46 # Index da matriz passado no click

i = indexMatriz

dicOrdenadas = {} # Key é o index da listaMatriz, value é o existe ou não

listaMatriz = [6, 2, 4, 1, 5, 9, 7, 6, 8,
 9, 7, 8, 2, 6, 3, 1, 9, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 1, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 7, 2, 3, 7, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7]

"""
[6, 2, 4, 1, 5, 9, 7, 6, 8,
 9, 7, 8, 2, 6, 3, 1, 9, 4,
 5, 6, 2, 3, 8, 7, 4, 9, 1,
 1, 5, 7, 8, 3, 4, 2, 6, 9,
 4, 9, 1, 6, 7, 8, 5, 2, 3,
 7, 8, 5, 9, 7, 2, 3, 7, 6,
 3, 4, 9, 7, 2, 6, 8, 1, 5,
 8, 3, 6, 5, 4, 1, 9, 7, 2,
 2, 1, 3, 4, 9, 5, 6, 8, 7]
 """

i = indexMatriz

while i >= 9:
	i -= 9

listaOrdenadasTMP = listaMatriz[i::9] # lista da linha pesquisada. Index inicial = 0

print listaOrdenadasTMP
print "------------------------ "

for ii in range(9):
	vaux = listaOrdenadasTMP[ii]
	listaOrdenadasTMP[ii] = None

	print listaOrdenadasTMP
	if vaux in listaOrdenadasTMP:
		dicOrdenadas[i] = True

	else:

		dicOrdenadas[i] = False

	i += 9

	listaOrdenadasTMP[ii] = vaux # Retorna o valor original

print dicOrdenadas
	
dicValid = [True, True, True]

if False in dicValid:
	print "AQUI!!!!! "
print dicValid