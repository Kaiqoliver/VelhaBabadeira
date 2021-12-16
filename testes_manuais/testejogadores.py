from Tabuleiro import *
from Megatabuleiro import *
from Jogadores import *

tabteste = Mega_Tabuleiro()
tabteste.imprimirTotal()
jogador1 =  Humano("pedrinho", "O", tabteste)
jogador2 =  Humano("kaiquinho","X",tabteste)

vez1 = True
vez2 = False
while (not tabteste.vencido):
    jogador1.jogada()
    tabteste.imprimirTotal()
    tabteste.imprime()
    jogador2.jogada()
    tabteste.imprimirTotal()
    tabteste.imprime()


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

print(tabteste.venceu())
print(tabteste.vencedor)
print(tabteste.vencido)
