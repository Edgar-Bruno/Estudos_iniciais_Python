#!/usr/bin/env python

import pygtk, gtk, gobject
gobject.threads_init()
pygtk.require('2.0')

class Timer():

	def __init__ (self):

		print "Aqui"
		self.x = 0
		self.g = 0
		self.Win()

	def start_t(self, widget):
		self.g = gobject.timeout_add(500, self.count)

	def Win(self):
		print "AQUI"
		self.win = gtk.Window()
		self.win.connect('destroy', lambda w: gtk.main_quit())
		self.box1 = gtk.HBox()
		self.win.add(self.box1)
		
		self.label = gtk.Label(self.x)

		self.button = gtk.Button("Inicio")
		self.button.connect("clicked", self.start_t)
		

		self.box1.pack_start(self.label)
		self.box1.pack_start(self.button)

		self.win.show_all()

	def count(self):
		self.x += 1
		self.label.set_text(str(self.x))
		print "------ ", self.x

		# PARA funcionar é necessário retornar Verdade
		return True

def main():
	gtk.main()

if __name__=="__main__":
	App = Timer()
	main()