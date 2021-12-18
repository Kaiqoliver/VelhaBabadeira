import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *

tabteste = Mega_Tabuleiro()
tabteste.imprimirTotal()
jogador1 =  ComeCru("pedrinho", "O", tabteste)
jogador2 =  ComeCru("kaiquinho","X",tabteste)

turno = 1
while (not tabteste.vencido):
    if (turno % 2 == 1):
        jogador1.jogada()
    else:
        jogador2.jogada()
    tabteste.imprimirTotal()
    print()
    tabteste.imprime()
    input()
    turno += 1



#print()
##tabteste.marcar(0,0,"X")
#jogador1.jogada()
#tabteste.imprimirTotal()
#print()
##tabteste.marcar(0,1,"X")
#jogador1.jogada()
#tabteste.imprimirTotal()
#print()
##tabteste.marcar(0,2,"X")
#jogador1.jogada()
#tabteste.imprimirTotal()
#print()
##tabteste.marcar(0,0,"X")
#jogador1.jogada()
#tabteste.imprimirTotal()
