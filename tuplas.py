"""
Tuplas

São bastante parecidas com listas.
Existem basicamente duas diferenças:
1 - As tuplas são representadas por parênteses ()
2- As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda modificação em uma tupla
gera uma nova tupla.
3- Tuplas são definidas pela vírgula e não pelo uso do parênteses



"""

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Tupla com apenas um elemento
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

print('*******************************************')

# Podemos gerar uma tupla dinâmicamente com o range (inicio, fim, passo)
tupla5 = tuple(range(11))
print(type(tupla5))

print('*******************************************')
# Desempacotamento de tupla
tupla6 = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla6
print(escola)
print(curso)

print('*******************************************')
# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis
# Soma, Valor Máximo, Valor Mínimo (se os valores forem inteiros ou reais) e Tamanho

tupla7 = (1, 2, 3, 4, 5, 6)
print(sum(tupla7))
print(max(tupla7))
print(min(tupla7))
print(len(tupla7))

print('*******************************************')
tupla8 = (1, 2, 3)
print(tupla8)
tupla9 = (4, 5, 6)
print(tupla9)

print(tupla8 + tupla9)  # Concatenando (Tuplas são imutáveis)
print(tupla8)
print(tupla9)

tupla9 = tupla8 + tupla9  # Tuplas são imutáveis, mas podemos sobreescrever seus valores
print(tupla9)

print('*******************************************')
# Verificar se determinado elemento está contido na tupla
tupla10 = (1, 2, 3)
print(3 in tupla10)

tupla11 = (1, 2, 3)
for n in tupla11:
    print(n)

for i, v in enumerate(tupla11):
    print(i, v)

print('*******************************************')

# Contando elementos dentro de uma tupla
tupla12 = ('a', 'b', 'c', 'e', 'a')
print(tupla12.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

print('*******************************************')

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
         'novembro', 'dezembro')

# O acesso de elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice está um elemento está na tupla
print(meses.index('junho'))

# Slicing
# tupla[inicio:fim:passo]
print(meses[5:])
print(meses[0:12])
print(meses[0:12:2])

print('*******************************************')
# Por que utilizar tuplas?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro. Isso porque trabalhar com elementos imutáveis traz segurança para o código.

# Copiando um tupla para outra. Na tupla não temos o problema do Shallow Copy

tupla13 = (1, 2, 3)
print(tupla13)
nova = tupla13
print(nova)
print(tupla13)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla13)

print('*******************************************')
