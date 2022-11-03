"""
Módulo Collections - Named Tuple

Named Tuple-> São tuplas, diferenciadas, onde, específicamos nome e parâmetros.

"""

from collections import namedtuple

# Precisamos definir o nome e parâmetros
cachorro = namedtuple('cachoro', ['idade', 'raca', 'nome'])
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
