# aumento multiplos

salario = float(input(' qual seu salario? '))

if salario <=1250:
    aumento = salario + ( salario * 15 / 100)
else:
    aumento = salario + ( salario * 10 / 100)

print(' quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, aumento))