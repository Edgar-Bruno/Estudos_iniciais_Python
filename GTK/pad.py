#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Exemplos de utilização do gtk

# referencias
# http://www.pygtk.org/pygtk2reference/class-gtkvbox.html

import gtk

def click_btn(widget):
	num = entry.get_text()
	cnum = widget.get_label()
	entry.set_text(num + cnum)

def click_env(widget):
	print "Discando..." + entry.get_text()

#Cria o objeto win
win = gtk.Window()

#Fecha a janela quando clicar em sair/
win.connect('destroy', lambda w: gtk.main_quit())


box = gtk.VBox(homogeneous=True, spacing=0)
win.add(box)

entry = gtk.Entry()

#Este "False" serve para fixar o campo entry quando a caixa de dialogo for maximizada
box.pack_start(entry, False)

table = gtk.Table(2,2, gtk.TRUE)

a = [1,2,3,4,5,6,7,8,9,"#",0,"*"]

x = 0
y = 0

for i in a:
    button = gtk.Button(str(i))

    button.connect("clicked", click_btn)

    table.attach(button, x, x+1, y, y+1)

    x += 1
    if x > 2:
    	x = 0
    	y += 1

enviar_btn = gtk.Button("ENVIAR")
enviar_btn.connect("clicked", click_env)

box.pack_start(table)
box.pack_start(enviar_btn)


win.show_all()

gtk.main()
