"""
Zip

zip() -> Cria um iteravel (Zip Object) que agrega elemento de cada um dos iteraveis passados como entrada
em pares.
o zip() utiliza com parametro o menor tamanho em iteravel. Isso significa que se estiver trabalhando com interaveis de
tamanho diferentes, ira parar quando os elementos do menor iteravel acabar.

"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)
print(list(zip1))

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

#Dictionary Comprehension
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
