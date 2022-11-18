"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção
filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
de acordo com a função.

Após utilizado dos dados de filter() eles são excluidos da memória
"""

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados por algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, - 0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

# A função filter() recebe dois parâmetros, sendo uma função e um iterável.
res = filter(lambda valor: valor > media, dados)
print(list(res))

paises = ['', 'Argentina', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Outra opção
res = filter(lambda pais: pais != '', paises)
print(list(res))

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter

# Opção 1
inativos = filter(lambda user: len(user['tweets']) == 0, usuarios)
print(list(inativos))

# Opção 2
inativos = filter(lambda user: not user['tweets'], usuarios)
print(list(inativos))

nomes = ['Ana', 'Vanessa', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
