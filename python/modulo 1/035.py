import colorama

v = float(input(' qual a velocidade seu carro estava? '))

if v <=80:
    print(colorama.Fore.GREEN + ' esta tudo certo, tenha um bom dia e cuidado na pista ')
    
else:
    print(colorama.Fore.RED + ' amigo o limite e 80km/h seu louco, MULTADO!')
    multa = (v - 80) * 7
    print(' voce deve pagar {}R$ de multa'.format(multa))