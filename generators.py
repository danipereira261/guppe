"""
Generator Expression

Generator em relação a List Comprehension é mais performática.
"""
from sys import getsizeof

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(list_comp)

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
print(set_comp)

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(dict_comp)

# Gerando uma lista de números com Genarator
gen = getsizeof(x * 10 for x in range(1000))
print(gen)

print(f'Para a mesma tarefa gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Genarator Expression: {gen} bytes')


# Iterando no Genarator Expression

gen = (x * 10 for x in range(1000))

for n in gen:
    print(n)