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


class Estabanado(Jogador):
    def __init__(self, nome, simbolo, mega_tabuleiro):
        Jogador.__init__(self,nome, simbolo, mega_tabuleiro)
    
    def jogada(self):
        coordenadas = {1: (0,0), 2: (0,1), 3: (0,2), 
                       4: (1,0), 5: (1,1), 6: (1,2),
                       7: (2,0), 8: (2,1), 9: (2,2)}

        tab = random.randint(1, 9)
        coo = random.randint(1, 9)
        
        while (self.joga(coordenadas[tab][0], coordenadas[tab][1], coordenadas[coo][0], coordenadas[coo][1]) < 0):
            tab = random.randint(1, 9)
            coo = random.randint(1, 9)
        