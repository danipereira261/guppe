"""
O bloco try/except, utilizamos para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.


"""


# # Tratando erro genérico
# try:
#     geek()
# except:
#     print('Deu algum erro')

# # Tratando um erro especifico
#
# try:
#     geek()
# except NameError:
#     print('Voce esta utilizando uma funçao inexistente')


## Tratando um erro especifico com detalhes do erro
# try:
#     len(5)
# except TypeError as err:
#     print(f'A aplicaçao gerou o seguinte erro: {err}')


# try:
#     'geek'[9]
# except NameError as errn:
#     print(f'Deu NameError: {errn}')
# except TypeError as errt:
#     print(f'Deu TypeError: {errt}')
# except:
#     print('Deu um erro inesperado')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'nome': 'geek'}
print(pega_valor(dic, 'nome'))
