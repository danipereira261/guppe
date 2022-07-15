""""
Tipo Float

Tipo rela, decimal

Casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a virgula.

"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(type(valor))

# Certo do ponto de vista do Float
valor = 1.44
print(type(valor))

# É possível
valor1, valor2 = 1, 44
print(type(valor1))
print(type(valor2))

# Podemos converter um float para um int
""""
OBS: Ao converter valores float para inteiros, nós perdemos a precisão.
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trabalhar com números complexos
variavel = 5j
print(variavel)
print(type(variavel))