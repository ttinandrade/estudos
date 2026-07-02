import datetime

ano = datetime.date.today().year

nasc = int(input(' ano de nascimento: '))
idade = ano - nasc

print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))

if idade == 18:
    print(' voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade 
    print(' voce ainda nao tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print(' voce ja deveria ter se alistado a {} anos'.format(saldo))