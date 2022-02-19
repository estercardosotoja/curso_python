"""
 1) Para cada número par em um range de 1 a 9, adicione esse número elevado
ao quadrado no conjunto, se o número for ímpar adicione 2 elementos, 1 por vez: 
‘Sou’, ’Impar’. Qual foi a resposta? Por que ‘Sou’, ‘Impar’ só apareceu uma vez?

"""


numeros = {num**2 if num % 2 == 0 else "Sou" "Impar" for num in range(1, 9)}
print(numeros)
