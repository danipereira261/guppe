"""
Módulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performance.
"""
from collections import deque

deq = deque('Geek')
print(deq)

# Adicionando elementos no deque

deq.append('y')
print(f'Adicionando um elemento no fim: {deq}')

deq.appendleft('k')
print(f'Adicionando um elemento no começo: {deq}')

deq.pop()
print(f'Removendo o último elemento: {deq}')

deq.popleft()
print(f'Removendo o primeiro elemento: {deq}')

deq.remove('G')
print(f"Removendo a letra 'G': {deq}")
