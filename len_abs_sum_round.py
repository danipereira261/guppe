"""
Len, Abs, Sum, Round

*Len
len() -> retorna o tamanho (ou seja, o número de itens) de um iterável

*Abs
abs() -> retorna o valor absoluto de um número inteiro ou real, seria o seu valor real sem o sinal.

*Sum
sum() -> recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial.
OBS: O valor inical default é 0

*Round
round() -> retorna um número arredondado para n digito de precisão após a casa, decimal. Se a precisão não for
informada retorna o inteiro mais próximo da entrada.


"""

print(abs(-5))
# Sem valor inicial
print(sum([1, 2, 3, 4, 5]))
# Com valor inicial (exemplo, somar os valor mais uma taxa)
print(sum([1, 2, 3, 4, 5], 5))

print(round(1.212121, 2))
print(round(1.6))
