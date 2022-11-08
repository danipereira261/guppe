"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension
[dado for dado in interável]

"""

# Exemplos
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

numeros_dobrados = [numero * 2 for numero in numeros]
print(numeros_dobrados)

nome = 'Geek University'
print([letra.upper() for letra in nome])

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([letra.title() for letra in amigos])

print([numero * 10 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in [1, 2, 3, 4, 5]])