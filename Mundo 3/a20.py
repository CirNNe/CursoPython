# FUNÇÕES:

# FUNÇÃO DE SOMA:
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

# Programa principal:
soma(4, 5)
soma(a=8, b=9)
soma(b=2, a=1)


# DESEMPACOTAR PARÂMETROS:
def contador (*num): # indica que não sabe quantos parâmetros serão passados.
    tamanho = len(num) # vai ler o tamanho da tupla que a função cria ao passar os parâmetros.
    print(f'A quantidade de números é: {tamanho}')

# Programa principal:
contador(2, 1, 7)


# TRABALHANDO COM LISTAS:
def dobro(listinha):
    posicao = 0
    while posicao < len(listinha): # enquanto a posição for menor que o tamanho da lista passada:
        listinha[posicao] *=  2 # o valor na posição atual vai dobrar seu valor
        posicao += 1 # e a posição avança até chegar ao fim da lista

# Programa principal:
valores = [6, 3, 9, 1, 0, 2] # lista
dobro(valores) # o função irá atuar na lista acima
print(valores) # printar a lista com os valores dobrados
