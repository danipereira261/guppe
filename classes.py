"""
POO - Classes
Em POO, classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.
"""



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


teste = Produto('notebook', 1200)
