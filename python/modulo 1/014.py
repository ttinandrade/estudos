largura = float(input('larguda da sua parede: '))
altura = float(input('altura da sua parede: '))
area = largura * altura


print(' a sua parede tem a dimensao de {}x{} e sua areaa e de {}m²'.format( largura, altura, area))

tinta = area / 2 

print(' para pintar essa parede precisamos de {}l de tinta'.format(tinta))