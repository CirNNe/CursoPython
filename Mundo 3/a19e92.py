#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime


perfil = dict()
perfil['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
perfil['idade'] = datetime.now().year - nasc
perfil['ctps'] = int(input('CTPS: '))
if perfil['ctps'] != 0:
    perfil['ano contratacao'] = int(input('Ano da contratação: '))
    perfil['salario'] = float(input('Salário: '))
    perfil['aposentadoria'] = perfil['idade'] + ((perfil['ano contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in perfil.items():
    print(f'{k}: {v}')

