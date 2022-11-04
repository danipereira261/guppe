"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados;

- Diferença entre PARÂMETRO e ARGUMENTO

Parâmetro-> sõo variáveis declaradas na definição da função;
Argumento-> são dados passados durante a execução de uma função;

- Argumentos Nomeados(Keyword Arguments)
Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem;

"""


def quadrado(numero):
    return numero * 7


print(f'Função quadrado: {quadrado(5)}')


def somar(a, b):
    return a + b


print(f'Função somar: {somar(1, 2)}')


def multiplicar(num1, num2):
    return num1 * num2


print(f'Função multiplicar: {multiplicar(2, 2)}')


def nome_completo(nome, sobrenome):
    return f'O nome completo é {nome} {sobrenome}'


nome = 'Daniele'
sobrenome = 'Pereira'
# Argumentos Nomeados(Keyword Arguments)
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Barreto', nome='Felipe'))


def somar_impares(lista):
    total = 0
    for n in lista:
        if n % 2 != 0:
            total = total + n
    return total


lista = [1, 2, 3, 4, 5, 6, 7]

print(somar_impares(lista))
