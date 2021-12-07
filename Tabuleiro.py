class Posicao:
	'''Simula as posições de um tabuleiro de jogo da velha'''
	def __init__(self):
		self.alterou = False
		self.conteudo = "-1"

	def marcar(self, desenho):
		if not self.alterou:
			self.conteudo = desenho
			self.alterou = True
	#def vazio(self):
		#return(not self.alterou)
class Tabuleiro:
	'''Simula um Jogo da Velha comum '''
	p00 = Posicao()
	p01 = Posicao()
	p02 = Posicao()
	p10 = Posicao()
	p11 = Posicao()
	p12 = Posicao()
	p20 = Posicao()
	p21 = Posicao()
	p22 = Posicao()
	def __init__(self):
		#self.jogo = [[Posicao(),Posicao(),Posicao()],[Posicao(),Posicao(),Posicao()],[Posicao(),Posicao(),Posicao()]]
		self.jogo = [[p00,p01,p02],[p10,p11,p12],[p20,p21,p22]]
		self.vencido = False
		self.vencedor = "-1"

	def marcar(self, x, y, conteudo):
		if self.jogo[x][y].alterou == False and self.venceu() == False:
			self.jogo[x][y].marcar(conteudo)
		else:
			if self.vencido == True:
				print("Esse tabuleiro já possui um vencedor ;)")
			else:
				print("Essa casa já está marcada")
	def venceu(self):
		c00 = self.jogo[0][0].conteudo
		c01 = self.jogo[0][1].conteudo
		c02 = self.jogo[0][2].conteudo
		c10 = self.jogo[1][0].conteudo
		c11 = self.jogo[1][1].conteudo
		c12 = self.jogo[1][2].conteudo
		c20 = self.jogo[2][0].conteudo
		c21 = self.jogo[2][1].conteudo
		c22 = self.jogo[2][2].conteudo

		if (c00 != "-1" and c01 != "-1" and c02 != "-1"):
			if (c00 == c01 and c00 == c02):
				self.vencido = True
				self.vencedor = c00
				return(True)
		elif(c10 != "-1" and c11 != "-1" and c12 != "-1"):
			if (c10 == c11 and c00 == c12):
				self.vencido = True
				self.vencedor = c10
				return(True)
		elif(c20 != "-1" and c21 != "-1" and c22 != "-1"):
			if (c20 == c21 and c20 == c22):
				self.vencido = True
				self.vencedor = c20
				return(True)

		elif(c00 != "-1" and c10 != "-1" and c20 != "-1"):
			if (c00 == c10 and c00 == c20):
				self.vencido = True
				self.vencedor = c00
				return(True)
		elif(c01 != "-1" and c11 != "-1" and c21 != "-1"):
			if (c01 == c11 and c01 == c21):
				self.vencido = True
				self.vencedor = c01
				return(True)
		elif(c02 != "-1" and c12 != "-1" and c22 != "-1"):
			if (c02 == c12 and c02 == c22):
				self.vencido = True
				self.vencedor = c02
				return(True)
		elif(c00 != "-1" and c11 != "-1" and c22 != "-1"):
			if (c00 == c11 and c00 == c22):
				self.vencido = True
				self.vencedor = c00
				return(True)
		elif(c02 != "-1" and c11 != "-1" and c20 != "-1"):
			if (c02 == c11 and c02 == c20):
				self.vencido = True
				self.vencedor = c02
				return(True)
		else:
		return(False)		
