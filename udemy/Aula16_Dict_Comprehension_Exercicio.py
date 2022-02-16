"""

1) Para todos os números de 1 a 99, use Dict Comprehension para encontrar o
dígito único mais alto em que qualquer um dos números é divisível. Ex: 64 tem
o maior divisor de digito único de 8, pois 9 não é divisor de 64.

"""

resultado = {number: max([divisor for divisor in range(1, 10) if number % divisor == 0]) for number in range(1, 100)}
print(resultado)

# Na linha acima estamos fazendo para cada number dentro do intervalo de 1 a 99 faça:
# (chave)number: Pegue o maior valor dentro da list comprehension(colchetes):
# Para cada divisor dentro do intervalo de 1 a 9(divisores de 1 digito) faça:
# Se o resto da divisão de number por divisor for zero adicione divisor a lista.
# Imprime resultado