"""
Módulo Collections: Ordered Dict

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

"""
# Em um dicionário, a ordem de inserção dos elementos não é garantida.
# dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# for chave, valor in dicionario.items():
#     print(f'Chave: {chave} Valor: {valor}')

from collections import OrderedDict

# dicionario = OrderedDict({'c': 3, 'd': 4, 'e': 5, 'a': 1, 'b': 2})
# for chave, valor in dicionario.items():
#     print(f'Chave: {chave} Valor: {valor}')

# Entendendo a diferença entre o Dict e o OrderedDict
# Dicionários Comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True-> Já que a ordem dos elementos são importa para o dicionário

o_dict1 = OrderedDict({'a': 1, 'b': 2})
o_dict2 = OrderedDict({'b': 2, 'a': 1})
print(o_dict1 == o_dict2)  # False-> Já que a ordem dos elementos importa para o OrderedDict
