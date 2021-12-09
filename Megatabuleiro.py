from Posicao import *

class Mega_Tabuleiro(Tabuleiro):
    '''Simula um Mega Jogo da Velha '''
    def __init__(self):
        Tabuleiro.__init__(self, "Megatabuleiro")
        tab00 = Tabuleiro("tab00")
        tab01 = Tabuleiro("tab01")
        tab02 = Tabuleiro("tab02")
        tab10 = Tabuleiro("tab10")
        tab11 = Tabuleiro("tab11")
        tab12 = Tabuleiro("tab12")
        tab20 = Tabuleiro("tab20")
        tab21 = Tabuleiro("tab21")
        tab22 = Tabuleiro("tab22")
        self.jogao = [[tab00,tab01,tab02],[tab10,tab11,tab12],[tab20,tab21,tab22]]
    
    def mega_marcar(self, a, b, x, y, conteudo):
        if not self.vencido:
            self.jogao[a][b].marcar(x, y, conteudo)
            if self.jogao[a][b].vencido:
                self.marcar(a, b, self.jogao[a][b].vencedor)

        self.venceu()
        if self.vencido:
            print(f"O jogo terminou com o {self.vencedor} como vencedor do Mega Jogo da Velha")
   
    def imprimirTotal(self):
        c00 = self.jogao[0][0].jogo
        c01 = self.jogao[0][1].jogo
        c02 = self.jogao[0][2].jogo 
        c10 = self.jogao[1][0].jogo
        c11 = self.jogao[1][1].jogo
        c12 = self.jogao[1][2].jogo
        c20 = self.jogao[2][0].jogo
        c21 = self.jogao[2][1].jogo
        c22 = self.jogao[2][2].jogo
        
        tabzao = [[c00,c01,c02], 
                  [c10,c11,c12],
                  [c20,c21,c22]]
                  
        for i in range(3):
            print("(+=====++=====++=====+)")
            for j in range(3):
                print("|",end="")
                for a in range(3):
                    print("|",end="")
                    for b in range(3):
                        print(f"{tabzao[i][a][j][b].conteudo}|", end ="")
                    #print("|",end="")
                print("|",end="")
                print()
        print("(+=====++=====++=====+)")

