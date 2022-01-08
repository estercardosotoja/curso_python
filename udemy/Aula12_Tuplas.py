"""
Tuplas

As tuplas são muito parecidas com listas, há duas diferenças:
    1 - Não pode remover ou adicionar dados, apenas sobreescrever;
    2 - Enquanto as listas são com [] 'colchetes' as tuplas são com () 'parenteses'
    Sintaxe: (elemento, elemento1, elemento2,...,elementoN) ou elemento, elemento1, elemento2,...,elementoN
    obs: o que determina uma dupla são as virgulas

    Vantagens das Tuplas
     - São mais seguras para os dados;
     - São mais rápidas para serem processadas;
     - Em duplas não há Shallow Copy = Cópias listas e as conecta, ou seja, qualquer modificação em uma modifica a outra.
     Então sempre serão idependentes entre si.

    ex:  #TEM QUE TER A VITGULAAAHHH
    tuplas1 = (1, 2, 3, 4, 5)
    tuplas2 = (1,)
    tuplas3 = 1, 2, 3, 4, 5
    tuplas4 = 1,

    print(type(tuplas1), type(tuplas2), type(tuplas3), type(tuplas4))

    Quando usar?
    - Quando não for necessário realizar modificações nos dados
    Exemplo: Calendário = meses, dias do ano.

"""


