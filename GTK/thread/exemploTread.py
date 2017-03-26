#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk, threading, gobject, time

class  ediThread(threading.Thread):
	"""docstring for Thread"""

	def __init__(self, mainviewEdi):
		threading.Thread.__init__(self)
		self.mainviewEdi = mainviewEdi

	def run(self):
		self.work_complete = False
		self.amount_completed = 0
		gobject.timeout_add(100, self.ativar_barra)

		for i in range(10):
			time.sleep(0.1)
			self.amount_completed += .1

		self.work_complete = True

	def ativar_barra(self):
		print self.amount_completed
		self.mainviewEdi.barra_progresso.set_fraction(self.amount_completed)

		if self.work_complete:
			self.mainviewEdi.barra_progresso.set_text("Completo")

		else:
			self.mainviewEdi.barra_progresso.set_text("%d%%" % (self.amount_completed * 100))

		return not self.work_complete


class Base:

	def __init__(self):
		# Construtor da classe
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_title("Exemplo Tread GTK")

		self.window.set_size_request(250, 200)
		self.window.set_position(gtk.WIN_POS_CENTER)

		self.barra_progresso = gtk.ProgressBar()

		self.buttonx = gtk.Button("Start")

		self.buttonx.connect("clicked", self.ativar)
		self.buttonx.set_tooltip_text("Ativador da Progress Bar")

		self.buttony = gtk.Button("Stop")

		hbox = gtk.HBox(homogeneous=True, spacing=5)
		
		hbox.pack_start(self.buttonx)
		hbox.pack_start(self.buttony)

		align = gtk.Alignment(0.5, 0.9, 0.25, 0)
		alignb = gtk.Alignment(0.5, 0.6, 0, 0.2)
		# http://www.pygtk.org/pygtk2reference/class-gtkalignment.html
		# http://amgcomputing.blogspot.pt/2011/12/pygtk-alignment-class.html

		align.add(hbox)
		alignb.add(self.barra_progresso)

		vbox = gtk.VBox()

		#vbox.pack_start(self.barra_progresso)
		vbox.add(alignb)
		vbox.add(align)

		self.window.add(vbox)

		self.window.show_all()


	def ativar(self, *args):
		print "Clicado no botão ativar"
		self.buttonx.set_sensitive(False) # Desabilita botão
		self.barra_progresso.set_fraction(0)

		worker = ediThread(self, self.contador())
		print "ALI"
		worker.start()

	def contador(self):
		print "aqui"
		return "XXXX"

	def main(self):
		gtk.main()

		
		
if __name__ == "__main__":
	gobject.threads_init()
	base = Base()
	base.main()