from datetime import date

atual = date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano
if idade <= 9:
    print('A sua categoria é MIRIM')
elif idade <= 14:
    print('A sua categoria é INFANTIL')
elif idade <= 19:
    print('A sua categoria é JUNIOR')
elif idade <= 20:
    print('A sua categoria é SÊNIOR')
else:
    print('A sua categoria é MASTER')
