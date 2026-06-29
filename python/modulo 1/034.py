import random
import time 

numero = random.randint(0, 100) # o computador vai 'PENSAR'
print('-=-' * 30)
print(' vou pensar em um numero de 0 a 100, tenta acertar ai otario')
jogador = int(input(' em qual numero eu pensei? ')) # o jogador vai tentar ADVINHAR
print(' PENSANDO....... ')
time.sleep(3) #mostra o resultado dps de 3 segundos

if jogador == numero:
    print(' NEM A PAU Q TU ACERTOU MISERAVEL!!!!!!!!!!')
else:
    print(' ruim dms, eu pensei no numero {} e nao no numero {}'.format(numero, jogador))
