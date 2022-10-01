""""""
"""
Data e Hora

- É utilizado o módulo integrado datetime.
- O formato padrão de data é o formato americano: aaaa/mm/dd
"""
import datetime


# É possível trabalhar com fuso horário
print('\n Data Atual - Possivel trabalhar com fuso horário')
horarioAtual = datetime.datetime.now()
print(horarioAtual)
print(type(horarioAtual))

print("\n Data Atual")
horarioAtual = datetime.datetime.today()
print(horarioAtual)
print(type(horarioAtual))

print('\n ')
print(repr(datetime.datetime.now()))
print(dir(datetime))

print('\n Ano máximo')
print(datetime.MAXYEAR)
print('\n Ano minimo')
print(datetime.MINYEAR)

print('\n ')
horarioAtual = datetime.datetime.now()
print(repr(horarioAtual))

print('\n Ano:')
print(horarioAtual.year)
print('\n Mes:')
print(horarioAtual.month)
print('\n Dia:')
print(horarioAtual.day)
print('\n Hora:')
print(horarioAtual.hour)
print('\n Minutos:')
print(horarioAtual.minute)
print('\n Segundos:')
print(horarioAtual.second)
print('\n Microsegundos:')
print(horarioAtual.microsecond)

# Ajustar Data e Hora
print('\n Ajustando a Hora:')
horarioAtual = datetime.datetime.now()
print(horarioAtual)
horarioAtual = horarioAtual.replace(year=1500, month=4, day=22, hour=10, minute=30,second=0,
                                    microsecond=0)
print(horarioAtual)

dataUsuario = input('Escolha uma data (dd/mm/aaaa): ')
dataUsuario = dataUsuario.split('/')
print(dataUsuario)
dataUsuario = datetime.datetime(int(dataUsuario[2]), int(dataUsuario[1]), int(dataUsuario[0]))
print(dataUsuario)

horarioAtual = datetime.datetime.now()
fimSeculo = datetime.datetime(2100, 12, 31, 23, 59, 59)
tempoRestante = fimSeculo - horarioAtual
print(tempoRestante)
print(f'Restam {tempoRestante.days / 365} anos para virar o século')

# Delta de Data e Hora

horarioAtual = datetime.datetime.now()
print(horarioAtual)
tempoTrabalho = datetime.timedelta(30) # 30 dias
primeiroSalario = horarioAtual + tempoTrabalho
print(primeiroSalario)
