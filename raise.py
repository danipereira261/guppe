"""
Levantando os próprios erros com o raise

raise -> Lança exceções
OBS: O raise não é uma função, é uma palavra reservada. O raise, assim como o return , finaliza a função, nada após o
raise é executado.
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'rosa')
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore("Geek", 'preto')
