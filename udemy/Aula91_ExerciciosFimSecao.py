"""
    1 - Faça um programa utilizando um arquivo chamado 'NotasEscola.txt' para
    gerenciar as notas de alunos de uma classe. O main deve conter um menu
    com as seguintes opções: a) Inserir alunos e notas b) Exibir os alunos e média
    final c) Alunos aprovados e reprovados d) Sair. Produza uma função para cada
    opção.
"""


def add_aluno():
    nome = input('Digite o nome do novo aluno: ')
    nota = input('Digite o nota do novo aluno: ')
    with open('Aula91_ExerciciosFimSecaoExercicio.txt', 'a') as arq:
        arq.write(nome + ' Nota:' + nota + '\n')
    print('Lista de Alunos atualizada: \n ')
    aluno_media()
    arq.close()


def aluno_media():
    with open('Aula91_ExerciciosFimSecaoExercicio.txt', 'r') as arq:
        print(arq.read())
    arq.close()


def alunos_status():
    print("alunos_Status");
    #r+:Arquivo já deve existir. Temos o controle do cursor e podemos escrever além de ler o arquivo.
    with open('Aula91_ExerciciosFimSecaoExercicio.txt') as arq:
        listaLinhas = arq.readlines()
        for dado in listaLinhas:
            id1 = dado.index(':') #Retorna o índice do primeiro ':'
            id2 = dado.index('nota') #Retorna o índice do 'N' de 'Nota'
            nome = dado[id1 + 1:id2 - 1] #É somado e subtraido 1 dos índices para evitar os  espaços em branco
            id3 = dado.index(':', 9) #Busca A PARTIR do índice 9 e o caracter ':', ou seja, o segundo ':' da linha
            nota = float(dado[id3 + 1:])

        if nota >= 6:
            print(f'{nome} APROVADO!\n')
        else:
            print(f'{nome} REPROVADO! \n')


while True:
    opcao = input("a) Inserir alunos e notas \n"
                  "b) Exibir os alunos e média final \n"
                  "c) Alunos aprovados e reprovados \n"
                  "d) Digite uma palavra ou 'sair': \n ")
    if opcao == 'a':
        add_aluno()
    elif opcao == 'b':
        aluno_media()
    elif opcao == 'c':
        alunos_status()
    elif opcao == 'd' or opcao == 'sair':
        break;
    else:
        print("Opcao Invalida");

