# VelhaBabadeira - EP4 MAC0216
Um Ultimate tic-tac-toe (ou Mega Jogo-da-velha), como descrito [aqui](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe), para terminal, com duas opções de jogo:
 Tradicional ou Random, e duas opções de jogadores automáticos: Estabanado ou Come-Crú, além do jogador Humano.

## Tabela de Conteúdos
* [Contribuintes](#contribuintes)
* [Detalhes do jogo](#detalhes-do-jogo)
* [Informações gerais](#informações-gerais)
* [Setup](#setup)

## Contribuintes
* Kaique Nunes de Oliveira NUSP12542244
* Felipe Kaneshiro de Souza NUSP11795770
* Pedro Lucas Resende Siqueira Campos NUSP12674130

## Detalhes do Jogo
### Modos de Jogo
* Modo Tradicional

Neste modo, um dos jogadores terá o primeiro turno de ação, e a seguir, os jogadores se alternam entre turnos para fazerem suas jogadas.

* Modo Aleatório

Neste modo, o turno de ação é concedido a um dos jogadores através da sorte. Como no lançar de uma moeda, todo turno terá um jogador sorteado para fazer a sua jogada.
Após o término do jogo, é exibido quanto cada participante jogou.

### Jogadores
* Estabanado

Este jogador sorteará uma posição livre do tabuleiro para marcar no seu turno.

* Come-Crú

Este jogador marcará a primeira posição livre de um tabuleiro no seu turno.

## Informações Gerais
VelhaBabadeira contém 4 arquivos destinados a classes, 3 arquivos destinados a testes automatizados com o Pytest e 4 arquivos que foram utilizados para
 testes manuais, além do programa principal, _jogo.py_.
 
 O objetivo deste Exercício é treinar conceitos de [Programação Orientada a Objetos](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos) bem como
 o uso de [Testes Automatizados](https://pt.wikipedia.org/wiki/Automa%C3%A7%C3%A3o_de_teste). Assim, buscamos transformar em objetos os elementos principais de um
  jogo da velha, e testamos cada classe primordial com testes automatizados a fim de garantir o comportamento esperado.
  
  Em _Tabuleiro.py_ abstraímos um tabuleiro com 9 posições que pode ser marcado, impresso e ter seu estado conferido (ter sido ganho ou _velhado_).
  
  Em _Megatabuleiro.py_ utilizamos o conceito de herança para construir um tabuleiro de 9 posições que serão marcadas de acordo com o estado de 9 tabuleiros.
  
  Em _Jogadores.py_ fizemos cada jogador fazer a sua jogada de acordo com seu comportamento esperado.
  
  Cada um dos objetos acima foram testados ou para garantir um comportamento mesmo em casos extremos, no caso dos tabuleiros, ou para averiguar o comportamento
  esperado, no caso do estilo de jogo dos jogadores.
  
  E em _MegaJogoDaVelha.py_ construímos a interface básica do jogo com o usuário, assim como a alternância de turnos e opções para se escolher durante um jogo.
  
  Finalmente, em _jogo.py_ pudemos contar com cada um dos objetos para iniciar um Mega jogo-da-velha de acordo com as entradas do usuário.

## Setup
Para jogá-lo, basta clonar o repositório em seu computador numa pasta desejada:
```
git clone https://github.com/Kaiqoliver/VelhaBabadeira
```
e executar o jogo dentro da pasta instalada usando Python3:
```
cd VelhaBabadeira
python3 jogo.py
```
