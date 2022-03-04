nome = str(input('Digite seu nome: '))
if nome == 'Higor':
    print('Que nome bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Seu nome é bem polular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome.')
else:
    print('Seu nome é bem normal.')
print('Bom dia {}!'. format(nome))