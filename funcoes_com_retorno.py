from random import random
from datetime import *
import time

"""
Funções com retorno

Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execução da função;
2- Podemos ter, em uma função, diferentes returns;
3- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
"""


# Exemplo função
def quadrado_de_7():
    return 7 * 7


quadrado_de_7()
print(f'Retorno da função: {quadrado_de_7()}')


def nova_funcao():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.2


print(nova_funcao())


def outra_funcao():
    return 2, 3, 4, 5


print(outra_funcao())


def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


def start_process():
    dh_inic_exec_process = str(time.strftime('%d%m%Y %H:%M:%S'))
    dh_fim_exec_proc = str(time.strftime('%d%m%Y %H:%M:%S'))
    return f'Começou em: {dh_inic_exec_process} Terminou em: {dh_fim_exec_proc}'


print(start_process())
