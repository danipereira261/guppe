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

# slice faz a mesma coisa que o reverse
print(lista1[:: -1])
print(lista2[:: -1])
