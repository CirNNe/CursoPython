# DICIONÁRIOS:

dados = dict()
dados = {
    'nome': 'Higor',
    'idade': 25
}
print(dados['nome'], dados['idade'])
dados['sexo'] = 'M'
dados['nome'] = 'Jão'
del dados['idade']
print(dados)

# -------------------------------------
print('-=' * 30)
# -------------------------------------

st = {
    'titulo': 'Star Wars',
    'ano': 1997,
    'diretor': 'George Lucas'
}
print(st)
print(st.values())
print(st.keys())
print(st.items())
for k, v in st.items():
    print(f'O {k} é {v}')

# ------------------------------------
print('-=' * 30)
# ------------------------------------

filme1 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}

filme2 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}

locadora = list()
locadora.append(filme1)
locadora.append(filme2)
print(locadora)
print(locadora[0])
print(locadora[1])

# -----------------------------------
print('-=' * 30)
# -----------------------------------

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

# ----------------------------------------------------
print('-=' * 30)
# ----------------------------------------------------
