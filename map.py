"""
Map

Com map fazemos mapeamento de valores para uma função

OBS: Depois da primeira utilização do resultado da função map(), ele zera.
"""

import math


def area(r):
    """Calcula a área de um circulo com raio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo o iterável.
# Retorna um Map Object.
areas = map(area, raios)
print(f'Map: {list(areas)}')
#
# # Map com Lambda
print(f'Map com Lambda: {list(map(lambda r: math.pi * (r ** 2), raios))}')

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]

print(f'Map com Lambda: {list(map(lambda dado: (dado[0], (9 / 5) * dado[1] + 32), cidades))}')


# Função que transforma Grau Celsius em Fahrenheit
# Função equivalente ao Map com Lambda, utilizei o parâmetro lista, que será a lista passada ao chamar a função
# o retorno da função será a nova lista com as modificações necessários
def c_para_f(lista):
    new_cidades = []
    for dado in lista:
        new_cidades.append((dado[0], (9 / 5) * dado[1] + 32))
    return new_cidades


print(c_para_f(cidades))
