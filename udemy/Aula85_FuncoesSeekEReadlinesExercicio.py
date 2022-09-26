"""
1 - Crie um arquivo com conteúdo aleatório. Em seguida, abra o arquivo, leia-o
    3 vezes a partir dos caracteres 5, 9, 14. Por fim, feche o arquivo.
"""

file = open('Aula85_FuncoesSeekEReadlinesExercicio.txt')
file.seek(5)
print(file.read())
file.seek(9)
print(file.read())
file.seek(14)
print(file.read())
file.close()




