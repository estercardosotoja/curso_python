"""
1 - Um escritor de livros pretende escrever e lançar edições para atingir a quantia de 1 milhão de reais.
Simplesmente por este motivo, crie uma classe que receberá em seu método construtor o nome do livro e o
número de páginas. Além disso, também deve ser criado um atributo no construtor para a edição do livro,
que será atualizado em uma unidade a cada livro que for publicado. Por fim, utilize randint() para gerar
um valor entre 0 e 500 mil, representando a arrecadação das vendas, o último atributo do construtor.
Crie o método mágico __repr__ para representar o nome do livro e a edição. Ainda, utilize __len__ para
determinar o número de páginas de cada livro. Por fim, verifique se o valor total de arrecadações
atingiu 1 milhão de reais.
"""

from random import randint as ri


class Livro:

    def __init__(self, nome_livro, num_pag, edicao, valor_arre):
        self.nome_livro = nome_livro
        self.num_pag = num_pag
        self.edicao = edicao
        self.valorArre = valor_arre

    def __repr__(self):
        return '\n Nome do Livro: ' + {self.nome_livro} + '\n Edição: ' + {self.edicao}

    def __len__(self):
        return self.num_pag

# Instanciação


livro1 = Livro('Harry Potter e as Relíquias da Morte', 551, 1, ri(0, 500000))
livro2 = Livro('O Pequeno Príncipe', 96, 2, ri(0, 500000))
livro3 = Livro('Mar Sem Fim', 308, 3, ri(0, 500000))


valorTotal = livro1.valorArre + livro2.valorArre + livro3.valorArre
if valorTotal > 1000000:
    print('\nParabéns! Você agora é um milionário!')
else:
    print('\nTente criar mais livros!')
print(f'Valor arrecadado: {valorTotal}')
