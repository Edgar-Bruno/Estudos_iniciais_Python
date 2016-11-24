#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Projeto de estudo de Python e criar um jogo bem legal.

from random import randint
import gtk

def ordenadas(listaMatriz, numeroSorteado, indexListaNumeros):
	# verifica se a ocorrência de números repetidos no eixo Y

	if indexListaNumeros == 1:

		indexListaNumeros = 0
	else:
		indexListaNumeros -= 1

	return numeroSorteado in listaMatriz[indexListaNumeros::11]

def quadrante(listaMatriz, numeroSorteado, indexMatriz, listaNumeros):

	listaMatrizTMP = listaMatriz + listaNumeros[:-1]

	posFix = [0, 4 , 8 , 44, 48, 52, 88, 92, 96]
	inIndex = None
	quadMontado = []
	#indexMatriz = 119

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
				z += 8

		if indexMatriz in validarQuad:
			inIndex = i
			break
	z = 0

	for i in range(3):
		quadMontado.extend(listaMatrizTMP[inIndex+z:inIndex+3+z])
		z += 11

	return numeroSorteado in quadMontado

def criarMatriz():
	# Função responsável pela sequência de números para criar o jogo 

	vaux = False
	vauxV = 0
	vauxH = 0

	numeroSorteado = None
	listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaMatriz seu valor é resetado
	listaMatriz = [] # Recebe todos números da listaNumeros
	quebraLoopInfinito = 0 # Mecanismo para impedir loops infinitos


	while not vaux:
		
		numeroSorteado = randint(1,9)

		if vauxV == 3:
			# Aqui é criado um 'espaço vertical' entre os 'quatrandes' do jogo
			listaNumeros.append(0)
			vauxV = 0

		if vauxH == 3:
			# Aqui é criado um 'espaço horizontal' entre os 'quatrandes' do jogo
			listaMatriz.extend([0]*11)
			vauxH = 0
			
		if numeroSorteado not in listaNumeros:
			# Primeira verificação de repetição dos números no eixo X
			listaNumeros.append(numeroSorteado)
	
			checkRepeti =[] # Recebe booleano de repetição ods números no eixo Y e no quadrante
			checkRepeti.append(ordenadas(listaMatriz, numeroSorteado, len(listaNumeros)))
			checkRepeti.append(quadrante(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros)-1, listaNumeros))

			if True in checkRepeti:

				listaNumeros.remove(listaNumeros[-1])

				if quebraLoopInfinito == 50:
				
					listaNumeros = []
					vauxV = 0
					quebraLoopInfinito = 0
					
				quebraLoopInfinito += 1

			else:

				vauxV += 1
				quebraLoopInfinito = 0

		if len(listaNumeros) == 11:
			listaMatriz.extend(listaNumeros)
			
			listaNumeros = []
			vauxV = 0
			vauxH += 1

		if len(listaMatriz) > 120:
			# Finzalia o while ao atingir a quantidade de números necessários para criar o jogo
			vaux = True

	return listaMatriz

#Cria o objeto win
win = gtk.Window()

#Fecha a janela quando clicar em sair/
win.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox()

win.add(box)

tableJogo = gtk.Table(10,10, gtk.TRUE)

a = criarMatriz()
x = 0
y = 0

for i in a:
    button = gtk.Button(str(i))

    #button.connect("clicked", click_btn)
    if button.get_label() != "0":
     
    	tableJogo.attach(button, x, x+1, y, y+1)

    x += 1
    if x > 10:
    	x = 0
    	y += 1

box.pack_start(tableJogo)

win.show_all()

gtk.main()