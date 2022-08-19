def calc(a, b):
    resultado = a + b
    print(resultado)


def n(nome):
    if nome == 'Daniele':
        print('Sou eu')
    else:
        print('Não sou eu')


def teste(nome):
    print(f'{nome}')


if __name__ == '__main__':
    calc(1, 2)
    n('Felipe')
    teste('geek')
