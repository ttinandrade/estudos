dist = float(input(' qual a distancia da sua viagem? '))

print(' voce esta prestes a começar uma viagem  de {}km'.format(dist))

if dist <=200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
    
print(' e o preco da sua viagem vai ser de {:.2f}R$'.format(preco))