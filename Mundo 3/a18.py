# Adicionando listas dentro de uma lista

dados = ('Maria', 20)
pessoas = list()
pessoas.append(dados[:]) # [:] cria uma cópia da lista dados dentro da lista pessoas
print(pessoas)
print('-' * 30)

# -------------------------------------------------------------------------------------

galera = (('Maria', 20), ('João', 25), ('Pedro', 22))
print(galera[0])
print(galera[2][1])
print(galera)
for p in galera:
    print(p)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
print('-' * 30)

# -------------------------------------------------------------------------------------

gente = list()
informacoes = list()
for c in range(1, 4):
    informacoes.append(str(input('Nome: ')))
    informacoes.append(int(input('Idade: ')))
    gente.append(informacoes[:])
    informacoes.clear()
print(gente)
print(informacoes)
for g in gente:
    if g[1] >= 18:
        print(f'{g[0]} é maior de idade.')
print('-' * 30)

# -------------------------------------------------------------------------------------

