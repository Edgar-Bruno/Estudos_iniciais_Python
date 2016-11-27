#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading, gtk,\
pygtk, commands, subprocess,\
urllib2, os, threading, time, gobject, pango

pygtk.require('2.0')

class  ediThread(threading.Thread):
	"""docstring for  ediThread"""
	def __init__(self, mainviewEdi):
		threading.Thread.__init__(self)
		self.mainviewEdi = mainviewEdi

	def run(self):
		self.work_complete = False
		self.amount_completed = 0
		gobject.timeout_add(1, self.ativar_barra)

		for i in range(100):
			time.sleep(0.15)
			self.amount_completed += .01

		self.work_complete = True

	def ativar_barra(self):
		print self.amount_completed
		self.mainviewEdi.barra_progresso.set_fraction(self.amount_completed)
		self.mainviewEdi.textoLabel.set_text("Valor da atualização %f" % self.amount_completed)

		if self.work_complete:
			self.mainviewEdi.barra_progresso.set_text("Completo")

		else:
			self.mainviewEdi.barra_progresso.set_text("%d%%" % (self.amount_completed * 100))
			#self.mainviewEdi.textoLabel.set_text("FIM DO barra_progresso")

		return not self.work_complete
	

class BaseY:

    
	def destroy(self, widget, data=None):
		print "Voce saiu do programa!!!"
		gtk.main_quit()

	def esconder(self, widget):
		print "Ola Edgar !!!"

		self.botao.hide()
		self.textoLabel.modify_font(pango.FontDescription("Ubuntu 5 bold"))
		self.textoLabel.set_text("O Botao para sair esta\n ESCONDIDO")
		self.textoLabel.set_tooltip_text("Esse e o texo do botao\n ESCONDER")

		self.janelinha.set_title("Titulo do programinha ESCONDER")
		os.system("gedit")

	def exibir(self, widget):
		print "Ola Vivi !!!"
		self.botao.show()

		self.textoLabel.set_text("O Botao para sair esta ESCONDIDO")

		self.textoLabel.set_tooltip_text("Esse e o texo do botao MOSTRAR")

		self.janelinha.set_title("Titulo do programinha EXIBIR")

	def textMudar(self, widget):
		#self.textoLabel.set_text("A entrada foi mudada")
		#var = subprocess.call(['ls']) #Aqui será exibido  a saida do comando [0] =sem erros
		#self.textoLabel.set_text(str(check_output(['ls','../'])))
		
		#self.textMudar.set_tooltip_text("Digite o que voce quiser aqui")
		var = "edgarar"
		print var
		self.textoLabel.set_text(str(var))



	def limparTXT(self, widget):
		self.textoEntrada.set_text("")
	
		os.system("apt-get -y purge gedit")
		#teste = popen("sudo apt-get purge gedit")

	def comboBox_text(self, widget):
		self.textoEntrada.set_text(widget.get_active_text())

	def add_comboBOX(self, widget):
		self.comboBox.append_text(self.textoEntrada.get_text())

	def add_comboBOXb(self, widget):
		print("ENTER  apertado")
		self.textoLabel.set_text("Foi Adicionado um valor no comboBox com ENTER :D")
		self.comboBox.append_text(self.entradaProges.get_text())
		time.sleep(0.25)
		self.entradaProges.set_text("")


	def baixar_img(self, widget):
		
		figura = urllib2.urlopen('http://all.hu/tux.jpg')
		img = open("salvar.png", "w")
		img.write(figura.read())
		img.close()
		os.system("apt-get -y install gedit")

	def infoSobre(self, widget):
		self.barra_progresso.set_text("Virginia Bruno")

		sobre = gtk.AboutDialog()
		sobre.set_program_name("Meu Primeiro Programa")
		sobre.set_version("0.0.1")
		sobre.set_copyright("(c) EDi-Rx")
		sobre.set_comments("Esse é meu primeiro programa GTK em Python")
		sobre.set_website("http://edgar.com")
		sobre.set_logo(gtk.gdk.pixbuf_new_from_file("../camera_icon.jpg"))
		sobre.run()
		sobre.destroy()

	def ativar(self, *args):
		print "Clicado no botão ativar"

		self.barra_progresso.set_fraction(0)
		worker = ediThread(self)
		worker.start()
		self.textoLabel.set_text("Foi Adicionado um valor no comboBox com ENTER :D")

	

	def __init__ (self):
		#self.aquiSanji = aquiSanji
		self.janelinha = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.janelinha.set_position(gtk.WIN_POS_CENTER)
		self.janelinha.set_size_request(500, 500)

		self.janelinha.set_title("Titulo do programinha INICIO")

		self.botaoH =gtk.ColorButton(color=gtk.gdk.Color(5,5,0))
		self.botaoH.set_tooltip_text("Clique e escolha uma cor")

		self.botaoG = gtk.Button("Ativar")
		self.botaoG.connect("clicked", self.ativar)
		self.botaoG.set_tooltip_text("Ativador da Progress Bar")

		self.botaoF = gtk.Button("Baixar")
		self.botaoF.connect('clicked', self.baixar_img)
		self.botaoF.set_tooltip_text("Aqui será baixado uma imagem de um endereço estático - http://all.hu/tux.jpg")

		#self.janelinha.set_tooltip_text("este e o meu programinha\nEdgar\nBruno\nVirginia")
		self.botaoE = gtk.Button("Sobre")
		self.botaoE.connect("clicked", self.infoSobre)
		self.botaoE.set_tooltip_text("As informações do programa")

		self.botaoD = gtk.Button("ADD ComboBox")
		self.botaoD.connect("clicked", self.add_comboBOX)
		self.botaoD.set_tooltip_text("Aqui sera adicionado\n o texto da entrada\nno comboBox")

		self.botaoC = gtk.Button("Limpar TXT")
		self.botaoC.connect("clicked", self.limparTXT)
		self.botaoC.set_tooltip_text("Aqui limpa o texto digitado")

		self.botaoB = gtk.Button("MOSTRAR")
		self.botaoB.connect("clicked", self.exibir)
		self.botaoB.set_tooltip_text("Mostrar o BOTAO SAIR!!!")

		self.botaoA = gtk.Button("ESCONDER")
		self.botaoA.connect("clicked", self.esconder)
		self.botaoA.set_tooltip_text("Esconder o BOTAO SAIR!!!")

		self.botao = gtk.Button("SAIR")
		self.botao.connect("clicked", self.destroy)
		self.botao.set_tooltip_text("Esse botao fechara o programa !!!")

		self.textoLabel = gtk.Label("TEXTO DA LABEL")
		self.textoLabel.set_tooltip_text("Esse e o texo da label")

		self.textoEntrada = gtk.Entry()
		self.textoEntrada.connect("changed", self.textMudar)

		self.entradaProges = gtk.Entry()
		self.entradaProges.connect("activate", self.add_comboBOXb)
	

		self.comboBox = gtk.combo_box_entry_new_text()
		self.comboBox.connect("changed", self.comboBox_text)
		self.comboBox.append_text("Algum texto 0")
		self.comboBox.set_tooltip_text("Aqui e a opcao do texto 0")
		self.comboBox.append_text("Algum texto 1")
		self.comboBox.append_text("Algum texto 3")
		
		dialog = gtk.FileChooserDialog("EScolha uma imagem",
			None, gtk.FILE_CHOOSER_ACTION_OPEN,
			(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
			gtk.STOCK_OPEN, gtk.RESPONSE_OK))

		dialog.set_default_response(gtk.RESPONSE_OK)
		filter = gtk.FileFilter()
		filter.set_name("IMAGEM_EDI")
		filter.add_mime_type("image/png")
		filter.add_mime_type("imagem/jpeg")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		dialog.add_filter(filter)

		response = dialog.run()

		if response == gtk.RESPONSE_OK:
			self.imagemPix = gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
			self.imagemPix = self.imagemPix.scale_simple(300,200, gtk.gdk.INTERP_BILINEAR)
			self.imagemEDi = gtk.image_new_from_pixbuf(self.imagemPix)

		elif response == gtk.RESPONSE_CANCEL:
			print "Nenhum arquivo foi  selecionado"
			raise SystemExit

		dialog.destroy()


		#varz = 0.5

		self.barra_progresso = gtk.ProgressBar()
		#self.barra_progresso.set_fraction(varz) # Aqui é feita a atualização da barra!!!

		#self.timer = gobject.timeout_add (150, self.progress_timeout)

		self.barra_progresso.set_text("Edgar Bruno")

		#self.imagemPix = gtk.gdk.pixbuf_new_from_file("../Rau.jpg")
		#self.imagemPix = self.imagemPix.scale_simple(300,200, gtk.gdk.INTERP_BILINEAR)
		#self.imagemEDi = gtk.image_new_from_pixbuf(self.imagemPix)

		#self.imagemEDi = gtk.Image()
		#self.imagemEDi.set_from_pixbuf(self.imagemPix)


		#fixed = gtk.Fixed()
		#fixed.put(self.botao, 20, 30)
		#fixed.put(self.botaoA, 20, 60)
		#fixed.put(self.botaoB, 20, 90)

		#self.caixa = gtk.HBox() - Horizontal
		self.caixa = gtk.HBox()
		#self.caixa.pack_start(self.textoLabel)
		self.caixa.pack_start(self.botao)

		self.caixa.pack_start(self.botaoA)
		self.caixa.pack_start(self.botaoB)
		self.caixa.pack_start(self.botaoC)
		
		#self.caixa.pack_start(self.textoEntrada)

		#self.janelinha.add(fixed)


		self.caixaC = gtk.HBox()
		self.caixaC.pack_start(self.botaoF)
		self.caixaC.pack_start(self.botaoE)
		self.caixaC.pack_start(self.botaoD)
		self.caixaC.pack_start(self.textoEntrada)




		self.caixaB = gtk.VBox()

		self.caixaB.pack_start(self.entradaProges)
		self.caixaB.pack_start(self.textoLabel)
		self.caixaB.pack_start(self.caixaC)
		self.caixaB.pack_start(self.caixa)
		#self.caixaB.pack_start(self.textoEntrada)
		self.caixaB.pack_start(self.comboBox)
		self.caixaB.pack_start(self.imagemEDi)
		self.caixaB.pack_start(self.botaoG)
		self.caixaB.pack_start(self.botaoH)
		self.caixaB.pack_start(self.barra_progresso)
		

		self.janelinha.add(self.caixaB)

		self.janelinha.show_all()
		self.janelinha.connect("destroy", self.destroy)

	def main(self):
		gtk.main()

if __name__ == "__main__":
	gobject.threads_init()
	base = BaseY()
	base.main()