"""
Documentando funções com Docstrings

OBS: Podemos ter acesso de uma documentação de uma função em Python utilizando a propriedade especial __doc__
Podemos ainda fazer acesso a documentação com a função help()
"""


# Exemplos

def diz_oi():
    """ Uma função simples que retorna a string 'Oi!'"""
    return f'Oi!'


print(diz_oi())


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á potencia informada.
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2.
    :return: Retorna o exponencial de 'numero' por potencia.
    """
    return numero ** potencia


print(exponencial(2))
