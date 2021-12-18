import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
import pytest

megatab = Mega_Tabuleiro()

megatab.mega_marcar(0,0,0,0,"O")
megatab.mega_marcar(0,0,0,1,"O")
megatab.mega_marcar(0,0,2,2,"O")

# megatab.mega_marcar(0,1,0,0,"X")
# megatab.mega_marcar(0,1,0,1,"X")
# megatab.mega_marcar(0,1,0,2,"X")

# megatab.mega_marcar(0,2,0,0,"X")
# megatab.mega_marcar(0,2,0,1,"X")
# megatab.mega_marcar(0,2,0,2,"X")

megatab.imprimirTotal()
print()
megatab.imprime()