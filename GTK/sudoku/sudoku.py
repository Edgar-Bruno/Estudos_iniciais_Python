#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Projeto de estudo de Python e criar um jogo bem legal.

from random import randint
import gtk

def criarMatriz():
	# Função responsável pela sequência de números para criar o jogo 

	vaux = False
	vauxV = 0
	vauxH = 0

	numeroSorteado = None
	listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaMatriz seu valor é resetado
	listaMatriz = [] # Recebe todos números da listaNumeros
	
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
			vauxV += 1

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

x = 0
y = 0

for i in a:
    button = gtk.Button(str(i))

    #button.connect("clicked", click_btn)

    tableJogo.attach(button, x, x+1, y, y+1)

    x += 1
    if x > 10:
    	x = 0
    	y += 1

box.pack_start(tableJogo)

win.show_all()

gtk.main()