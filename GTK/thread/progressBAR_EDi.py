#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk, gobject

class ProgressBar:

	def __init__(self):

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_resizable(True)

		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_title("ProgressBar")
		self.window.set_border_width(0)
		vbox = gtk.VBox(False, 5)
		vbox.set_border_width(10)

		self.buttonx = gtk.Button("Start")
		self.buttonx.connect("clicked", self.ativar)
		self.buttonx.set_tooltip_text("Ativador da Progress Bar")
		
		hbox = gtk.HBox(homogeneous=True, spacing=5)
		
		hbox.pack_start(self.buttonx)
        
		# Create a centering alignment object
		align = gtk.Alignment(0.5, 0.9, 0.25, 0)

		alignb = gtk.Alignment(0.7, 0.5, 0, 0)

		align.add(hbox)

		vbox.add(align)
		vbox.pack_start(alignb, False, False, 5)


		# Create the ProgressBar
		self.pbar = gtk.ProgressBar()
		self.pbar.set_text("EXEMPLO")

		alignb.add(self.pbar)

		self.window.add(vbox)
		
		separator = gtk.HSeparator()
		vbox.pack_start(separator, False, False, 0)

		self.window.show_all()

		self.x = 5

	# Update the value of the progress bar so that we get
	# some movement
	def progress_timeout(self, pbobj):

		print "ccc ",self.__dict__
		# Calculate the value of the progress bar using the
		# value range set in the adjustment object
		new_val = pbobj.pbar.get_fraction() + 0.1
		if new_val > 1.0:
			new_val = 0
			return False
		else:
			print B.b1(self.x) # => 'Hello from class A'
			self.x  = B.b1(self.x)
			print "----", new_val
		# Set the new value

		pbobj.pbar.set_text(str(new_val))
		pbobj.pbar.set_fraction(new_val)

		"""if self.x:
									print "SIM"
									print self.incrementador()
						
								else:
									print "Não"
									print self.incrementador()"""

		# As this is a timeout function, return TRUE so that it
		# continues to get called
		return True

	def ativar(self, *args):
		# Add a timer callback to update the value of the progress bar
		self.timer = gobject.timeout_add (100, self.progress_timeout, self)

		self.window.set_size_request(50, 200)

	def main(self):
		gtk.main()
		return 0

class B(object):
	"""docstring for Exe"""
	@classmethod
	def b1(self, XXX):
		print "A ", XXX
		XXX += 100

		XXX += self.xyx()

		return XXX

	@classmethod
	def xyx(self):

		zz = 7
		print "AUI"
		return zz
		

if __name__ == "__main__":
	base = ProgressBar()
	base.main()