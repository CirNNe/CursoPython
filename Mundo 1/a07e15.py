km = float(input('Quantos km pecorridos? '))
dias = int(input('Quantos dias alugados? '))
valor = (km * 0.15) + (dias * 60)
print('O preço a pagar pelo aluguel é de R${:.2f}'.format(valor))