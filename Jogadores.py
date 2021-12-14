from Tabuleiro import *
from Megatabuleiro import *
import random

class Jogador:
    ''' Simulação de alguns jogadores ''' 
    def __init__(self, nome, simbolo, mega_tabuleiro):
        self.nome = nome
        self.simbolo = simbolo
        self.mega_tabuleiro = mega_tabuleiro

    def joga(self, a, b, x, y):
        self.mega_tabuleiro.mega_marcar(a, b, x, y, self.simbolo)

class Humano(Jogador):
    def __init__(self, nome, simbolo, mega_tabuleiro):
        Jogador.__init__(self,nome, simbolo, mega_tabuleiro)
        
    def jogada(self):
        coordenadas = {1: (0,0), 2: (0,1), 3: (0,2), 
                       4: (1,0), 5: (1,1), 6: (1,2),
                       7: (2,0), 8: (2,1), 9: (2,2)}
        
        tab = int(input("Em qual tabuleiro será a jogada? "))
        coo = int(input("Qual a posição da jogada no mini tabuleiro? "))
        print()
        
        self.joga(coordenadas[tab][0], coordenadas[tab][1], coordenadas[coo][0], coordenadas[coo][1])
        # checar se é válida


class Estabanado(Jogador):
    def __init__(self, nome, simbolo, mega_tabuleiro):
        Jogador.__init__(self,nome, simbolo, mega_tabuleiro)
    
    def jogada(self):
        coordenadas = {(0,0): 1, (0,1): 2, (0,2): 3,
                       (1,0): 4, (1,1): 5, (1,2): 6,
                       (2,0): 7, (2,1): 8, (2,2): 9}
        
        # Encontrar mini tabuleiros válidos
        jogoMega = self.mega_tabuleiro.jogo
        livreGrande = []
        for a in range(3):
            for b in range(3):
                if not jogoMega[a][b].alterou:
                    livreGrande.append((a,b))
        tab = random.randint(0, len(livreGrande)-1)
        a, b = livreGrande[tab]
        # Encontrar posições disponíveis do mini tabuleiro sorteado.
        tabSorteado = self.mega_tabuleiro.jogao[a][b]
        livreMicro = []
        for x in range(3):
            for y in range(3):
                if not tabSorteado.jogo[x][y].alterou:
                    livreMicro.append((x,y))
        coo = random.randint(0, len(livreMicro)-1)
        x, y = livreMicro[coo]

        print(f"O jogador {self.nome} jogará no tabuleiro {coordenadas[(a,b)]} na posição {coordenadas[(x,y)]}: ")
        print()
        self.joga(a, b, x, y)

class ComeCru(Jogador):
    def __init__(self, nome, simbolo, mega_tabuleiro):
        Jogador.__init__(self,nome, simbolo, mega_tabuleiro)

    def jogada(self):
        c00 = self.mega_tabuleiro.jogao[0][0].jogo
        c01 = self.mega_tabuleiro.jogao[0][1].jogo
        c02 = self.mega_tabuleiro.jogao[0][2].jogo 
        c10 = self.mega_tabuleiro.jogao[1][0].jogo
        c11 = self.mega_tabuleiro.jogao[1][1].jogo
        c12 = self.mega_tabuleiro.jogao[1][2].jogo
        c20 = self.mega_tabuleiro.jogao[2][0].jogo
        c21 = self.mega_tabuleiro.jogao[2][1].jogo
        c22 = self.mega_tabuleiro.jogao[2][2].jogo
        
        tabzao = [[c00,c01,c02], 
                  [c10,c11,c12],
                  [c20,c21,c22]]

        coordenadas = {(0,0): 1, (0,1): 2, (0,2): 3,
                       (1,0): 4, (1,1): 5, (1,2): 6,
                       (2,0): 7, (2,1): 8, (2,2): 9}

        for i in range(3):
            for j in range(3):
                for a in range(3):
                    for b in range(3):
                        if not tabzao[i][a][j][b].alterou:
                            print(f"O jogador {self.nome} jogará no tabuleiro {coordenadas[(i,a)]} na posição {coordenadas[(j,b)]}: ")
                            print()
                            return self.joga(i, a, j, b)
                    
    
