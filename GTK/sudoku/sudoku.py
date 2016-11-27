#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Projeto de estudo de Python e criar um jogo bem legal.

from random import randint
import gtk, os

def abscissas(listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):

	i = indexMatriz

	if not listaNumeros and not listaMatriz:

		while i % 11 != 0:
			i -= 1

		listaNumeros = listaMatriz[i:i+11]

	return numeroSorteado in listaNumeros

def ordenadas(listaMatriz, numeroSorteado, indexListaNumeros):
	# verifica se a ocorrência de números repetidos no eixo Y

	"""if indexListaNumeros == 1:
			
					indexListaNumeros = 0
					
				else:
					indexListaNumeros -= 1"""

	return numeroSorteado in listaMatriz[indexListaNumeros::11]

def quadrante(listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):

	listaMatrizTMP = listaMatriz + listaNumeros

	posFix = [0, 4 , 8 , 44, 48, 52, 88, 92, 96]
	inIndex = None
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
	resetCriaMatriz = 0 # Mecanismo para "resetar" a um, eventual, loop infinito

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
		
		checkRepeti =[] # Recebe booleano de repetição ods números no eixo Y e no quadrante
		checkRepeti.append(abscissas(listaMatriz, numeroSorteado, len(listaNumeros), listaNumeros))	
		checkRepeti.append(ordenadas(listaMatriz, numeroSorteado, len(listaNumeros)))
		checkRepeti.append(quadrante(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros), listaNumeros))

		if True in checkRepeti:
			
			if quebraLoopInfinito == 25:
				listaNumeros = []
				vauxV = 0
				quebraLoopInfinito = 0
				resetCriaMatriz += 1
			
			if resetCriaMatriz == 25:
				vaux = True

			quebraLoopInfinito += 1

		else:

			listaNumeros.append(numeroSorteado)
			vauxV += 1
			quebraLoopInfinito = 0


		if len(listaNumeros) == 11:
			listaMatriz.extend(listaNumeros)
			
			listaNumeros = []
			vauxV = 0
			vauxH += 1

		if len(listaMatriz) is 121:
			# Finzalia o while ao atingir a quantidade de números necessários para criar o jogo
			vaux = True

	return listaMatriz

#Cria o objeto win
win = gtk.Window()

#Fecha a janela quando clicar em sair/
win.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox()

win.add(box)

tableJogo = gtk.Table(10,10)

a =[None]
s = 0

while not len(a) == 121:
	s += 1
	a = criarMatriz()

print "Tentativa -> " ,s

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