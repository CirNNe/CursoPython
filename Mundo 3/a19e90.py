# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

boletim = dict()
boletim['nome'] = str(input('Nome: ')).strip()
boletim['media'] = float(input('Média: '))
print(f"O nome do aluno é: {boletim['nome']}")
print(f"A média do aluno é: {boletim['media']}")
if boletim['media'] < 6:
    print('Aluno reprovado!')
if 5 <= boletim['media'] <= 7:
    print('Aluno em recuperação!')
else:
    print('Aluno aprovado!')
