"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência á Teoria dos Conjuntos da Matemática.
- Aqui no Pynthon os Conjuntos são chamados de Sets.
Disto isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indicce, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
 - Um dicionário tem chave/valor;
 - Um conjunto tem apenas valor;

"""
# Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro
# e não fara parte do conjunto.

# Forma 2  - Mais comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 3}
print(s)
print(type(s))

print(s)
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que além de não termos valores duplicados, não temos ordem.

# Não aceitam valores duplicados
conjunto = {99, 2, 34, 2, 23, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} qtd: {len(conjunto)}')
dicionario = {99: 'id', 2: 'id', 34: 'id', 2: 'id', 23: 'id', 12: 'id', 1: 'id', 44: 'id', 5: 'id', 34: 'id'}
print(f'Dicionário: {dicionario} qtd {len(dicionario)}')

# Aceitam valores duplicados
lista = [99, 2, 34, 2, 23, 12, 1, 44, 5, 34]
print(f'Lista: {lista} qtd {len(lista)}')
tupla = (99, 2, 34, 2, 23, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} qtd {len(tupla)}')

# Assim como todo outro conjunto em Python podemos colocar todos os tipos de dados misturados em Sets.

s = {1, 'b', True, 34, 22, 44}
print(s)
print(type(s))

# Podemos iterar em Sets
for valor in s:
    print(valor)

# Usos interessantes com Sets
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou um museu e os visitantes informam
# manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(f' Lista: {len(cidades)}')

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? Faria um loop na lista...?
# Podemos utilizar o Set para isso:
print(f' Set: {len(set(cidades))}')

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Remover elementos em um conjunto
print(s)
# Forma 1
ret = s.remove(3)  # Não é índice! Informamos o valor a ser removido
print(ret)
print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2
s.discard(22)
print(s)

# Copiando um conjunto para outro
s = {1, 2, 3}
print(f'Original: {s}')
# Forma 1 - Deep Copy
novo = s.copy()
print(f'Cópia: {novo}')
novo.add(4)
print(f'Cópia: {novo}')
print(f'Original: {s}')

# Forma 2 - Shallow Copy
s = {1, 2, 3}
novo = s
print(f'Novo: {novo}')
novo.add(4)
print(f'Novo: {novo}')
print(f'S: {s}')

# Podemos remover todos os itens de um conjunto
s = {1, 2, 3}
print(f'Antes: {s}')
s.clear()
print(f'Depois: {s}')

# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2  - Utilizando o pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(f'Utilizando intersection: {ambos1}')

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(f'Utilizando &: {ambos2}')

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(f'Utilizando difference: {so_python}')
so_java = estudantes_java.difference(estudantes_python)
print(f'Utilizando difference: {so_java}')

# Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# * Se os valores todos inteiros ou reais

s = {1, 2, 4, 5, 6, 7}
print(f'Soma: {sum(s)}')
print(f'Valor Máximo: {max(s)}')
print(f'Valor Mínimo: {min(s)}')
print(f'Tamanho: {len(s)}')
