"""
Try / Except / Else / Finally

Dica de quando e onde tratar o código:
Toda entrada deve ser tratada

# Else -> É executado somente se não ocorrer o erro.



"""


# try:
#     num = int(input('Digite um numero:'))
# except ValueError as err:
#     print(f'Valor incorreto: {err}')
# else:
#     print(f'Voce digitou: {num}')


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

print(dividir(num1, num2))
