"""
1 - Crie duas classes (uma para um personagem no video game e outra para o
controle do console). O controle deve ser capaz de fazer o personagem pular,
abaixar, desviar para esquerda e desviar para direita, sendo comandado,
respectivamente, pelas teclas W, A, S e D. Use a dica e a função choice()
para determinar por onde virá o obstáculo ('Cima', 'Baixo', 'Esquerda' ou
'Direita'), e o tempo para o próximo obstáculo, que deve decair com o aumento
dos pontos. Cada obstáculo passado gera +1 ponto. Ainda, crie um loop infinito
do jogo até a pessoa perder. Por fim, apresente a pontuação final.
Dica:
import time
time.sleep(3) # O programa 'para' por 3 segundo
"""


class Personagem:

    def __init__(self, nome, alt, peso, resis):
        self.nome = nome
        self.alt = alt
        self.peso = peso
        self.resis = resis

    def pular(self):
        print('\n Pulou')

    def apertou_w(self, personagem):
        personagem.__pular()

    def abaixar(self):
        print('\n Abaixou')

    def apertou_s(self, personagem):
        personagem.__abaixar()

    def desviar_esquerda(self):
        print('\n Desviou para a esquerda')

    def apertou_a(self, personagem):
        personagem.__desviar_esquerda()

    def desviar_direita(self):
        print('\n Desviou para a direita')

    def apertou_d(self, personagem):
        personagem.__desviar_direita()

    def main(self):
        jogo = True
        while jogo is True:
            op = input('\n -- W - Pular, '
                       '\n -- A - Abaixar, '
                       '\n -- S - Desviar para a Esquerda '
                       '\n -- D - Desviar para a Direita '
                       '\n --------: Digite seu comando: -- : ')

            if op == 'W':
                self.pular()
            elif op == 'A':
                self.abaixar()
            elif op == 'S':
                self.desviar_esquerda()
            elif op == 'D':
                self.desviar_direita()
            else:
                print("\n Opção errada!")
