largura_p = float(input('Largura da parede: '))
altura_p = float(input('Altura da parede: '))
a = largura_p * altura_p
t = a / 2
print('A área da parede é de {:.2f} m² e a quantidade de tinta necessária para pinta-la é de {:.2f} litros'.format(a, t))