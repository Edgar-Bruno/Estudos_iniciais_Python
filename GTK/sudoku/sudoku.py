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

def criarMatriz():
	# Função responsável pela sequência de números para criar o jogo 

	vaux = False
	vauxV = 0
	vauxH = 0

	numeroSorteado = None
	listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaMatriz seu valor é resetado
	listaMatriz = [] # Recebe todos números da listaNumeros
	limpaListaNumeros = 0 # Mecanismo para impedir loops infinitos


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
			vaux = True
			
		if numeroSorteado not in listaNumeros:
			listaNumeros.append(numeroSorteado)
			if not ordenadas(listaMatriz, numeroSorteado, len(listaNumeros)):
				vauxV += 1
				limpaListaNumeros = 0
			else:
				listaNumeros.remove(listaNumeros[-1])
				if limpaListaNumeros == 20:
					listaNumeros = []
					vauxV = 0
				limpaListaNumeros += 1
				print " %d  -> %d " % (limpaListaNumeros, numeroSorteado)

		if len(listaNumeros) == 11:
			listaMatriz.extend(listaNumeros)
			print listaNumeros
			listaNumeros = []
			vauxV = 0
			vauxH += 1

	return listaMatriz

#Cria o objeto win
win = gtk.Window()

#Fecha a janela quando clicar em sair/
win.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox()

win.add(box)

tableJogo = gtk.Table(10,10, gtk.TRUE)


a = criarMatriz()

"""a = [8, 9, 6, 0, 5, 3, 1, 0, 7, 2, 4,
3, 4, 7, 0, 8, 9, 6, 0, 2, 5, 1,
2, 3, 8, 0, 5, 9, 6, 0, 1, 4, 7,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
5, 2, 6, 0, 3, 1, 7, 0, 9, 8, 4,
2, 4, 3, 0, 1, 9, 5, 0, 8, 7, 6,
9, 2, 5, 0, 3, 6, 4, 0, 8, 1, 7,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
8, 2, 5, 0, 6, 9, 3, 0, 1, 4, 7,
2, 3, 8, 0, 7, 1, 6, 0, 5, 9, 4,
5, 4, 3, 0, 7, 6, 9, 0, 8, 2, 1]"""

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