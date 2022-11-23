"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
any() -> Retorna True se qualquer elemento do iterãvel for verdadeiro
"""

# Exemplo

# print(all([0, 1, 2, 3, 4]))
# print(all([1, 2, 3, 4]))

# nomes = ['Carlos', 'Cassia', 'Cassandra', 'Cesar']
#
# print(all([nome[0] == 'C' for nome in nomes]))

print(any([1, 2, 3, 4, 5]))
print(any([0, False, {}, (), []]))

nomes = ['Carlos', 'Cassia', 'Cassandra', 'Cesar']
print(any([nome[0] == 'C' for nome in nomes]))

print(any(num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0))
