"""
Sets Comprehension
"""
"""
Relembrando:
- Não possuem ordenação
- Não possuem elementos repetidos
- São declarados por chaves {}

#Aplicações
#String:
trava_linguas ='O rato roeu a roupa do rei de roma'
conjunto = {letra for letra in trava_linguas}
print(conjunto) #Estará desordenado e sem letras repetidas

#Range():
Forma 1:
conjunto_impares = {numero for numero in range(1,21,2)}
print(conjunto_impares)
Forma 2:
conjunto_impares = {numero for numero in range(1,21) if numero % 2 != 0}
print(conjunto_impares)

#Desafio: Faça usando comprehension de conjuntos imprimir os multiplos de 3, porem os não multiplos
devem ser impressos com a mensagem print('Desconhecido:{numero}').

- Respeite sempre a ordem de importancia.
"""

multiplos_tres = {numero if numero % 3 == 0 else print(f"Desconhecido:{numero}") for numero in range(1, 21)}
print(multiplos_tres)

#IMPORTANTE: Caso há algum print() dentro do comprehesion, será retornado None como um dos elementos.


