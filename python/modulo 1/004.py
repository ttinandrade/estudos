# metodos de tipos

a = input('digite qualquer coisa: ')

print(' e um numero? {}'.format(a.isnumeric()))
print(' e uma letra? {}'.format(a.isalpha()))
print(' tem letras ou numeros? {}'.format(a.isalnum()))
print(' e so um espaço? {}'.format(a.isspace()))
print(' esta tudo em maiusculo? {}'.format(a.isupper()))
print('esta tudo em minusculo? {}'.format(a.islower()))