"""
1 - Crie uma superclasse chamada 'FormaGeometrica', que possui um método
'calcula_area' e recebe o nome de uma figura geométrica em seu método
construtor. Após isso, crie duas subclasses ('Areaquadrado' e 'Areacirculo') que
herdam de 'FormaGeométrica' e calculam a área de sua respectiva forma. O
método nas Classes Filhas deve ter o nome 'calcula_area', igual em sua Classe
Mãe.
"""


class FormaGeometrica:

    def __init__(self, nome_forma):
        self.nome_forma = nome_forma

    def calcula_area(self):
        return 'Área desse do' + self.nome_forma + ' é: '


class AreaQuadrado(FormaGeometrica):

   def calcula_area(self):
    tam = float(input(f'\n Digite o largura do quadrado:'))

    if tam > 0:
        area = tam ** 2
        print(f'A área do quadrado é: {area} ')
    else:
        print('\n Área não pode ter número negativo')


class Areacirculo(FormaGeometrica):

    def calcula_area(self):
        raio = float(input(f'\n Digite o raio do circulo:'))

        if raio > 0:
            area = raio * 3.14
            print(f'A área do circulo é: {area} ')
        else:
            print('\n Área Não pode ser número negativo')


cir_peq = Areacirculo('circulo_pequeno')
qua_grand = AreaQuadrado('quadrado grande')

qua_grand.calcula_area()
cir_peq.calcula_area()

