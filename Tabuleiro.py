import random

class Posicao:
	'''Simula as posições de um tabuleiro de jogo da velha'''
	def __init__(self):
		self.alterou = False
		self.conteudo = " "

	def marcar(self, desenho):
		if not self.alterou:
			self.conteudo = desenho
			self.alterou = True

	#def vazio(self):
	#	return(not self.alterou)

class Tabuleiro:
	'''Simula um Jogo da Velha comum '''
	def __init__(self,nome):
		p00 = Posicao()
		p01 = Posicao()
		p02 = Posicao()
		p10 = Posicao()
		p11 = Posicao()
		p12 = Posicao()
		p20 = Posicao()
		p21 = Posicao()
		p22 = Posicao()
		#self.jogo = [[Posicao(),Posicao(),Posicao()],[Posicao(),Posicao(),Posicao()],[Posicao(),Posicao(),Posicao()]]
		self.jogo = [[p00,p01,p02],[p10,p11,p12],[p20,p21,p22]]
		self.vencido = False
		self.vencedor = " "
		self.nomeTAB = nome

	def marcar(self, x, y, conteudo):
		# self.venceu()
		if not self.jogo[x][y].alterou and not self.vencido:
			self.jogo[x][y].marcar(conteudo)
			self.venceu()
		else:
			if self.vencido == True:
				print("Esse tabuleiro já possui um vencedor ;)")
				return(-1)
			else:
				print("Essa casa já está marcada")
				return(-2)
		
		if self.deu_velha():
			if random.random() >= 0.5:
				self.vencedor = "X"
				self.vencido = True
			else:
				self.vencedor = "O"
				self.vencido = True
			
			print(f"O tabuleiro {self.nomeTAB} deu velha vamos sortear um vencedor")

		if self.vencido:
			if self.vencedor == "X":
				self.jogo[0][0].conteudo = "X"
				self.jogo[0][1].conteudo = " "
				self.jogo[0][2].conteudo = "X"
				self.jogo[1][0].conteudo = " "
				self.jogo[1][1].conteudo = "X"
				self.jogo[1][2].conteudo = " "
				self.jogo[2][0].conteudo = "X"
				self.jogo[2][1].conteudo = " "
				self.jogo[2][2].conteudo = "X"
			
			elif self.vencedor == "O":
				self.jogo[0][0].conteudo = "O"
				self.jogo[0][1].conteudo = "O"
				self.jogo[0][2].conteudo = "O"
				self.jogo[1][0].conteudo = "O"
				self.jogo[1][1].conteudo = " "
				self.jogo[1][2].conteudo = "O"
				self.jogo[2][0].conteudo = "O"
				self.jogo[2][1].conteudo = "O"
				self.jogo[2][2].conteudo = "O"

			print(f"O {self.vencedor} ganhou o tabuleiro {self.nomeTAB}.")
			return(1)
		return(0)

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

		if (c00 != " " and c01 != " " and c02 != " "):
			if (c00 == c01 and c00 == c02):
				self.vencido = True
				self.vencedor = c00
		elif(c10 != " " and c11 != " " and c12 != " "):
			if (c10 == c11 and c10 == c12):
				self.vencido = True
				self.vencedor = c10
		elif(c20 != " " and c21 != " " and c22 != " "):
			if (c20 == c21 and c20 == c22):
				self.vencido = True
				self.vencedor = c20
		elif(c00 != " " and c10 != " " and c20 != " "):
			if (c00 == c10 and c00 == c20):
				self.vencido = True
				self.vencedor = c00
		elif(c01 != " " and c11 != " " and c21 != " "):
			if (c01 == c11 and c01 == c21):
				self.vencido = True
				self.vencedor = c01
		elif(c02 != " " and c12 != " " and c22 != " "):
			if (c02 == c12 and c02 == c22):
				self.vencido = True
				self.vencedor = c02
		elif(c00 != " " and c11 != " " and c22 != " " ):
			if (c00 == c11 and c00 == c22):
				self.vencido = True
				self.vencedor = c00
		elif(c02 != " " and c11 != " " and c20 != " "):
			if (c02 == c11 and c02 == c20):
				self.vencido = True
				self.vencedor = c02
	
	def imprime(self):
		print("(+=====+)")
		for i in range(3):
			print("||", end = "")
			for j in range(3):
				if j !=2:
					print(f"{self.jogo[i][j].conteudo}", end = "|")
				else:
					print(f"{self.jogo[i][j].conteudo}", end = "|")
			print("|")
		print("(+=====+)")

	def deu_velha(self):
		if self.vencido:
			return False

		for i in range(3):
			for j in range(3):
				if not self.jogo[i][j].alterou:
					return(False)
		return True