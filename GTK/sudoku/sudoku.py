#!/usr/bin/env python
# Projeto de estudo de Python e criar um jogo bem legal.

import gtk

# Função responsável pela sequência de números para criar o jogo 
def criarMatriz():

	vaux = False

#Cria o objeto win
win = gtk.Window()

#Fecha a janela quando clicar em sair/
win.connect('destroy', lambda w: gtk.main_quit())

box = gtk.VBox()

win.add(box)

tableJogo = gtk.Table(10,10, gtk.TRUE)



a = makeMatriz()

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

win.show_all()

gtk.main()