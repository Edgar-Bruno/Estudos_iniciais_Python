#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Exemplo de jogo SUDOKU
from random import randint
import pygtk, gtk, copy, pango, gobject
pygtk.require('2.0')

class ProgressBar(object):

	def __init__(self):

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_resizable(True)

		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_title("Carregar jogo")
		self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		self.window.set_border_width(0)
		vbox = gtk.VBox(False, 5)
		vbox.set_border_width(10)

		self.textoLabel = gtk.Label("TEXTO DA LABEL")

		self.buttonStart = gtk.Button("Start")
		self.buttonStart.connect("clicked", self.ativador)
		self.buttonStart.set_tooltip_text("Gere um novo jogo")
		
		hbox = gtk.HBox(homogeneous=True, spacing=5)
		
		hbox.pack_start(self.buttonStart)
        
		#Cria o alinhamento dos objetos
		align = gtk.Alignment(0.5, 0.9, 0.25, 0)
		alignb = gtk.Alignment(0.7, 0.5, 0, 0)

		align.add(hbox)

		vbox.add(align)
		vbox.pack_start(alignb, False, False, 5)

		# Cria a ProgressBar
		self.pBar = gtk.ProgressBar()
		self.pBar.set_text(" ")

		alignb.add(self.pBar)

		
		separator = gtk.HSeparator()
		
		vbox.pack_start(separator, False, False, 0)


		vbox.pack_start(self.textoLabel)

		self.window.add(vbox)

		self.window.show_all()

		self.vaux = False # Flag para evitar loops infinitos

		self.listaSudokuMatrix = None

	def ativador(self, *args):
		self.timer = gobject.timeout_add (1, self.criarMatriz)
		self.buttonStart.set_sensitive(False) # Desabilita botão

	def criarMatriz(self):


		if not self.vaux:

			self.listaNumeros = [] # Cria uma lista com 11 números após, ser inserida em listaSudokuMatrix seu valor é resetado
			self.listaSudokuMatrix = [] # Recebe todos números validos da listaNumeros a fim de gerar a matriz numérica do jogo
			self.quebraLoopInfinito = 0 # Mecanismo para impedir loops infinitos
			self.resetCriaMatriz = 0 # Mecanismo para "resetar" a matriz quando, é, identificado um eventual loop infinito
			self.vaux = True
			self.pBar.set_fraction(0)

		else:

			self.numeroSorteado = randint(1,9)
			self.textoLabel.set_text(str(self.listaNumeros))

			checkRepeti = [] # Recebe booleano de repetição ods números no eixo Y e no quadrante

			checkRepeti.append(SudokuMain.abscissas(self.listaNumeros, len(self.listaNumeros), self.numeroSorteado))
			checkRepeti.append(SudokuMain.ordenadas(self.listaSudokuMatrix, len(self.listaSudokuMatrix) + len(self.listaNumeros), self.numeroSorteado))	
			checkRepeti.append(SudokuMain.quadrante(self.listaSudokuMatrix, len(self.listaSudokuMatrix) + len(self.listaNumeros), self.numeroSorteado, self.listaNumeros))

			if True in checkRepeti:

				if self.quebraLoopInfinito == 20:
					self.listaNumeros = []
					self.quebraLoopInfinito = 0
					self.resetCriaMatriz += 1
				
					if self.resetCriaMatriz == 10:
						self.vaux = False

				self.quebraLoopInfinito += 1
				
			else:
				self.listaNumeros.append(self.numeroSorteado)
				self.quebraLoopInfinito = 0

				#self.addVal = ((len(self.listaSudokuMatrix) + len(self.listaNumeros)) * 0.012345679)
				self.pBar.set_fraction((len(self.listaSudokuMatrix) + len(self.listaNumeros)) * 0.012345679)
				
				if len(self.listaNumeros) == 9:
			
					self.listaSudokuMatrix.extend(self.listaNumeros)
					self.listaNumeros = []

					#raw_input("Press Enter to continue..."

			if len(self.listaSudokuMatrix) == 81:

				AppS = SudokuMain(self.listaSudokuMatrix)
				AppS.main()
				
				return False

		return True

	def main(self):

		gtk.main()
		return 0

class SudokuMain(ProgressBar):

	def __init__(self, progressBar):

		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

		self.window.set_title("Sudoku")
		self.window.connect('destroy', lambda w: gtk.main_quit())
		self.window.set_border_width(10)
		#self.window.set_size_request(550, 550)
		
		# Posições iniciais de cada quadrante do jogo

		self.matrizSudoku = progressBar

		self.matrizSudokuOculta = self.ocutador()

		self.dicObjtos = self.cria_widgets()

		self.window.show_all()

		for i in self.dicObjtos:

			if not self.dicObjtos[i].get_text():
				cursor = gtk.gdk.Cursor(gtk.gdk.HAND2) 

			else:
				cursor = gtk.gdk.Cursor(gtk.gdk.X_CURSOR)
				self.dicObjtos[i].set_tooltip_text("Não clicavel")

			self.dicObjtos[i].window.set_cursor(cursor)
		# Solução para alterar o cursor está na documentação
		# http://faq.pygtk.org/index.py?file=faq05.006.htp&req=edit
		# http://www.pygtk.org/pygtk2reference/class-gdkcursor.html

	def cria_widgets(self):

		self.hbox = gtk.HBox(False, 0)
		self.table = gtk.Table(3,3, gtk.TRUE)

		x = 0
		y = 0

		dicObjtos = {}
		# Dicionário conterá todos os valores para identificar o botão, valor e indice.

		for quadNumero, i in enumerate(self.posFix):

			self.table_b = gtk.Table(3,3, gtk.TRUE)
			self.frame = gtk.Frame()
	
			xx = 0
			yy = 0

			quadMontado = []
			# monta o quadrante

			z = 0

			for iq in range(3):

				for d in range(i+z, i+3+z):
					#print "Indice = %d Valor = %d" % (d, self.matrizSudokuOculta[d])
					# A key do dicionário é o index da matrizSudokuOculta. O Seu valor será o elemento label
					quadMontado.append(d)
					dicObjtos[d] = None

				z += 9
				
			for idNum in quadMontado:

				self.event_box = gtk.EventBox()
				self.label = gtk.Label()

				if quadNumero % 2 == 0:
				
					if idNum % 2 == 0:
						# Cor 1 do fundo clicavel
						color = "#afc6e9"
					else:
						color = "#d7e3f4"
				else:

					if idNum % 2 == 0:

						color = "#A4ACB8"
						# Cor 2 do fundo clicavel
					else:
						color = "#B8C2CF"

				self.event_box.modify_bg(gtk.STATE_NORMAL,
					self.event_box.get_colormap().alloc_color(color))

				attr = pango.AttrList()
				
				if self.matrizSudokuOculta[idNum] == 0:
					
					self.label.set_text("")
					self.event_box.connect("button_press_event", self.click_btn, self.label, idNum)
					size = pango.AttrSize(15000, 0, 1)

				else:
					# Cor da fonte não clicavel

					self.label.set_markup("<b>%s</b>" % str(self.matrizSudokuOculta[idNum]))
					size = pango.AttrSize(20000, 0, 1)

				self.label.set_size_request(40, 40)
				
				attr.insert(size)
				
				self.label.set_attributes(attr)
				
				dicObjtos[idNum] = self.label

				self.event_box.add(self.label)

				self.event_box.set_events(gtk.gdk.BUTTON_PRESS_MASK)

				self.table_b.attach(self.event_box, xx, xx+1, yy, yy+1, xpadding=1, ypadding=1)

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

		return dicObjtos

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
		 	# Essa variável recebe os booleanos de cada metodo referente ao indexMatriz

		 	dicValidador.update(dicAux)

		if True in listaValid:
			dicValidador[indexMatriz] = True

		# Valida a repetição dos números
		for i in dicValidador.keys():
			if dicValidador[i]:
			# Destaca a cor do número repedido
				
				color = "#DF0E0A"
				# self.dicObjtos[i].set_tooltip_text("Repitido")

			else:
			# Cor padrão dos números sem repetições
				color = "#292929"
			
			self.dicObjtos[i].modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse(color))


	@classmethod
	def verificador(cls, keys, values):
		#Verifica a ocorrencia de números repetidos no momento do jogo

		dicVerificador = {} # Key é o index da listaSudokuMatrix, value será True ou False

		dictTMP = dict(zip(keys, values)) # Keys é o index e values é o valor da listaSudokuMatrix 

		for i in dictTMP:
			vTMP = dictTMP[i]	# valor do elemento.
			dictTMP[i] = None 	# Substituição do valor pesquisado

			if vTMP in dictTMP.values():
				dicVerificador[i] = True
			else:
				dicVerificador[i] = False

			dictTMP[i] = vTMP

		return dicVerificador

	@classmethod
	def abscissas(cls, listaSudokuMatrix, indexMatriz, numeroSorteado=None, flag=None):
		# verifica se há ocorrência de números repetidos no eixo X para montar a matriz do jogo
		#lado esquerdo

		i = indexMatriz

		while i % 9 != 0:
			i -= 1

		if flag:
		
			checkRepeti = cls.verificador(range(i, i+9), listaSudokuMatrix[i:i+9])

		else:

			checkRepeti = numeroSorteado in listaSudokuMatrix[i:i+9]

		return checkRepeti

	@classmethod
	def ordenadas(cls, listaSudokuMatrix, indexMatriz, numeroSorteado=None, flag=None):
		# verifica se há ocorrência de números repetidos no eixo Y
		#Sobe

		i = indexMatriz
		while i >= 9:
			i -= 9
		
		if flag:
			# List Comprehensions list = [i+x*9 for x in range(9)]
			checkRepeti = cls.verificador([i+x*9 for x in range(9)], listaSudokuMatrix[i::9])

		else:

			checkRepeti = numeroSorteado in listaSudokuMatrix[i::9]

		return checkRepeti

	@classmethod
	def quadrante(cls, listaSudokuMatrix, indexMatriz, numeroSorteado=None, listaNumeros=None, flag=None):
		# Verifica se há ocorrência de números repetidos no quadrante

		cls.posFix = [0, 3 , 6 , 27, 30, 33, 54, 57, 60]

		if listaNumeros:

			listaSudokuMatrixTMP = listaSudokuMatrix + listaNumeros
		
		else:

			listaSudokuMatrixTMP = listaSudokuMatrix

		inIndex = None
		quadranteValores = []

		y = 0

		for i in cls.posFix:
			z = 0
			quadranteIndex =[]

			for x in range(9):

				quadranteIndex.append(i+z)
				z += 1
				y += 1

				if y > 2:
					y = 0
					z += 6

			if indexMatriz in quadranteIndex:
				inIndex = i
				break
		z = 0

		for i in range(3):
			
			quadranteValores.extend(listaSudokuMatrixTMP[inIndex+z:inIndex+3+z])
			z += 9

		if flag:

			checkRepeti = cls.verificador(quadranteIndex, quadranteValores)
			
		else:

			checkRepeti = numeroSorteado in quadranteValores

		return checkRepeti

	def ocutador(self):
		
		#Função responsável por ocultar os números da matrizSudoku

		listaSudokuMatrixOculta = copy.copy(self.matrizSudoku)

		listaOcultados = []

		while not len(listaOcultados) == 50:
		# Quantidade limite de números ocultados

			ocultar = randint(0,80)

			if not ocultar in listaOcultados:
				listaOcultados.append(ocultar)

				listaSudokuMatrixOculta[ocultar] = 0
		
		return listaSudokuMatrixOculta

	def main(self):
		gtk.main()
		return 0

if __name__=="__main__":
	App = ProgressBar()
	App.main()