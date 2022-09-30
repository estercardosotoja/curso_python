"""
1 - Desenvolva o sistema de um controle universal para uma casa. O controle deve ser a Classe-Mãe, que
contém o método liga/desliga e é herdada por outras três classes (equipamentos controlados):
ar-condicionado, micro-ondas e televisão, que controlam, respectivamente, temperatura, tempo e volume em
métodos dentro das classes. Além disso, os métodos construtores das Classes Filhas recebem a variável
controlada em seu valor atual, por exemplo 'temperaturaAtual'.
Obs.: Utilize também propriedades para realizar o acesso aos atributos.

"""


class Control:

    def liga_desliga(self, estado):
        if self.estado is True:
            self.estado = estado
        else:
            self.estado = estado


class ArCondicionado(Control):

    def __init__(self, estado, temperatura):
        super.__init__(estado)
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp):
        self.__temperatura = temp

    @property
    def temperaturaAtual(self):
        return f'Temperatura atual: {self.__temperatura}'


class MicroOndas(Control):

    def __init__(self, estado, tempo):
        super.__init__(estado)
        self.__tempo = tempo

    @property
    def tempo(self):
        return self.__tempo()

    @tempo.setter
    def tempo(self, time):
        self.__tempo = time

    @property
    def tempoAtual(self):
        return f'Tempo atual: {self.__tempo}'


class Televisao(Control):

    def __init__(self, estado, volume):
        super.__init__(estado)
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume()

    @volume.setter
    def volume(self, tam):
        self.__volume = tam

    @property
    def volumeAtual(self):
        return f'Volume atual: {self.__volume}'


arc = ArCondicionado(False, 45)
mic = MicroOndas(False, 60)
tv = Televisao(False, 85)

print('\n')
print(tv.liga_desliga())
tv.volume(80)
print(tv.volumeAtual)
print(tv.volume)
