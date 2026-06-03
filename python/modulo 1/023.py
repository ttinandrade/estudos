import random

a = input(' primeiro aluno: ')
b = input(' segundo aluno: ')
c = input(' terceiro aluno: ')
d = input(' quarto aluno: ')

lista = [a, b, c, d]
sorteio = random.choice(lista)

print(' o aluno escolhido foi: {}'.format(sorteio))
