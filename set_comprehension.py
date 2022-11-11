"""
Set Comprehension
"""
# Exemplos

numeros = {num for num in range(1, 7)}
print(f'Números Set: {numeros}')

numeros = {x ** 2 for x in range(10)}
print(f' Números ao quadrado Set: {numeros}')

numeros = {x: x ** 2 for x in range(10)}
print(f' Números ao quadrado em um dicionário: {numeros}')

letras = {letras for letras in "Geek University"}
print(letras)
