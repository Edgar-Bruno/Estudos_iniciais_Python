#!/usr/bin/env python

import time, gtk 
from threading import Thread, Event 
  
gtk.gdk.threads_init() # initialize threads right away 

class cdProgressBar(Thread): 
	def __init__(self, time = 10): 
		Thread.__init__(self)
		self.time = self.tot_time = time 
		self.builder = gtk.Builder()
		self.builder.add_from_file('progressbar_countdown.glade')
		self.window = self.builder.get_object('cd_window') 
		self.progressbar = self.builder.get_object('cd_progressbar')
		self.set_progressbar()

		
         # threading
        cself.unpause = Event()
        self.restart = False 
        self.setDaemon(True) # stop the thread on exit

	def main(self):
		self.window.show_all() 
		self.start() # start the thread 
		gtk.main() 
        
	def quit(self, widget, data = None): 
		gtk.main_quit() 
        
	def startbutton_clicked(self, widget, data = None): 
		if not self.unpause.isSet(): 
			self.unpause.set() 
		self.restart = True 
        
	def pausebutton_clicked(self, widget, data = None): 
		if self.unpause.isSet(): 
			self.unpause.clear() # pause the countdown timer 
		else: 
			self.unpause.set() 
            
	def set_progressbar(self): 
		self.progressbar.set_text(str(self.time)) 
		self.progressbar.set_fraction(self.time/float(self.tot_time)) 
         
	def run(self): 
		while True: 
			self.unpause.wait() # wait the self.unpause.isSet() 
			if self.restart: 
				self.time = self.tot_time 
				self.restart = False 
			self.set_progressbar()
			time.sleep(1) 
			if self.time != 0: 
				self.time -= 1 
             
cd_window = cdProgressBar() 
cd_window.main()    