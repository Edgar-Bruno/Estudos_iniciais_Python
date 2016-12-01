#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exemplo de tela para montar o jogo SUDOKU
import pygtk
from random import randint
pygtk.require('2.0')
import gtk

class Aplicacao:


	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.set_title("Sudoku")
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		#self.window.set_size_request(550, 550)

		self.cria_widgets()

		self.window.show_all()

	def cria_widgets(self):

		self.hbox = gtk.HBox(True, 50)
		self.table = gtk.Table(3,3, gtk.TRUE)

		x = 0
		y = 0

		posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]

		listaMatriz =[None]
		s = 0

		while not len(listaMatriz) == 81:
			listaMatriz = self.criarMatriz()
			s += 1
			print "Tentativa -> " ,s

		print "*****************"
		#print listaMatriz

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

				#print "Valores de [i = %d, z = %d, iq = %d]" % (i, z, iq)
				#print quadMontado
				for d in range(i+z, i+3+z):
					#print "Indice = %d Valor = %d" % (d, listaMatriz[d])
					dicValores[d] = [listaMatriz[d]]
					quadMontado.append(d)
				z += 9
			
			#print quadMontado

			for ii in quadMontado:
				
				self.button = gtk.Button(str(dicValores[ii][0]))

				self.button.connect("clicked", self.click_btn, dicValores, ii)
				
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

	def click_btn(self, widget, dicValores, id):
		cnum = widget.get_label()
		print "Valor = %d, id = %d" % (dicValores[id][0], id)


	def abscissas(self, listaMatriz, numeroSorteado, indexMatriz):
		# verifica se a ocorrência de números repetidos no eixo X
		#lado esquedo

		i = indexMatriz
		
		while i % 9 != 0:
			i -= 1

		return numeroSorteado in listaMatriz[i:i+9]
	
	def ordenadas(self, listaMatriz, numeroSorteado, indexMatriz):
		# verifica se a ocorrência de números repetidos no eixo Y
		#Sobe

		i = indexMatriz
		while i >= 9:
			i -= 9

		return numeroSorteado in listaMatriz[i::9]

	def quadrante(self, listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):

		listaMatrizTMP = listaMatriz + listaNumeros

		posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]
		inIndex = None
		quadMontado = []

		y = 0

		for i in posFix:
			z = 0
			validarQuad =[]
			for x in range(9):

				#print "AQUI", numeroSorteado
				validarQuad.append(i+z)
				z += 1
				y += 1

				if y > 2:
					y = 0
					z += 6

			#print validarQuad
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
		resetCriaMatriz = 0 # Mecanismo para "resetar" a um, eventual, loop infinito

		while not vaux:
			
			numeroSorteado = randint(1,9)
	
			checkRepeti =[] # Recebe booleano de repetição ods números no eixo Y e no quadrante
			checkRepeti.append(self.abscissas(listaNumeros, numeroSorteado, len(listaNumeros)))
			checkRepeti.append(self.ordenadas(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros)))	
			checkRepeti.append(self.quadrante(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros), listaNumeros))

			#print checkRepeti

			if True in checkRepeti:

				if quebraLoopInfinito == 25:
					listaNumeros = []
					quebraLoopInfinito = 0
					resetCriaMatriz += 1
				
					if resetCriaMatriz == 25:
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

		return listaMatriz
		
	def main(self):

		gtk.main()

if __name__=="__main__":
	App = Aplicacao()
	App.main()
