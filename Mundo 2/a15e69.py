cont18 = contm = contf = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if sexo in 'M':
        contm += 1
    if sexo == 'F' and idade < 20:
        contf += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja encerrar? [S/N]: ')).strip().upper()[0]
    if parar == 'S':
        break
print(f'''
FIM DO PROGRAMA
Total de {cont18} pessoas com mais de 18 anos;
Total de {contm} homens cadastrados;
Total de {contf} mulheres com menos de 20 anos.
''')
