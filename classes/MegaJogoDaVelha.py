import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *
import random

class Jogo:
    '''Classe do jogo em si'''
    def __init__(self,jogador1_tipo, jogador1_nome, jogador2_tipo, jogador2_nome,tipo):
        self.tipo = tipo
        self.megaTab = Mega_Tabuleiro()
        if (jogador1_tipo == "ComeCru"):
            self.jogador1 = ComeCru(jogador1_nome,"X",self.megaTab)

        elif (jogador1_tipo == "Estabanado"):
            seed = random.randint(0, 1000000)
            self.jogador1 = Estabanado(jogador1_nome,"X",self.megaTab, seed)
        
        elif(jogador1_tipo == "Humano"):
            self.jogador1 = Humano(jogador1_nome,"X",self.megaTab)         
    
        if (jogador2_tipo == "ComeCru"):
            self.jogador2 = ComeCru(jogador2_nome,"O",self.megaTab)

        elif (jogador2_tipo == "Estabanado"):
            seed = random.randint(0, 1000000)
            self.jogador2 = Estabanado(jogador2_nome,"O", self.megaTab, seed)
        
        elif(jogador2_tipo == "Humano"):
            self.jogador2 = Humano(jogador2_nome,"O",self.megaTab)

    def jogar(self):
        if self.tipo == "Tradicional":
            turno = 1
            opcoes = ""
            self.megaTab.imprimirTotal()
            input()
            while (not self.megaTab.vencido and not self.megaTab.velhado):
                # Perguntar a cada 10 turnos se desejam Resetar ou Finalizar
                if turno % 10 == 0:
                    opcoes = input("Pressione ENTER para próximo turno, ou digite \"RECOMEÇAR\" para recomeçar o jogo, ou \"FINALIZAR\" para terminar o jogo: ")
                    print()
                    if opcoes == "RECOMEÇAR":
                        turno = 1
                        opcoes = ""
                        self.recomecar()
                        self.megaTab.imprimirTotal()
                        print()
                    elif opcoes == "FINALIZAR":
                        break
                if (turno % 2 == 1):
                    # Adiciona pressionar ENTER para ver jogada de jogadores automaticos
                    if turno > 1 and self.jogador2.tipo in {"Estabanado", "ComeCru"} and turno % 10 != 0:
                        input()
                    if self.jogador2.tipo == "Humano":
                        print()
                    #self.megaTab.imprimirTotal()
                    print()
                    print(f"TURNO {turno}: vez de {self.jogador1.nome}")
                    self.jogador1.jogada()
                    self.megaTab.imprimirTotal()
                else:
                    if self.jogador1.tipo in {"Estabanado", "ComeCru"} and turno % 10 != 0:
                        input()
                    if self.jogador1.tipo == "Humano":
                        print()
                    #self.megaTab.imprimirTotal()
                    print()
                    print(f"TURNO {turno}: vez de {self.jogador2.nome}")
                    self.jogador2.jogada()
                    self.megaTab.imprimirTotal()
                turno += 1
            #self.megaTab.imprimirTotal()
        
        elif self.tipo == "Random":
            turno = 1
            opcoes = ""
            self.megaTab.imprimirTotal()
            input()
            while (not self.megaTab.vencido and not self.megaTab.velhado):
                if turno % 10 == 0:
                    opcoes = input("Pressione ENTER para próximo turno, ou digite \"RECOMEÇAR\" para recomeçar o jogo, ou \"FINALIZAR\" para terminar o jogo: ")
                    print()
                    if opcoes == "RECOMEÇAR":
                        turno = 1
                        opcoes = ""
                        self.recomecar()
                        self.megaTab.imprimirTotal()
                        print()
                    elif opcoes == "FINALIZAR":
                        break
                
                if random.random() < 0.5:
                    if turno > 1 and self.jogador2.tipo in {"Estabanado", "ComeCru"} and turno % 10 != 0:
                        input()
                    if self.jogador2.tipo == "Humano":
                        print()
                    #self.megaTab.imprimirTotal()
                    print()
                    print(f"TURNO {turno}: vez de {self.jogador1.nome}")
                    self.jogador1.jogada()
                    self.megaTab.imprimirTotal()
                else:
                    if self.jogador1.tipo in {"Estabanado", "ComeCru"} and turno % 10 != 0:
                        input()
                    if self.jogador1.tipo == "Humano":
                        print()
                    #self.megaTab.imprimirTotal()
                    print()
                    print(f"TURNO {turno}: vez de {self.jogador2.nome}")
                    self.jogador2.jogada()
                    self.megaTab.imprimirTotal()
                turno += 1
    
    def recomecar(self):
        self.__init__(self.jogador1.tipo, self.jogador1.nome, self.jogador2.tipo, self.jogador1.nome)
