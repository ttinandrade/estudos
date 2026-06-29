v1 = int(input(' digita um valor: '))
v2 = int(input(' digita outro valor: '))
v3 = int(input(' digita mais um valor: '))

# verificando o menor valor
menor = v1

if v2<v1 and v2<v3:
    menor = v2

if v3<v1 and v3<v2:
    menor = v3

#verificando o maior valor

maior = v1 

if v2>v1 and v2>v3:
    maior = v2

if v3>v1 and v3>v2:
    maior = v3

print(' o menor valor foi {}'.format(menor))
print(' o maior valor foi {}'.format(maior))