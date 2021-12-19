import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
import pytest

def test_mega_marcar_inexistente():
    mtab = Mega_Tabuleiro()
    res = mtab.mega_marcar(-1, 0, 0, 0, "X")
    assert res == -3 

def test_mega_tab_vencido():
    mtab = Mega_Tabuleiro()
    mtab.mega_marcar(0, 0, 0, 0, "X")
    mtab.mega_marcar(0, 0, 0, 1, "X")
    mtab.mega_marcar(0, 0, 0, 2, "X")
    mtab.mega_marcar(0, 1, 0, 0, "X")
    mtab.mega_marcar(0, 1, 1, 1, "X")
    mtab.mega_marcar(0, 1, 2, 2, "X")
    mtab.mega_marcar(0, 2, 0, 2, "X")
    mtab.mega_marcar(0, 2, 1, 1, "X")
    mtab.mega_marcar(0, 2, 2, 0, "X")
    assert mtab.vencido 

def test_mega_tab_deu_velha():
    mtab = Mega_Tabuleiro()
    mtab.mega_marcar(0, 0, 0, 0, "X")
    mtab.mega_marcar(0, 0, 0, 1, "X")
    mtab.mega_marcar(0, 0, 0, 2, "X")

    mtab.mega_marcar(0, 1, 1, 0, "O")
    mtab.mega_marcar(0, 1, 1, 1, "O")
    mtab.mega_marcar(0, 1, 1, 2, "O")
     
    mtab.mega_marcar(0, 2, 2, 0, "X")
    mtab.mega_marcar(0, 2, 2, 1, "X")
    mtab.mega_marcar(0, 2, 2, 2, "X")
     
    mtab.mega_marcar(1, 0, 0, 0, "O")
    mtab.mega_marcar(1, 0, 1, 1, "O")
    mtab.mega_marcar(1, 0, 2, 2, "O")

    mtab.mega_marcar(1, 2, 0, 2, "X")
    mtab.mega_marcar(1, 2, 1, 1, "X")
    mtab.mega_marcar(1, 2, 2, 0, "X")
     
    mtab.mega_marcar(2, 2, 0, 0, "O")
    mtab.mega_marcar(2, 2, 1, 0, "O")
    mtab.mega_marcar(2, 2, 2, 0, "O")

    mtab.mega_marcar(1, 1, 0, 1, "X")
    mtab.mega_marcar(1, 1, 1, 1, "X")
    mtab.mega_marcar(1, 1, 2, 1, "X")
     
    mtab.mega_marcar(2, 0, 0, 2, "O")
    mtab.mega_marcar(2, 0, 1, 2, "O")
    mtab.mega_marcar(2, 0, 2, 2, "O")
     
    mtab.mega_marcar(2, 1, 0, 0, "X")
    mtab.mega_marcar(2, 1, 1, 1, "X")
    mtab.mega_marcar(2, 1, 2, 2, "X")
    assert mtab.deu_velha()

def test_marcar_mega_tabuleiro():
    mtab = Mega_Tabuleiro()
    mtab.mega_marcar(0, 0, 0, 0, "X")
    mtab.mega_marcar(0, 0, 0, 1, "X")
    mtab.mega_marcar(0, 0, 0, 2, "X")
    assert mtab.jogo[0][0].conteudo == "X"

def test_mega_marcar_mega_tabuleiro_vencido():
    mtab = Mega_Tabuleiro()
    mtab.mega_marcar(0, 0, 0, 0, "X")
    mtab.mega_marcar(0, 0, 0, 1, "X")
    mtab.mega_marcar(0, 0, 0, 2, "X")
    mtab.mega_marcar(0, 1, 0, 0, "X")
    mtab.mega_marcar(0, 1, 1, 1, "X")
    mtab.mega_marcar(0, 1, 2, 2, "X")
    mtab.mega_marcar(0, 2, 0, 2, "X")
    mtab.mega_marcar(0, 2, 1, 1, "X")
    mtab.mega_marcar(0, 2, 2, 0, "X")
    res = mtab.mega_marcar(1, 0, 0, 0, "X")
    assert res == -5

def test_mega_marcar_mega_tabuleiro_velhado():
    mtab = Mega_Tabuleiro()
    mtab.mega_marcar(0, 0, 0, 0, "X")
    mtab.mega_marcar(0, 0, 0, 1, "X")
    mtab.mega_marcar(0, 0, 0, 2, "X")

    mtab.mega_marcar(0, 1, 1, 0, "O")
    mtab.mega_marcar(0, 1, 1, 1, "O")
    mtab.mega_marcar(0, 1, 1, 2, "O")
     
    mtab.mega_marcar(0, 2, 2, 0, "X")
    mtab.mega_marcar(0, 2, 2, 1, "X")
    mtab.mega_marcar(0, 2, 2, 2, "X")
     
    mtab.mega_marcar(1, 0, 0, 0, "O")
    mtab.mega_marcar(1, 0, 1, 1, "O")
    mtab.mega_marcar(1, 0, 2, 2, "O")

    mtab.mega_marcar(1, 2, 0, 2, "X")
    mtab.mega_marcar(1, 2, 1, 1, "X")
    mtab.mega_marcar(1, 2, 2, 0, "X")
     
    mtab.mega_marcar(2, 2, 0, 0, "O")
    mtab.mega_marcar(2, 2, 1, 0, "O")
    mtab.mega_marcar(2, 2, 2, 0, "O")

    mtab.mega_marcar(1, 1, 0, 1, "X")
    mtab.mega_marcar(1, 1, 1, 1, "X")
    mtab.mega_marcar(1, 1, 2, 1, "X")
     
    mtab.mega_marcar(2, 0, 0, 2, "O")
    mtab.mega_marcar(2, 0, 1, 2, "O")
    mtab.mega_marcar(2, 0, 2, 2, "O")
     
    mtab.mega_marcar(2, 1, 0, 0, "X")
    mtab.mega_marcar(2, 1, 1, 1, "X")
    mtab.mega_marcar(2, 1, 2, 2, "X")
    
    res = mtab.mega_marcar(2, 2, 1, 1, "O")
    assert res == -4
