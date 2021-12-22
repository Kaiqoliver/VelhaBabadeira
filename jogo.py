import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *
from classes.MegaJogoDaVelha import *
import random

def main():
    bv = "Bem-vinde ao Mega Jogo da Velha!\n\nO Tabuleiro sera mapeado da seguinte forma:\n(+=====+)\n||1|2|3||\n||4|5|6||\n||7|8|9||\n(+=====+)"

    opcoes_de_jogadores = "Agora, escolha seus dois jogadores entre as opcoes: Humano, Estabanado, ComeCru."
    
    tipo_do_jogo = "Agora, escolha uma categoria de jogo: Tradicional ou Random."

    tudo_pronto = "Tudo pronto! O jogo sera iniciado (apos ver cada tabuleiro, pressione ENTER para a jogada). A cada 10 turnos, o jogo podera ser recomeçado, mantendo as opcoes de jogadores, ou finalizado, para terminar o programa."

    print(f"{bv}\n")
    print(f"{opcoes_de_jogadores}\n")
    nome1 = input("Nome do Jogador 1: ")
    tipo1 = input("Tipo do Jogador 1: ")
    while not tipo1 in {"Estabanado", "ComeCru", "Humano"}:
        print("Escolha um tipo de jogador válido")
        tipo1 = input("Tipo do Jogador 1: ")
    print()
    nome2 = input("Nome do Jogador 2: ")
    tipo2 = input("Tipo do Jogador 2: ")
    while not tipo2 in {"Estabanado", "ComeCru", "Humano"}:
        print("Escolha um tipo de jogador válido")
        tipo2 = input("Tipo do Jogador 2: ")
    print()
    print(f"{tipo_do_jogo}\n")
    tipo_jogo = input("Tipo de jogo: ")
    while not tipo_jogo in {"Tradicional", "Random"}:
        print("Escolha um formato válido")
        tipo_jogo = input("Tipo de jogo: ") 
    print()
    print(f"{tudo_pronto}\n")
    if tipo_jogo == "Random":
        mjv = Random(tipo1, nome1, tipo2, nome2)
    
    else:
        mjv = Tradicional(tipo1, nome1, tipo2, nome2)
        
    mjv.jogar()
    
if __name__ == "__main__":
    main()

