import sys
sys.path.insert(1, '.')
from classes.Tabuleiro import *
import pytest

def test_marca_inexistente():
    tab = Tabuleiro("Tabteste")
    res = tab.marcar(4, 4, "X")
    assert res == -3

def test_marca_repetido():
    tab = Tabuleiro("Tabteste")
    tab.marcar(0, 0, "X")
    res = tab.marcar(0, 0, "O")
    assert res == -1 

def test_marca_velha():
    tab = Tabuleiro("Tabteste")
    tab.marcar(0, 0, "X")
    tab.marcar(0, 1, "O")
    tab.marcar(0, 2, "X")
    tab.marcar(1, 0, "O")
    tab.marcar(1, 2, "X")
    tab.marcar(2, 2, "O")
    tab.marcar(1, 1, "X")
    tab.marcar(2, 0, "O")
    tab.marcar(2, 1, "X")
    assert tab.marcar(2, 0, "O") == -4

def test_vencido():
    tab = Tabuleiro("Tabteste")
    tab.marcar(0, 0, "X")
    tab.marcar(1, 1, "X")
    tab.marcar(2, 2, "X")
    assert tab.vencido

def test_deu_velha():
    tab = Tabuleiro("Tabteste")
    tab.marcar(0, 0, "X")
    tab.marcar(0, 1, "O")
    tab.marcar(0, 2, "X")
    tab.marcar(1, 0, "O")
    tab.marcar(1, 2, "X")
    tab.marcar(2, 2, "O")
    tab.marcar(1, 1, "X")
    tab.marcar(2, 0, "O")
    tab.marcar(2, 1, "X")
    assert tab.deu_velha()

def test_marca_tabuleiro_vencido():
    tab = Tabuleiro("Tabteste")
    tab.marcar(0, 0, "X")
    tab.marcar(0, 1, "O")
    tab.marcar(1, 1, "X")
    tab.marcar(0, 2, "O")
    tab.marcar(2, 2, "X")
    res = tab.marcar(2, 0, "O")
    assert res == -2
