import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *
from classes.MegaJogoDaVelha import *
import random

def main():
    bv = "Bem-vinde ao Mega Jogo da Velha!\n\nO Tabuleiro sera mapeado da seguinte forma:\n(+=====+)\n||1|2|3||\n||4|5|6||\n||7|8|9||\n(+=====+)"

    opcoes_de_jogo = "Agora, escolha seus dois jogadores entre as opcoes: Humano, Estabanado, ComeCru"

    tudo_pronto = "Tudo pronto! O jogo sera iniciado. A cada 9 turnos, o jogo podera ser recomecado, mantendo as opcoes de jogadores, ou finalizado, para terminar o programa."

    print(f"{bv}\n")
    print(f"{opcoes_de_jogo}\n")
    nome1 = input("Nome do Jogador 1: ")
    tipo1 = input("Tipo do Jogador 1: ")
    print()
    nome2 = input("Nome do Jogador 2: ")
    tipo2 = input("Tipo do Jogador 2: ")
    print(f"{tudo_pronto}\n")
    mjv = Jogo(tipo1, nome1, tipo2, nome2)
    mjv.jogar()
    
if __name__ == "__main__":
    main()

