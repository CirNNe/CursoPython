'''
idade = int(input('Digite sua idade: '))
if idade < 18:
    tempo = 18 - idade
    print('Ainda falta {} para o alistamento, calma!'.format(tempo))
elif idade == 18:
    print('Você tem {} e chegou a hora de alistar!'.format(idade))
else:
    tempo = idade - 18
    print('Já passou {} do prazo para o alistamento!'.format(tempo))
'''

from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
if idade < 18:
    tempo = 18 - idade
    print('Você tem {} anos e ainda falta {} ano para o alistamento'.format(idade, tempo))
elif idade == 18:
    print('Voce tem {} anos e esta na hora de se alistar.'.format(idade))
else:
    tempo = idade - 18
    print('Você tem {} anos e já passou {} ano(s) do tempo para se alistar.'.format(idade, tempo))
