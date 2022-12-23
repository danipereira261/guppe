"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. O sort()
só funciona em listas.
Podemos utilizar o sorted com qualquer iterável.
Como o próprio nome diz, sorted() serve para ordernar.
"""

numeros = {0, 19, 7, 5, 10, 4, 6, 26, 1}
print(f"Original: {numeros}")

print(f"Ordenação: {sorted(numeros)}")  # O sorted, SEMPRE retorna uma lista com os elementos do iterável ordenados

print(f"Depois da ordenação: {numeros}")

# Adicionando parâmetros ao sorted()
numeros = [6, 1, 8, 2]
print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

musicas = [{'titulo': 'Depre', 'tocou': 5},
           {'titulo': 'Te amo demais', 'tocou': 2},
           {'titulo': 'Graveto', 'tocou': 10},
           {'titulo': 'Infiel', 'tocou': 50}
           ]

print(f'Ordenando do menor para o maior')
print(sorted(musicas, key=lambda musica: musica['tocou']))

print(f'Ordenando do maior para menor')
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
