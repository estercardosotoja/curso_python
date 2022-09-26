"""
    1) Teste se um arquivo chamado livros.txt não exista pela abertura x, caso o
    arquivo já exista abra como w+, utilize Try/Except nessa manipulação. Imprima
    na tela qual foi o modo de abertura, escreva no bloco o nome dos três melhores
    livros que você já leu (um em cada linha) adicionando ao arquivo, feche-o.
    Abrao novamente e adicione mais um livro ao final do arquivo sem apaga-lo, por fim,
    leia a versão final.
"""

try:
    with open('Aula90_ModosDeAberturadeArquivosExercicio.txt','x') as arq:
        print('Modo de Abertura x')
        arq.write('Harry Potter\nCortiço\nHomoSapiens')
except FileExistsError:
    with open('Aula90_ModosDeAberturadeArquivosExercicio.txt', 'w+') as arq:
        print('Modo de Abertura w+')
        arq.write('Harry Potter\nCortiço\nHomoSapiens\n')

        arq.close()

with open('Aula90_ModosDeAberturadeArquivosExercicio.txt','a') as arq:
    print('Modo de Abertura a')
    arq.write('1964\n')

    arq.close()

with open('Aula90_ModosDeAberturadeArquivosExercicio.txt','r') as arq:
    print('Modo de Abertura r')
    print(arq.read())
