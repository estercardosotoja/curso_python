"""
Dict Comprehension
"""
"""
- Representados por chaves {}
- Possuem a relação chave->dado

Como declarar?
Ex:
a)

"""
#Exemplo apenas com for
#Exemplo para criar um outro dicionario dividindo idade pela metade
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
pessoas_meia_idade = {chave: dado // 2 for chave, dado in pessoas_idade.items()}
print(pessoas_meia_idade)

#b)
#Exemplo de if e for
#Exemplo para criar um outro dicionario que contenha apenas os maiores de idade
pessoas_idade = {'Ana': 22,'Matheus' : 17, 'Lucas': 24}
maiores_idade = {chave: dado for chave, dado in pessoas_idade.items() if dado >= 18}
print(maiores_idade)

#c)
#Exemplo com if,else e for
#Criando um dicionario com pessoas maiores de idade,mas com um aviso para o menor de idade
pessoas_idade = {'Ana': 22, 'Matheus': 17, 'Lucas': 24}
maiores_idade = {chave: (dado if dado >= 18 else 'Não pode entrar') for chave, dado in pessoas_idade.items()}
print(maiores_idade)
