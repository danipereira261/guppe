"""
Reversed

OBS: A função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável.
A função reversed() retorna um iterável chamado List Reverse Iterator
"""
# Exemplos
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

# Podemos converter o elemento retornado para uma lista, Tupla ou Conjunto
res = print(list(reversed(lista)))
tupla = print(tuple(reversed(tupla)))
# Em conjuntos, não definimos a ordem dos elementos
conjunto_set = print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')  # end para não quebrar a linha

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Ja vimos como fazer isso de forma mais fácil com o uso do slice
print('Geek University'[:: -1])

# Podemos tambem utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

print('\n')

# Apesar que também já vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
