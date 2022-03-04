from datetime import date

totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Digite o ano que a pessoa nasceu: '))
    atual = date.today().year
    idade = atual - nasc
    if idade >= 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade e {} menores de idade'.format(totmaior, totmenor))
