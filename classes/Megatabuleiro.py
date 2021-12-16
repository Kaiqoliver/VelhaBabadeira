from Tabuleiro import *

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
        if not self.vencido:
            res = self.jogao[a][b].marcar(x, y, conteudo)
            # sortear vencedor caso dê velha
            if self.jogao[a][b].deu_velha():
                self.jogao[a][b].vencido = True
                if random.random() < 0.5:
                    self.jogao[a][b].vencedor = "X"
                else:
                    self.jogao[a][b].vencedor = "O"
                self.jogao[a][b].desenha_vencedor()
            # marcar o mini tabuleiro que representa o tabuleirão
            if self.jogao[a][b].vencido and not self.jogo[a][b].alterou:
                self.marcar(a, b, self.jogao[a][b].vencedor)
                print(self.jogao[a][b].vencido)
                self.venceu()
                print(self.jogao[a][b].vencido)
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

