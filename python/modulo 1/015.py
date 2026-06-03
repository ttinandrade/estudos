produto = float(input('qual e o valor do produto? R$'))
novo = produto - ( produto * 5 / 100)

print(' o produto que custava R${} na promoçao de 5% vai custar R${}'.format(produto, novo))