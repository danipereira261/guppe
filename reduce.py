"""
Reduce

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso, 99% das vezes
um loop for é mais legivel.

"""

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar a função reduce() precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n
print(res)
