import sys
sys.path.insert(1, '.')
from classes.Megatabuleiro import *
from classes.Tabuleiro import *
from classes.Jogadores import *
import pytest

def test_ComeCru_sozinho():
    mt = Mega_Tabuleiro()
    cc = ComeCru("ComeCrueSozinho", "O", mt)
    turno = 1

    while (not mt.vencido):
        cc.jogada()
        turno += 1
    assert turno == 10
    
def test_dois_ComeCrus():
    mt = Mega_Tabuleiro()
    cc1 = ComeCru("ComeCru1", "O", mt)
    cc2 = ComeCru("ComeCru2", "X", mt)
    turno = 1

    while (not mt.vencido):
        if (turno % 2 == 1):
            cc1.jogada()
        else:
            cc2.jogada()
        turno += 1
    assert turno == 62

def test_Estabanado_sozinho():
    mt = Mega_Tabuleiro()
    estb = Estabanado("EstabanadoSozinho", "O", mt, 216)
    turno = 1

    while (not mt.vencido):
        estb.jogada()
        turno += 1
    # a seed 216 faz o jogador sozinho acabar no turno 29
    assert turno == 29
    
    
def test_dois_Estabanados():
    mt = Mega_Tabuleiro()
    estb1 = Estabanado("Estabanado1", "X", mt, 216)
    estb2 = Estabanado("Estabanado2", "O", mt, 216)
    turno = 1
    while (not mt.vencido):
        if (turno % 2 == 1):
            estb1.jogada()
        else:
            estb2.jogada()
        turno += 1
    # a seed 216 faz os jogadores acabarem no turno 57
    assert turno == 57