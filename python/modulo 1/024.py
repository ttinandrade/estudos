import random

a = input(' primeiro nome: ')
b = input(' segundo nome: ')
c = input(' terceiro nome: ')
d = input(' quarto nome: ')

lista = [ a, b, c, d]
random.shuffle(lista)

print(lista)