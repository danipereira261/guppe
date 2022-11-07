"""
**kwargs

Poderíamos chamar este parâmetro de **xix, mas por convenção chamamos de **kwargs
Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.

Nas nossas funções, podemos ter (nesta ordem):
1. Parâmetros obrigatórios;
2. *args;
3. Parâmetros default (não obrigatórios)
4. **kwargs

"""


# Exemplo
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
print('****************************************************************************')
cores_favoritas()
# OBS: Os parâmetros *args e **kwargs não são obrigatórios
print('****************************************************************************')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))
print('****************************************************************************')


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print('Casado')
        print(kwargs)


minha_funcao(8, 'Julia')
print('****************************************************************************')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
print('****************************************************************************')
minha_funcao(34, 'Felipe', eu='nao', voce='vai')
print('****************************************************************************')
minha_funcao(19, 'Julia', 9, 4, 3, java=False, python=True)
print('****************************************************************************')


# OBS: O ** asterico serve para que informemos ao Python que estamos passando
# como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes desempacotar esses dados.

# Desempacotar o **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))

