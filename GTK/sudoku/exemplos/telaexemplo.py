#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exemplo de tela para montar o jogo SUDOKU
import pygtk
pygtk.require('2.0')
import gtk

class Aplicacao:

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.set_title("Sudoku")
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.set_size_request(500, 500)

		self.create_widgets()

		self.window.show_all()


	def create_widgets(self):

		self.hbox = gtk.HBox(False, 50)
		self.table = gtk.Table(3,3, gtk.TRUE)

		x = 0
		y = 0

		for i in range(9):
			self.table_b = gtk.Table(2,2, gtk.TRUE)
			self.frame = gtk.Frame()
	
			xx = 0
			yy = 0

			for ii in range(9):
				var = "[%d, %d]" % (i, ii)
				self.button = gtk.Button(str(var))

				self.table_b.attach(self.button, xx, xx+1, yy, yy+1)
				xx += 1
				if xx > 2:
					xx = 0
					yy += 1

			self.frame.add(self.table_b)
			self.table.attach(self.frame, x, x+1, y, y+1,xpadding=1, ypadding=1)
			x += 1
			if x > 2:
				x = 0
				y += 1

		self.hbox.pack_start(self.table, True, False, 50)


		self.window.add(self.hbox)
		
	def main(self):

		gtk.main()

if __name__=="__main__":
	App = Aplicacao()
	App.main()
