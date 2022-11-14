"""
utilizando Lambdas

Expressões lambdas são funções anônimas.
"""

# # Função em Python
# def funcao(x):
#     return x * 3 + 1
#
#
# print(f'Função: {funcao(4)}')
# print(f'Função: {funcao(7)}')
#
# # Lambda
# calc = lambda x: x * 3 + 1
# print(f'Expressão Lambda:  {calc(4)}')
# print(f'Expressão Lambda:  {calc(7)}')

# strip() -> remove os espaços no início e no fim da palavra é o trim do SQL
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('daniele', ' pereira'))

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Artur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(f'Antes da ordenação {autores}')

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(f'Depois da ordenação {autores}')


# Função quadrática
# f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratica(a, b, c):
    """ Retorna a função f(x) = a * x ** 2 + b * x + c"""

    return lambda x: a * x ** 2 + b * x + c


print(f'Chamando a função: {geradora_funcao_quadratica(3, 0, 1)(2)}')
