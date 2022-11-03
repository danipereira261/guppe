"""
Módulo Collections - Default Dict


Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar um lambda
para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não
existe, essa chave será criada e o valor default será atribuído.

OBS: Lambdas são funções anônimas, que podem ou nõo receber parâmetros de entrada e retornar valores.
"""
# Dicionário comum
# dicionario = {'curso': 'Programação em Python: Essencial'}
# print(dicionario)
# print(dicionario['curso'])
# print(dicionario['outro']) # Key Error no dicionário comum

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])  # Aqui não gera Key Error
