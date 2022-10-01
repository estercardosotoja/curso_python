"""
    1) Deseja-se criar um programa que deixe a formula secreta da coca cola
    criptografada, para isso crie uma classe FormulaCocaCola com atributos
    privados: ingrediente, temperatura (Celsius), açúcar (gramas) e o nome do
    proprietário. Crie uma senha de acesso escolhida pelo usuário, instancie o
    objeto e passe o mesmo para um arquivo PICKLE. Após isso, peça a senha
    para acessar os atributos, caso esteja correta, leia o arquivo e imprima-os, se
    não imprima um aviso de acesso negado.
"""
import jsonpickle


class FormulaCocaCola:

    senha = ' '

    def __init__(self, ingre, tempe, acucar, name_prop):
        self.__ingre = ingre
        self.__tempe = tempe
        self.__acucar = acucar
        self.__name_prop = name_prop

    @property
    def ingre(self):
        return self.__ingre

    @ingre.setter
    def ingre(self, value):
        self.__ingre = value

    @property
    def tempe(self):
        return self.__tempe

    @tempe.setter
    def tempe(self, value):
        self.__tempe = value

    @property
    def acucar(self):
        return self.__acucar

    @acucar.setter
    def acucar(self, value):
        self.__acucar = value

    @property
    def name_prop(self):
        return self.__name_prop

    @name_prop.setter
    def name_prop(self, value):
        self.__name_prop = value

    def registrando_formula(self):
        formula = {'Ingrediente': self.__ingre,
                   'Temperatura': self.__tempe,
                   'Açucar': self.__acucar,
                   'Nome Proprietario': self.__name_prop
                   }

        with open('Aula111_ManipulandoPickleJsonExercicio_CocaCola.json', 'w') as arq:
            arq.write(jsonpickle.encode(formula))

    def create_acess(self):
        self.senha = input('\n Digite a senha: ')
        print('\n Senha criada com sucesso!')

    def acesso_formula(self):
        senha_digitada = input('\n Digite a senha: ')

        if senha_digitada == self.senha:
            with open('Aula111_ManipulandoPickleJsonExercicio_CocaCola.json') as arq:
                print(jsonpickle.decode(arq.read()))
        else:
            print("\n Acesso Negado")


cocav1 = FormulaCocaCola('COCA', 20, 70, 'Ambev')
cocav1.registrando_formula()
cocav1.create_acess()
cocav1.acesso_formula()
