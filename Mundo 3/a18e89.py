# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()

while True:

    aluno = str(input('Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], media])

    continuar = str(input('Deseja adicionar outro aluno [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Comando inválido, digite novamente [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

for i, a in enumerate(ficha):
    print(f'Nº {i} / Aluno(a) {a[0]} / Média: {a[2]}')

while True:

    pesquisa = int(input('Digite o número do aluno para ver sua nota individualmente [999 interrompe]: '))
    
    if pesquisa == 999:
        break
    
    if pesquisa <= len(ficha) - 1:
        print(f'Aluno {ficha[pesquisa][0]} / Nota 1: {ficha[pesquisa][1][0]} / Nota 2: {ficha[pesquisa][1][1]}')

