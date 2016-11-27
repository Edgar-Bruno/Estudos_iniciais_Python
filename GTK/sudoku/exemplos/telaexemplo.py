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
		#self.window.set_size_request(550, 550)

		self.create_widgets()

		self.window.show_all()


	def create_widgets(self):

		self.hbox = gtk.HBox(True, 50)
		self.table = gtk.Table(3,3, gtk.TRUE)


		listaMatriz =[6, 2, 4, 0, 1, 5, 9, 0, 7, 3, 8,
					 9, 7, 8, 0, 2, 6, 3, 0, 1, 5, 4,
					 5, 6, 2, 0, 3, 8, 7, 0, 4, 9, 1,
					 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
					 1, 5, 7, 0, 8, 3, 4, 0, 2, 6, 9,
					 4, 9, 1, 0, 6, 7, 8, 0, 5, 2, 3,
					 7, 8, 5, 0, 9, 1, 2, 0, 3, 4, 6,
					 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
					 3, 4, 9, 0, 7, 2, 6, 0, 8, 1, 5,
					 8, 3, 6, 0, 5, 4, 1, 0, 9, 7, 2,
					 2, 1, 3, 0, 4, 9, 5, 0, 6, 8, 7]

		#print listaMatriz
		x = 0
		y = 0

		posFix = [0, 4 , 8 , 44, 48, 52, 88, 92, 96]



		for i in posFix:
			self.table_b = gtk.Table(3,3, gtk.TRUE)
			self.frame = gtk.Frame()
	
			xx = 0
			yy = 0

			#monta o quadrante
			quadMontado = []

			z = 0
			for iq in range(3):
				quadMontado.extend(listaMatriz[i+z:i+3+z])
				
				z += 11

			print quadMontado

			for ii in quadMontado:
				#var = "[%d, %d]" % (i, ii)
				
				self.button = gtk.Button(str(ii))
				self.table_b.attach(self.button, xx, xx+1, yy, yy+1)

				xx += 1
				if xx > 2:
					xx = 0
					yy += 1

			self.frame.add(self.table_b)
			self.table.attach(self.frame, x, x+1, y, y+1,xpadding=3, ypadding=3)
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
