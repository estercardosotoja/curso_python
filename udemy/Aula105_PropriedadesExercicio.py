"""
1 - Crie uma classe contendo atributos públicos e privados representando
objetos pessoais. Após isso, crie uma propriedade pra cada atributo privado.
Instancie um objeto e faça acesso a todos os atributos. Utilize também o setter,
para alterar algum valor do objeto.

"""


class DadosPessoais:

    def __init__(self, email, cpf, end, placa_car):
        self.__email = email
        self.__cpf = cpf
        self.end = end
        self.placa_car = placa_car

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

    def end(self):
        return self.end

    def placa_car(self):
        return self.placa_car()

    def __str__(self):
        return '\n --- Dados Pessoais --- ' \
               '\n Email: ' + self.email + \
               '\n CPF: ' + self.cpf + \
               '\n Endereço: ' + self.end + \
               '\n Placa do Carro: ' + self.placa_car


pessoa1 = DadosPessoais('pessoa1@gmail.com', '123.456.789.09', 'Rua da Esperanca n 409', 'QWE-4568')
pessoa2 = DadosPessoais('pessoa2@gmail.com', '098.765.432.10', 'Rua da Comemoracao n 89', 'ASD-3216')
print(pessoa1)
print(pessoa2)
