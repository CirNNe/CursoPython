km_viagem = int(input('Quantidade de km da viagem: '))
if km_viagem <= 200:
    preco = km_viagem * 0.50
    print('O valor da passagem é de R$: {:.2f}'.format(preco))
else:
    preco = km_viagem * 0.45
    print('O valor da passagem é de R$: {:.2f}'.format(preco))