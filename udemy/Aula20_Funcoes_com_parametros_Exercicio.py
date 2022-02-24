"""

    1 - Criar uma função recursiva (que retorne ela mesma) para armazenar N termos da sequência de Fibonacci em uma lista.
    N é definido pelo usuário. Ao encontrar os termos, imprimir a lista e finalizar a função.
    2 - Criar 5 funções: uma para um cadastro, outra para realizar o login, outra para mudar a senha, outra para realizar
    logout e ainda uma para definir qual opção o usuário deseja escolher.
    Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a opção 'sair').
    Atente-se às regras:
     - Só é possível realizar um cadastro se não houver nenhum anterior.
     - Só é possível realizar login se houver um cadastro.
     - Só é possível realizar login se o usuário informar corretamente username e senha.
     - Só é possível alterar a senha se o usuário estiver logado.
     - Só é possível alterar a senha se o usuário informar corretamente a senha atual.
     - Só é possível realizar logout se o usuário estiver logado

"""


def realizar_cadastro():
    print(f"\n  \t \t \t *********** Cadastro ********** ")
    #name = str(input('Digite seu username:'))
    #senha = str(input('Digite a senha:'))
    #user = {name: senha}
    user = {'ester': '123'}
    print(f"\n\o/ Realizado Cadastro \o/")
    return user

def realizar_login(user):
    cadastro = len(user)
    if cadastro > 0:
        nome_digitado = 'ester'
        senha_digitada = '123'
        #print(f'Nome digitado: {user.values(senha_digitada)} \n Tipo:  {type(user.get(senha_digitada))}')
        #print(f'Senha digitada: {user.get(nome_digitado)} \n Tipo:  {type(user.get(nome_digitado))} ')

    for nome, senha in user.items():
        print(f"Nome = {nome} - Senha = {senha}")
        if nome_digitado is nome:
            if senha_digitada is senha:
                print("Login")
                return True
            else:
                print("NO LOGIN SENHA")
                return False
        else:
            print("NO LOGIN EMAIL")
            return False
    else:
        print("Usuário ou Senha Inválido!")
        return False



def alterar_senha():
    print(f"\n  \t \t \t *********** Alterando Senha ********** ")
    cadastro = len(user)
    if cadastro > 0:
        nome_digitado = 'ester' #str(input(f'User:'))
        for nome, senha in user.items():
            print(f'nome: {nome}, nome_digitado:{nome_digitado}')
            if nome_digitado is nome:
                senha_digitada = input(f'Digite a nova senha:')3+
                user_novo = {nome_digitado, senha_digitada}
                user.update(user_novo)
            else:
                print("Não há usuário com este nome!")
                return False
    else:
        print("Não há usuários cadastrados!")
        return False

def realizar_logout():
    print(f"\n \t \t \t *********** Logout ********** ")

def menu():
    global user
    global cadastro
    global login
    print(f"\n \t \t \t *********** Menu ********** ")
    opcao = int(input(f"Digite a opção:  "
                  "\n 1 - Realizar Cadastro "
                  "\n 2 - Realizar Login "
                  "\n 3 - Alterar a Senha "
                  "\n 4 - Realizar Logout"
                  "\n Opção: "))
    if opcao == 1:
        user = realizar_cadastro()
    elif opcao == 2:
        login = realizar_login(user)
    elif opcao == 3:
        alterar_senha()
    elif opcao == 4:
        realizar_logout()
    else:
        print(f"OPCAO INVALIDA \n Tente novamente!")
        menu()

def sair():
    sair = str(input("Deseja continuar? s/n "))
    return sair

user = { }
cadastro = True
login = False
while sair != 's':
    menu()
