"""
Dicionários
OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.
Dicionários são representados por chaves {}.

OBS: Sobre dicionários
- Chave e valor são separados por dois pontos 'chave:valor'
- Tanto chave quanto valor podem ser de qualquer tipo de dado
- Podemos misturar tipos de dados

"""
# Criação de Dicionários
print(type({}))

# Forma 1 (Mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (Menos comum)
paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises2)
print(type(paises2))

# Acessamdo elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado o KeyError
pais = paises.get('py')
if pais:
    print(f'Encontrei o pais: {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = paises.get('ru', 'Não encontrado')
print(f'Encontrei o pais: {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla,
# dicionário como chaves de dicionário
# Tuplas por exemplo são bastante interessantes de ser utilizadas como chave de dicionário, pois as mesmas são imutáveis
localidades = {(35.6895, 39.6917): 'Escritório em Tókio',
               (40.7128, 74.0060): 'Escritório em Nova York',
               (37.7749, 122.4194): 'Escritório em São Paulo',
               }

print(localidades)
print(type(localidades))
print('**************************************************************')
