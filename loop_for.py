"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(11, 10)

# Exemplo for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

print('****************************************')

# Exemplo for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

print('****************************************')

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)

print('****************************************')

for i, v in enumerate(nome):
    print(nome[i])

print('****************************************')

for indice, letra in enumerate(nome):
    print(letra)

print('****************************************')

# Com o _ eu descarto o indice
for _, letra in enumerate(nome):
    print(letra)

print('****************************************')

for valor in enumerate(nome):
    print(valor)

print('****************************************')

qtd = int(input('Quantas vezes esse loop tem que rodar: '))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n} / {qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('****************************************')

# Tabela de emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Unicode Original: U+1F60D
# Unicode Modificado: U0001F60D

emoji = '\U0001F60D'

for n in range(1, 10):
    print(f'{emoji * n}')

print('****************************************')

emoji = ['\U0001F60D', '\U0001F609']
for n in emoji:
    print(f'{n * len(emoji)}')

print('****************************************')
