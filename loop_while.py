"""
Loop while

Forma geral

while expressão booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5
num < 10

OBS: Em um loop while é importante que cuidemos do critério de parada, para não gerar o loop infinito.
"""

num = 1
while num < 10:
    print(num)
    num = num + 1
print('******************************')

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')

print('******************************')





