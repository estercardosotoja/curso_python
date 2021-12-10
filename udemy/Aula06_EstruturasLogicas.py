"""
Estruturas Lógicas

and (e): True apenas se todas as condições forem True
or (ou): True quando pel menos uma condição for True
is (é): Comparação entre os valores, similar ao ==
not (não): Invertido do valor booleano (True - False
                                        False -> True)
"""

#Exemplo 1 - AND
agua = True;
comida = False;

if agua and comida:
    print('Cachorro feliz')
else:
    print('Cachorro triste')

#Exemplo 2 - OR

pizza = False;
lasanha = False;

if pizza or lasanha:
    print('Ester feliz')
else:
    print('Ester triste')

#Exemplo 3 - IS
login = False

if login is True:
    print('Logado')
else:
    print('Deslocado')

#Exemplo 4 - NOT
login = False

if not login:
    print('Deslocado')
else:
    print('Logado')

