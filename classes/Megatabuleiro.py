import sys
sys.path.insert(1, '.')
from classes.Tabuleiro import *

class Mega_Tabuleiro(Tabuleiro):
    '''Simula um Mega Jogo da Velha '''
    def __init__(self):
        Tabuleiro.__init__(self, "Megatabuleiro")
        tab00 = Tabuleiro("1")
        tab01 = Tabuleiro("2")
        tab02 = Tabuleiro("3")
        tab10 = Tabuleiro("4")
        tab11 = Tabuleiro("5")
        tab12 = Tabuleiro("6")
        tab20 = Tabuleiro("7")
        tab21 = Tabuleiro("8")
        tab22 = Tabuleiro("9")
        self.jogao = [[tab00,tab01,tab02],[tab10,tab11,tab12],[tab20,tab21,tab22]]
    
    def mega_marcar(self, a, b, x, y, conteudo):
        if not 0 <= a < 3 or not 0 <= b < 3:
            return -3 

        if not self.vencido and not self.velhado:
            res = self.jogao[a][b].marcar(x, y, conteudo)
            # sortear vencedor caso dê velha
            if self.jogao[a][b].velhado:
                self.jogao[a][b].vencido = True
                if random.random() < 0.5:
                    self.jogao[a][b].vencedor = "X"
                else:
                    self.jogao[a][b].vencedor = "O"
                self.jogao[a][b].desenha_vencedor()
            # marcar o mini tabuleiro que representa o tabuleirão
            if self.jogao[a][b].vencido: 
                self.marcar(a, b, self.jogao[a][b].vencedor)
        if self.vencido:
            print()
            print(f"O jogo terminou com o {self.vencedor} como vencedor do Mega Jogo da Velha.")
            return -5
        # c.c., deu velha
        if self.velhado:
            print()
            print()
            print("O Megatabuleiro deu velha.")
            return -4
        return res

   
    def imprimirTotal(self):
        for i in range(3):
            print("(+=====++=====++=====+)")
            for j in range(3):
                print("|",end="")
                for a in range(3):
                    print("|",end="")
                    for b in range(3):
                        print(f"{self.jogao[i][a].jogo[j][b].conteudo}|", end ="")
                    #print("|",end="")
                print("|",end="")
                print()
        print("(+=====++=====++=====+)")

