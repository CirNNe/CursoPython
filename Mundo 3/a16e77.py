# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('caderno',
            'livro',
            'garrafa',
            'copo',
            'monitor',
            'teclado')
for p in palavras:
    print(f'\nNa palavara {p} temos ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')
