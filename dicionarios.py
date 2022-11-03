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

# Adicionar elementos em um dicionário

receita = {"jan": 100, "fev": 120, "mar": 300}
print(receita)
print(type(receita))

# Forma 1  -mais comum
receita["abr"] = 350
print(receita)

# Forma 2
receita.update({"mai": 500})
print(receita)

# update serve tanto para incluir quanto para alterar
# dicionários não aceitam chaves repetidas

# Remover dados de um dicionário
receita = {"jan": 100, "fev": 120, "mar": 300}
print(receita)
# Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)

# OBS: Aqui precisamos informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2
del receita['fev']
print(receita)
# OBS: Neste caso o valor removido não é retornado

# Dicionário dentro de lista, desta forma facilmente adicionamos ou removemos produtos no carrinho
carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário (zerar dados)
#d.clear()
#print(d)

# Copiando um dicionário para outro
# Forma 1 Deep Copy
#novo = d.copy()
#print(novo)
#novo['d'] = 4
#print(d)
#print(novo)

# Forma 2 Shallow Copy
#novo = d
#print(novo)
#novo['d'] = 4
#print(d)
#print(novo)

# Forma não usual de criar dicionários

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O metodo fromkeys recebem dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado





