a = int(input(' digita um numero: '))
b = a*2
c = a*3
d = a**(1/2)
print('o seu numero e {} \n o dobro do seu numero e {} \n o triplo e {} \n e a raiz quadrada de {} raiz quadrada e {}'.format(a, b, c, a, d))

#podemos fazer sem variaveis
a = int(input(' digita um numero: '))
print('o seu numero e {} \n o dobro do seu numero e {} \n o triplo e {} \n e a raiz quadrada de {} e {}'.format(a, (a*2), (a*3), a, pow(a, (1/2))))