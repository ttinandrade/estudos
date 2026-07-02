nota1 = float(input('qual foi sua primeira nota? '))
nota2 = float(input('qual foi sua segunda nota? '))

media = (nota1 + nota2)/2

print(' a media das suas notas sao {}'.format(media))

if media > 7:
    print('parabens voce esta aprovado')
elif  media >= 5 and media < 7:
    print('voce esta em recupecao')
else:
    print('infelizmente voce reprovou')
