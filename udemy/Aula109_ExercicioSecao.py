"""
 - Crie uma SuperClasse chamada 'Pessoa' que recebe como atributos nome,
cpf e salário. Após isso, construa a Classe Filha: 'Funcionario', que possui o
método sem parâmetros chamado 'promocao', que apenas acrescenta 10% no
salário a algum funcionário. Por sua vez, a classe 'Funcionario' deve ser
Classe Mãe de outras duas classes: 'Gerente' e 'Estagiario', e ambos precisam
ter o atributo 'codigo' em seu método construtor. Além disso, o gerente precisa
do atributo 'numEstagiarios', representando a quantidade de funcionário que
ele é responsável. Ainda, na classe gerente deve haver um método que
possibilite a alteração do código dos estagiários, sendo que os estagiários não
têm acesso a troca de codigo. Instancie 3 estagiários e 1 gerente. Dê
promoção para os dois primeiros estagiários e para o gerente.
Obs.: Utilize também um método mágico para representar as classes
'Estagiário' e 'Gerente', e propriedades para acessar os atributos de 'Pessoa'.
"""


class Pessoa:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, valor):
        self.salario = valor

    def __repr__(self):
        return f'\n Pessoa \n Nome: {self.nome} \n CPF: {self.cpf} \n Salario: {round(self.salario)}'
                                                                                # round = arrendonda valor


class Funcionario(Pessoa):

    def promocao(self):
        self.salario *= 1.1


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, codigo_gerente, num_estagiario, codigoEstagiarios):
        super().__init__(nome, cpf, salario)
        self.codigo_gerente = codigo_gerente
        self.num_estagiario = num_estagiario
        self.codigoEstagiarios = codigoEstagiarios

    def alt_cod_estagiario(self, novo_cod):
        self.codigoEstagiarios = novo_cod

    def __repr__(self):
        return f'\n Sou Gerente {self.nome} e possuo {self.num_estagiario} colaboradores sob minha gerencia'


class Estagiario(Funcionario):

    def __init__(self, nome, cpf, salario, codigo_estagiario):
        super().__init__(nome, cpf, salario)
        self.__codigo_estagiario = codigo_estagiario


gerente = Gerente('Pablo', 12345678900, 12000, 'gege123', 3, 'es1234')
estagiario1 = Estagiario('João', 12345678911, 400, 'es1234')
estagiario2 = Estagiario('Larissa', 12345678922, 400, 'es1234')
estagiario3 = Estagiario('Pedro', 12345678933, 400, 'es1234')

print(gerente.__repr__())
print(estagiario1.__repr__())
print(estagiario2.__repr__())
print(estagiario3.__repr__())


