"""
Listas
Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representados por colchetes: []
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

num = 100
if num in lista4:
    print(f'Encontrei o número: {num}')
else:
    print(f'Não encontrei o número: {num}')

print('************************************************')

# Podemos facilmente checar se determinado valor está contido na lista
letra = 'h'
if letra in lista5:
    print(f'Encontrei a letra: {letra}')
else:
    print(f'Não encontrei a letra: {letra}')

print('************************************************')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

print('************************************************')

# Podemos facilmente contar o número de ocorrências em um valor
print(lista1.count(1))
print(lista5.count('e'))

print('************************************************')

# Adicionar elementos em listas: Para adicionar elementos em listas, utilizamos a função append
# Com append nós só conseguimos adicionar um elemento por vez
print(lista1)
lista1.append(96)
print(lista1)

lista1.append([8, 3, 1])  # Coloca a lista como elemento único, sublista
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

print('************************************************')

# Podemos inserir um novo elemento na lista informando a posição do índice
# Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

print('************************************************')
# Podemos facilmente juntar duas listas, abaixo duas possibilidades:

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)

print('************************************************')

# Podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# slice fazendo a mesma coisa que o reverse acima
print(lista1[:: -1])
print(lista2[:: -1])

print('************************************************')

# Copia e tamanho de lista
lista7 = lista2.copy()
print(len(lista7))

print('************************************************')
# Podemos remover facilmente o último elemento de uma lista, o pop retorna o elemento removido
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice, os elementos a direita serão deslocados para a esquerda
print(lista5)
lista5.pop(2)
print(lista5)

print('************************************************')

# Podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

print('************************************************')

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

print('************************************************')

# Podemos facilmente converter uma string para uma lista, por padrão separa os elementos pelo espaço entre eles.
curso = 'Programação Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

curso = 'Programação, Python, Essencial'
print(curso)
curso = curso.split(',')
print(curso)

print('************************************************')

# Convertendo uma lista em uma string
lista7 = ['Programação', 'Python:', 'Essencial']
print(lista7)
curso = ' '.join(lista7)
print(curso)

curso = '$'.join(lista7)
print(curso)

print('************************************************')

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista8 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 4534345345]
print(lista8)
print(type(lista8))

print('************************************************')

# Iterando sobre listas

for elemento in lista8:
    print(elemento)

carrinho = []
produto = []

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

print('************************************************')

# Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

print('************************************************')

# Fazer acesso aos elementos de forma inversa
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

print('************************************************')
for cor in cores:
    print(cor)

print('************************************************')

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

print('************************************************')

# Gerar indice em um for

for k, v in enumerate(cores):
    print(k, v)

print('************************************************')

# Gerar chave e valor em uma lista
cores = list(enumerate(cores))
print(cores)

print('************************************************')
# Encontrar o indice de um elemento na lista
numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual indice da lista está o o valor 6
print(numeros.index(6))
# Em qual indice da lista está o valor 9
print(numeros.index(9))
# Retorna o valor do primeiro elemento encontrado
print(numeros.index(5))
# Podemos fazer a busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do indice 1
# Podemos fazer dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # buscar o indice do valor 8, entre os indices 3 a 6

print('************************************************')
# Revisao de slicing
# lista[inicio:fim:passo]
# Trabalhando com slice de listas com o parametro 'inicio'

print('************************************************')
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro 'fim'
print(lista[:2])  # Começa em 0, pega até o indice 2 -1

# Trabalhando com slice de lista com o parametro 'passo'
print(lista[1::2])  # Começa em 1, vai até o final, de 2 em dois

print('************************************************')
# Invertendo valores em uma lista
nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
# melhor forma de fazer
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

print('************************************************')

# Soma*, Valor Maximo*, Valor Minimoo*, Tamanho
# * Se os valores forem todos inteiros ou reais.
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho de lista

print('************************************************')
# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(type(tupla))

# Desempacotamento de listas

lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

print('************************************************')

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1 - Deep Copy

"""
Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente
independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy (cópia profunda)
"""
lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Forma 2 - Shallow Copy

lista_teste = [1, 2, 3]
print(lista_teste)

nova_teste = lista_teste
print(nova)

nova_teste.append(4)

print(lista_teste)
print(nova_teste)

"""
Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas após realizar 
a modificação em uma das listas, essa modificação se refletiu em ambas as listas. 
Isso em Python é chamado de Shallow Copy.
"""
