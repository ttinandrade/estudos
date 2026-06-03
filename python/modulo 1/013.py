# conversor de moedas

a = float(input(' quanto vc tem na carteira? R$'))
dolar = a / 3.27

print(' com R${:.2f} voce consegue comprar US${:.2f}.'.format(a, dolar))