# Primeiro exmplo:

nome = str(input('Digite seu nome: ')).strip()
if 'HIGOR' in nome.upper():
    print('Que nome top, meu parceirinho!')
else:
    print('Que nome normalzinho.')
print('Bom dia, {}!'.format(nome))


# Segundo exemplo:

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi: {}'.format(m))
if m >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
