import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, './classes')
from Tabuleiro import *

tabteste = Tabuleiro("tabteste")
tabteste.imprime()
print()
tabteste.marcar(0,0,"X")
tabteste.imprime()
print()
tabteste.marcar(0,0,"O")
tabteste.imprime()
print()
# tabteste.marcar(0,2,"X")
# tabteste.imprime()
# print()
# tabteste.imprime()
# tabteste.marcar(0,0,"X")
# print(tabteste.venceu())
# print(tabteste.vencedor)
# print(tabteste.vencido)
