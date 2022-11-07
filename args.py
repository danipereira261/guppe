"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que começe com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo
Mas o que é o *args?
O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se qye tupla são imutáveis.
"""


# Entendendo o args
# def soma_todos_numeros(*args):
#     return sum(args)
#
#
# print(soma_todos_numeros())
# print(soma_todos_numeros(1, 2))
# print(soma_todos_numeros(2, 3))
# print(soma_todos_numeros(2, 3, 4))
# print(soma_todos_numeros(3, 4, 5, 6))
# print('*******************************')


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não sei quem você é'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info('University', 3.456987))
print('*******************************')


def soma_todos_numeros(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: O * asterico serve para que informemos ao Python que estamos passando
# como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados.
