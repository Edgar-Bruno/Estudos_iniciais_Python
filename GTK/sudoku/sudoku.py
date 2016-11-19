#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Projeto de estudo de Python e criar um jogo bem legal.

from random import randint
import gtk

# Função responsável pela sequência de números para criar o jogo 
def criarMatriz():

	vaux = False
	numeroSorteado = None
	listaNumeros = []
	
	while not vaux:
		
		numeroSorteado = randint(1,9)

		if numeroSorteado not in listaNumeros:
			listaNumeros.append(numeroSorteado)
			print listaNumeros
		else:
			print "não"

		if len(listaNumeros) == 9:
			vaux = True


	print listaNumeros
	return listaNumeros

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
    if x > 2:
    	x = 0
    	y += 1

box.pack_start(tableJogo)

#win.show_all()

#gtk.main()