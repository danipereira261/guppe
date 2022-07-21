"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variaveis globais são reconhecidas, seu escopo compreende, todo o programa.

2 - Variaveis locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variaves em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que
ao declararmos uma variavel, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesmo.
"""

numero = 42
print(numero)
print(type(numero))