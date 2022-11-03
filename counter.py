"""
Módulo Collections - Counter (Contador)
Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor e quantidade
de ocorrências desse elemento.
"""

# Utilizando o Counter

from collections import Counter

# Exemplo 1
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 11, 1, 2, 4, 4, 5, 6, 8, 9, 10, 45, 65, 70, 65, 70, 25]
res = Counter(lista)
print(type(res))
print(res)

# Veja que para elemento da lista, o Counter criou uma chave e como valor colocou a quantidade de ocorrências.
# Counter({1: 2, 4: 2, 65: 2, 70: 2, 11: 1, 2: 1, 5: 1, 6: 1, 8: 1, 9: 1, 10: 1, 45: 1, 25: 1})

# Exemplo 2
print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

# Exemplo 3
texto = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
palavras = texto.split()
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
