#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exemplo de jogo SUDOKU
import pygtk, copy
from random import randint
pygtk.require('2.0')
import gtk

class Aplicacao:

	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.set_title("Sudoku")
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.set_border_width(10)
		#self.window.set_size_request(550, 550)

		self.matrizSudoku = self.criarMatriz()

		self.matrizSudokuOculta = self.ocutador()

		self.cria_widgets()

		self.window.show_all()

	def cria_widgets(self):

		self.hbox = gtk.HBox(False, 0)
		self.table = gtk.Table(3,3, gtk.TRUE)

		x = 0
		y = 0

		# Posições iniciais de cada quadrante do jogo
		posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]

		#print self.matrizSudoku

		# Dicionário conterá todos os valores para identificar o botão, valor e indice.
	
		dicValores = {}

		for i in posFix:
			self.table_b = gtk.Table(3,3, gtk.TRUE)
			self.frame = gtk.Frame()
	
			xx = 0
			yy = 0

			#monta o quadrante
			quadMontado = []

			z = 0

			for iq in range(3):

				for d in range(i+z, i+3+z):
					#print "Indice = %d Valor = %d" % (d, self.matrizSudokuOculta[d])
					# A key do dicionário é o index da matrizSudokuOculta. O Seu valor será o elemento label
					dicValores[d] = None
					quadMontado.append(d)

				z += 9

			for idNum in quadMontado:

				self.event_box = gtk.EventBox()
				
				if self.matrizSudokuOculta[idNum] == 0:
					
					self.label = gtk.Label("")
					self.event_box.connect("button_press_event", self.click_btn, dicValores, idNum)

				else:

					self.label = gtk.Label(str(self.matrizSudokuOculta[idNum]))
				
				self.label.set_size_request(35, 35)

				dicValores[idNum] = self.label
				
				self.event_box.add(self.label)
				self.event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)


				if idNum % 2 == 0:
					self.event_box.modify_bg(gtk.STATE_NORMAL,
	                            self.event_box.get_colormap().alloc_color("#D3D3D3"))

				self.table_b.attach(self.event_box, xx, xx+1, yy, yy+1)

				xx += 1
				if xx > 2:
					xx = 0
					yy += 1

			self.frame.add(self.table_b)
			self.table.attach(self.frame, x, x+1, y, y+1, xpadding=2, ypadding=2)

			x += 1
			if x > 2:
				x = 0
				y += 1

		self.hbox.pack_start(self.table, True, False, 50)

		self.window.add(self.hbox)

	def click_btn(self, widget, event, dicValores, indexMatriz):

		if dicValores[indexMatriz].get_text() == "":
			checkValor = 0

		else:
			checkValor = int(dicValores[indexMatriz].get_text())

		if event.button == 1:
			 checkValor += 1
			 if checkValor > 9:
			 	checkValor = 1
			
		#elif event.button == 2:
			#botão do meio
		elif event.button == 3:
			checkValor -= 1
			if checkValor < 1:
				checkValor = 9

		dicValores[indexMatriz].set_text(str(checkValor))

		print self.abscissas(self.matrizSudokuOculta, checkValor, indexMatriz)
	

	def abscissas(self, listaMatriz, numeroSorteado, indexMatriz):
		# verifica se há ocorrência de números repetidos no eixo X
		#lado esquedo

		i = indexMatriz
		
		while i % 9 != 0:
			i -= 1

		return numeroSorteado in listaMatriz[i:i+9]
	
	def ordenadas(self, listaMatriz, numeroSorteado, indexMatriz):
		# verifica se há ocorrência de números repetidos no eixo Y
		#Sobe

		i = indexMatriz
		while i >= 9:
			i -= 9

		return numeroSorteado in listaMatriz[i::9]

	def quadrante(self, listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):
		# Verifica se há ocorrência de números repetidos no quadrante

		listaMatrizTMP = listaMatriz + listaNumeros

		posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]
		inIndex = None
		quadMontado = []

		y = 0

		for i in posFix:
			z = 0
			validarQuad =[]

			for x in range(9):

				validarQuad.append(i+z)
				z += 1
				y += 1

				if y > 2:
					y = 0
					z += 6

			if indexMatriz in validarQuad:
				inIndex = i
				break
		z = 0

		for i in range(3):
			quadMontado.extend(listaMatrizTMP[inIndex+z:inIndex+3+z])

			z += 9

		return numeroSorteado in quadMontado

	def criarMatriz(self):
	
		# Função responsável pela sequência de números para criar o jogo 

		vaux = False

		numeroSorteado = None
		listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaMatriz seu valor é resetado
		listaMatriz = [] # Recebe todos números da listaNumeros
		quebraLoopInfinito = 0 # Mecanismo para impedir loops infinitos
		resetCriaMatriz = 0 # Mecanismo para "resetar" a matriz quando, é, identificado um eventual loop infinito 

		while not vaux:
			
			numeroSorteado = randint(1,9)
	
			checkRepeti =[] # Recebe booleano de repetição ods números no eixo Y e no quadrante
			checkRepeti.append(self.abscissas(listaNumeros, numeroSorteado, len(listaNumeros)))
			checkRepeti.append(self.ordenadas(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros)))	
			checkRepeti.append(self.quadrante(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros), listaNumeros))

			if True in checkRepeti:

				if quebraLoopInfinito == 20:
					listaNumeros = []
					quebraLoopInfinito = 0
					resetCriaMatriz += 1
				
					if resetCriaMatriz == 10:
						vaux = True

				quebraLoopInfinito += 1

			else:

				listaNumeros.append(numeroSorteado)
				quebraLoopInfinito = 0

				if len(listaNumeros) == 9:

					listaMatriz.extend(listaNumeros)
					listaNumeros = []

					if len(listaMatriz) is 81:

						# Finzalia o while ao atingir a quantidade de números necessários para criar o jogo	
						vaux = True

		while not len(listaMatriz) == 81:
		# Faz a segunda conferência da listaMatriz
			listaMatriz = self.criarMatriz()

		return listaMatriz

	def ocutador(self):
		
		#Função responsável por ocultar os números da matrizSudoku

		listaMatrizOculta = copy.copy(self.matrizSudoku)

		listaOcultados = []

		while not len(listaOcultados) == 50:
		# Quantidade limite de números ocultados

			ocultar = randint(0,80)

			if not ocultar in listaOcultados:
				listaOcultados.append(ocultar)

				listaMatrizOculta[ocultar] = 0
		
		return listaMatrizOculta
		
	def main(self):

		gtk.main()

if __name__=="__main__":
	App = Aplicacao()
	App.main()
