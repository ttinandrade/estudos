emprestimo = float(input('qual o valor da casa? '))
salario = float(input('qual o seu salario? '))
anos = int(input('quantos anos de financiamento? '))

prestacao = emprestimo / (anos * 12)
minimo = salario * 30 / 100

print('para pagar uma casa de {}R$ em {} anos a prestacao sera de {:.2f}R$ '.format(emprestimo, anos, prestacao), end='')

if prestacao <= minimo:
    print('emprestimo pode ser CONCENDIDO!')
else:
    print('emprestimo NEGADO!')
