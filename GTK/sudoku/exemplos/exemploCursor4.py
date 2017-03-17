#!/usr/bin/env python


import pygtk
pygtk.require('2.0')
import gtk


class Cursor():

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.set_title("Sudoku")
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.set_border_width(10)
		self.window.set_size_request(550, 550)


		self.botaoG = gtk.Button("Ativar")

		event_box = gtk.EventBox()




		#self.botaoG.connect("realize", self.realize_cb)
		
		self.botaoX = gtk.Button("Ativar X")

		self.caixaB = gtk.VBox()

		self.caixaC = gtk.VBox()

		self.caixaC.pack_start(self.botaoX)

		event_box.add(self.botaoG)


		self.caixaB.pack_start(event_box)

		self.caixaB.pack_start(self.caixaC)

		

		self.window.add(self.caixaB)


		event_box.realize()
		event_box.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.CROSS_REVERSE))


		self.window.show_all()

	def realize_cb(self, widget):
   		self.botaoG.window.set_cursor(gtk.gdk.Cursor(gtk.gdk.WATCH))
   		print "AQUI "

	def main(self):

		gtk.main()
		return 0

if __name__=="__main__":
	App = Cursor()
	App.main()