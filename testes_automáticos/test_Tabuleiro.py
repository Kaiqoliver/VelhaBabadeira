from classes.Tabuleiro import *

class TestaTabuleiro:
    def test_marca_inexistente():
        tab = Tabuleiro()
        res = tab.marcar(4, 4, "X")
        assert res == -3

    def test_marca_repetido():
        tab = Tabuleiro()
        tab.marcar(0, 0, "X")
        res = tab.marcar(0, 0, "O")
        assert res == -1 

    def test_marca_velha():
        tab = Tabuleiro()
        tab.marcar(0, 0, "X")
        tab.marcar(0, 1, "O")
        tab.marcar(0, 3, "X")
        tab.marcar(1, 0, "O")
        tab.marcar(1, 2, "X")
        tab.marcar(2, 2, "O")
        tab.marcar(1, 1, "X")
        tab.marcar(2, 1, "O")
        tab.marcar(2, 0, "X")
        assert tab.marcar(2, 0, "O") == -4

    def test_vencido():
        tab = Tabuleiro()
        tab.marcar(0, 0, "X")
        tab.marcar(1, 1, "X")
        tab.marcar(2, 2, "X")
        assert tab.vencido == True

    def test_deu_velha():
        tab = Tabuleiro()
        tab.marcar(0, 0, "X")
        tab.marcar(0, 1, "O")
        tab.marcar(0, 3, "X")
        tab.marcar(1, 0, "O")
        tab.marcar(1, 2, "X")
        tab.marcar(2, 2, "O")
        tab.marcar(1, 1, "X")
        tab.marcar(2, 1, "O")
        tab.marcar(2, 0, "X")
        assert tab.deu_velha() == True

    def test_tabuleiro_vencido():
        tab = Tabuleiro()
        tab.marcar(0, 0, "X")
        tab.marcar(0, 1, "O")
        tab.marcar(1, 1, "X")
        tab.marcar(0, 2, "O")
        tab.marcar(2, 2, "X")
        res = tab.marcar(2, 0, "O")
        assert res == -1

        
    