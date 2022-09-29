"""
Crie uma classe Robo para controlar o objeto R2D2 com os seguintes métodos:
- Construtor: Recebe como atributo a bateria que varia entre 0 e 100 e cria um atributo de instancia chamado estado
que apresenta se o robô está ligado ou desligado.

- liga_desliga: Quando esse método é chamado o robô passa a ser ligado caso esteja desligado e vice-versa.

- movimento: Recebe como atributo uma string, que representa qual o lado que o robô irá andar e decresce o
atributo bateria em 10 para cada execução desse método.

- controle_energia: Imprime os atributos estado e bateria atualizados do Robo.

Crie uma interface de menu para o Usuário decidir o que irá fazer com o Robo, ou seja,
qual método irá acessar. Faça tratamento de erros com Try/Except/Else/Finally.
Trate também as condições especiais como bateria zerada o que irá acontecer com o seu R2D2?
Dentre outros, fica a cargo de cada programador.
"""


class Robo:

    def __int__(self, bateria, estado):
        self.bateria = bateria
        self.estado = estado

    def liga_desliga(self):
        if self.estado is True:
            self.estado = False
        else:
            self.estado = True

    def movimento(self, string):
        if string is True:
            self.bateria -= 10

    def controle_energia(self):
        print("---------- R2D2 ----------"
              "\nBateria: ", self.bateria +
              "\nEstado: ", self.estado)

    def menu(self):
        r2d2 = True
        op = input("---------- R2D2 ----------"
                   "\n 1 - Liga/ Desligar"
                   "\n 2 - Movimento"
                   "\n 3 - Controle de Energia"
                   "\n 4 - Sair"
                   "\n Digite a opção: ")
        while r2d2 is True:
            if op == '1':
                self.liga_desliga()
                if self.estado is True:
                    print("\n Estado atual é: Ligado")
                else:
                    print("\n Estado atual é: Desligado")
                self.controle_energia()

            elif op == '2':
                lado = input('Qual lado deseja movel? '
                             '\n 1 - Esquerda'
                             '\n 2 - Direira '
                             '\n 3 - Para frente'
                             '\n 4 - Para Atras'
                             '\n Digite o numero: ')

                self.controle_energia()
                self.movimento(lado)
                self.controle_energia()
            elif op == '3':
                self.controle_energia()
            elif op == '4':
                r2d2 = False
                break
            else:
                print("\n Opçao errada, Digite novamente")
