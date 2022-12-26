"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

"""

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o primeiro valor: '))

print(max(val1, val2))
print(min(val1, val2))

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


musicas = [{'titulo': 'Depre', 'tocou': 5},
           {'titulo': 'Te amo demais', 'tocou': 2},
           {'titulo': 'Graveto', 'tocou': 10},
           {'titulo': 'Infiel', 'tocou': 50}
           ]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Como encontrar a música mais tocada e a menos tocada sem usar o min(), max() e lambda?

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 9999

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
