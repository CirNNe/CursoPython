from calendar import isleap

ano = int(input('Digite um ano: '))
if isleap(ano):
    print('É bissexto!')
else:
    print('Não é bissexto!')