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
    name = str(input("Digite seu username: "))
    senha = input("Digite a senha: ")
    user = {name: senha}
    print(f"\o/ Realizado Cadastro \o/")
    return user


def realizar_login(user):
    print(f"\n \t \t \t *********** Realizar Login ********** ")
    print(user)
    if cadastro:
        nome_digitado = str(input("Digite nome do usuário"))
        senha_digitada = input("Digite a senha")
        print(user.get(nome_digitado))
        print(user.get(senha_digitada))
        if nome_digitado in user.values() and senha_digitada in user.items():
            print("******** Realizamos login ******")
            return True
        else:
            print("Não realizamos login \n Erro senha ou user")
            return False
    else:
        print("Não tem nenhum usuário cadastrado \nCadastre novo usuário" )
        return False



def alterar_senha():
    print(f"\n  \t \t \t *********** Alterando Senha ********** ")

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