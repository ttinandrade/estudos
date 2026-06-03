dias = int(input(' quantos dias o carro ficou alugado? '))
km = float(input(' quantos km foi rodado? '))
pago = (dias * 60 ) + ( km * 0.15)

input(' o total a pagar e de {:.2f}'.format(pago))