import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *
from classes.MegaJogoDaVelha import *

jogo = Jogo("Estabanado", "kaninho", "Estabanado", "kaiquinho","Tradicional")
jogo.jogar()