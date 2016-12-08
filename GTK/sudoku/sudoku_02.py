#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exemplo de jogo SUDOKU
import pygtk, gtk, copy, pango
from random import randint
pygtk.require('2.0')

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

		#self.dicValores = self.dicionarioValores()

		self.dicValores = self.cria_widgets()

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
					quadMontado.append(d)
					dicValores[d] = None

				z += 9

			for idNum in quadMontado:

				self.event_box = gtk.EventBox()
				
				if idNum % 2 == 0:
					self.event_box.modify_bg(gtk.STATE_NORMAL,
	                            self.event_box.get_colormap().alloc_color("#cccccc"))

				attr = pango.AttrList()
				
				if self.matrizSudokuOculta[idNum] == 0:
					
					self.label = gtk.Label("")
					self.event_box.connect("button_press_event", self.click_btn, self.label, idNum)
					size = pango.AttrSize(18000, 0, 1)

				else:
					
					if idNum % 2 == 0:
						self.event_box.modify_bg(gtk.STATE_NORMAL,
							self.event_box.get_colormap().alloc_color("#c5c5ef"))
					else:
						self.event_box.modify_bg(gtk.STATE_NORMAL,
							self.event_box.get_colormap().alloc_color("#d7d7f4"))

					self.label = gtk.Label()
					self.label.set_markup("<b>%s</b>" % str(self.matrizSudokuOculta[idNum]))
					size = pango.AttrSize(20000, 0, 1)
				
				self.label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#292929'))
				self.label.set_size_request(35, 35)
				

				attr.insert(size)

				self.label.set_attributes(attr)
				
				dicValores[idNum] = self.label

				self.event_box.add(self.label)
				self.event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)



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

		#print dicValores
		return dicValores

	def click_btn(self, widget, event, itemClicado, indexMatriz):

		if itemClicado.get_text() == "":
			checkValor = 0

		else:
			checkValor = int(itemClicado.get_text())

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

		itemClicado.set_text(str(checkValor))
		# Valor exibido no label

		self.matrizSudokuOculta[indexMatriz] = checkValor
		# inclui o novo valor na matriz e esse será verificado posteriormente

		dicValidador = {}

		metodos = ('abscissas', 'ordenadas', 'quadrante')

		listaValid = []

		for i in metodos:
		 # Verifica se o elemento clicado está repedito nos três metodos de validação
		 	dicAux = eval('self.%s(self.matrizSudokuOculta, indexMatriz, flag=True)' % i)

		 	listaValid.append(dicAux[indexMatriz])
		 	# Essa variável recebe a os booleanos de cada metodo referente ao indexMatriz

		 	dicValidador.update(dicAux)

		if True in listaValid:
			dicValidador[indexMatriz] = True

		self.validador(dicValidador)

	def validador(self, dicValid):
		# Verifica eixo X ao jogar
		for i in dicValid.keys():
			if dicValid[i]:
			# Destaca a cor do número repedido
				self.dicValores[i].modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#DF0E0A'))

			else:
				self.dicValores[i].modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse('#292929'))



	def abscissas(self, listaMatriz, indexMatriz, numeroSorteado=None, flag=None):
		# verifica se há ocorrência de números repetidos no eixo X
		#lado esquedo

		i = indexMatriz

		while i % 9 != 0:
			i -= 1

		if flag:
		# Verificação de há repetição de um número em mais de uma vez
			dicAbscissas = {} # Key é o index da listaMatriz, value será True ou False

			listaAbscissasTMP = listaMatriz[i:i+9] # lista da linha pesquisada. Index inicial = 0

			for ii, indexO in enumerate(range(i, i+9)):
			# Verifica se há outras repetições na linha
				vaux = listaAbscissasTMP[ii]	# valor do elemento a conferido mais de uma repetição
				listaAbscissasTMP[ii] = None	# Substituição do valor pesquisado
							
				if vaux in listaAbscissasTMP:
					dicAbscissas[indexO] = True

				else:

					dicAbscissas[indexO] = False

				listaAbscissasTMP[ii] = vaux # Retorna o valor original

			checkRepeti = dicAbscissas

		else:
		# Função criarMatriz
			checkRepeti = numeroSorteado in listaMatriz[i:i+9]

		return checkRepeti
	
	def ordenadas(self, listaMatriz, indexMatriz, numeroSorteado=None, flag=None):
		# verifica se há ocorrência de números repetidos no eixo Y
		#Sobe

		i = indexMatriz
		while i >= 9:
			i -= 9
		
		if flag:
			dicOrdenadas = {} # Key é o index da listaMatriz, value é o existe ou não
			listaOrdenadasTMP = listaMatriz[i::9] # lista da linha pesquisada. Index inicial = 0
			
			for ii in range(9):

				vaux = listaOrdenadasTMP[ii]
				listaOrdenadasTMP[ii] = None

				if vaux in listaOrdenadasTMP:
					dicOrdenadas[i] = True

				else:

					dicOrdenadas[i] = False

				i += 9

				listaOrdenadasTMP[ii] = vaux # Retorna o valor original

			checkRepeti = dicOrdenadas

		else:

			checkRepeti = numeroSorteado in listaMatriz[i::9]

		return checkRepeti

	def quadrante(self, listaMatriz, indexMatriz, numeroSorteado=None, listaNumeros=None, flag=None):
		# Verifica se há ocorrência de números repetidos no quadrante

		if listaNumeros:

			listaMatrizTMP = listaMatriz + listaNumeros
		
		else:

			listaMatrizTMP = listaMatriz

		print numeroSorteado
		print listaNumeros
		print flag
		

		#raw_input("Press Enter to continue...")
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

		if flag:

			dicQuadrante = {}

			for i, indexO in enumerate(validarQuad):
				vaux = quadMontado[i]
				quadMontado[i] = None

				if vaux in quadMontado:

					dicQuadrante[indexO] = True
				else:
					dicQuadrante[indexO] = False
				
				quadMontado[i] = vaux
		
			checkRepeti = dicQuadrante
		else:

			checkRepeti = numeroSorteado in quadMontado

		return checkRepeti

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
			checkRepeti.append(self.abscissas(listaNumeros, len(listaNumeros), numeroSorteado))
			checkRepeti.append(self.ordenadas(listaMatriz, len(listaMatriz) + len(listaNumeros), numeroSorteado))	
			checkRepeti.append(self.quadrante(listaMatriz, len(listaMatriz) + len(listaNumeros), numeroSorteado, listaNumeros))

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
