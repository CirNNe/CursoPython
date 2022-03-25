'''
sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo.upper() != 'M' and sexo.upper() != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Sexo {} registrado com sucesso!'.format(sexo))
'''

# Revisado:

sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
