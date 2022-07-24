"""
Ranges
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para tranalhar melhor com os loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória.

Formas gerais

#Forma 1

range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo 1 em 1)
"""

# Forma 1
for num in range(11):
    print(num)

print('*************************')

# Forma 2
for num in range(1, 11):
    print(num)

print('*************************')

# Forma 3 ( valor_inicio, valor_parada, passo)
for num in range(0, 11, 2):
    print(num)

print('*************************')

# Forma 4 (valor_inicio, valor_parada, passo(invertido))
for num in range(10, 0, -1):
    print(num)

print('*************************')