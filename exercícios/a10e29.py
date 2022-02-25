velo = int(input('Digite a velocidade do carro: '))
multa = (velo - 80) * 7
if velo > 80:
    print('Sua velocidade ultrapassou 80km/h, você foi multado em R$: {:.2f}'.format(multa))