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

		self.create_widgets()

		self.window.show_all()

	def create_widgets(self):

		self.hbox = gtk.HBox(True, 50)
		self.table = gtk.Table(3,3, gtk.TRUE)

		x = 0
		y = 0

		posFix = [0, 4 , 8 , 44, 48, 52, 88, 92, 96]

		listaMatriz =[None]
		s = 0

		while not len(listaMatriz) == 121:
			s += 1
			listaMatriz = self.criarMatriz()

		print "Tentativa -> " ,s



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

	def abscissas(self, listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):
	
		i = indexMatriz

		if not listaNumeros and not listaMatriz:

			while i % 11 != 0:
				i -= 1

			listaNumeros = listaMatriz[i:i+11]

		return numeroSorteado in listaNumeros

	def ordenadas(self, listaMatriz, numeroSorteado, indexListaNumeros):
		# verifica se a ocorrência de números repetidos no eixo Y

		"""if indexListaNumeros == 1:
				
						indexListaNumeros = 0
						
					else:
						indexListaNumeros -= 1"""

		return numeroSorteado in listaMatriz[indexListaNumeros::11]

	def quadrante(self, listaMatriz, numeroSorteado, indexMatriz, listaNumeros=None):

		listaMatrizTMP = listaMatriz + listaNumeros

		posFix = [0, 4 , 8 , 44, 48, 52, 88, 92, 96]
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
					z += 8

			if indexMatriz in validarQuad:
				inIndex = i
				break
		z = 0

		for i in range(3):
			quadMontado.extend(listaMatrizTMP[inIndex+z:inIndex+3+z])
			z += 11

		return numeroSorteado in quadMontado

	def criarMatriz(self):
		# Função responsável pela sequência de números para criar o jogo 

		vaux = False
		vauxV = 0
		vauxH = 0

		numeroSorteado = None
		listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaMatriz seu valor é resetado
		listaMatriz = [] # Recebe todos números da listaNumeros
		quebraLoopInfinito = 0 # Mecanismo para impedir loops infinitos
		resetCriaMatriz = 0 # Mecanismo para "resetar" a um, eventual, loop infinito

		while not vaux:
			
			numeroSorteado = randint(1,9)

			if vauxV == 3:
				# Aqui é criado um 'espaço vertical' entre os 'quatrandes' do jogo
				listaNumeros.append(0)
				vauxV = 0

			if vauxH == 3:
				# Aqui é criado um 'espaço horizontal' entre os 'quatrandes' do jogo
				listaMatriz.extend([0]*11)
				vauxH = 0
			
			checkRepeti =[] # Recebe booleano de repetição ods números no eixo Y e no quadrante
			checkRepeti.append(self.abscissas(listaMatriz, numeroSorteado, len(listaNumeros), listaNumeros))	
			checkRepeti.append(self.ordenadas(listaMatriz, numeroSorteado, len(listaNumeros)))
			checkRepeti.append(self.quadrante(listaMatriz, numeroSorteado, len(listaMatriz) + len(listaNumeros), listaNumeros))

			if True in checkRepeti:
				
				if quebraLoopInfinito == 25:
					listaNumeros = []
					vauxV = 0
					quebraLoopInfinito = 0
					resetCriaMatriz += 1
				
				if resetCriaMatriz == 25:
					vaux = True

				quebraLoopInfinito += 1

			else:

				listaNumeros.append(numeroSorteado)
				vauxV += 1
				quebraLoopInfinito = 0


			if len(listaNumeros) == 11:
				listaMatriz.extend(listaNumeros)
				
				listaNumeros = []
				vauxV = 0
				vauxH += 1

			if len(listaMatriz) is 121:
				# Finzalia o while ao atingir a quantidade de números necessários para criar o jogo
				vaux = True

		return listaMatriz
		
	def main(self):

		gtk.main()

if __name__=="__main__":
	App = Aplicacao()
	App.main()
