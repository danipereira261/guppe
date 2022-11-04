"""
Funções com parâmetro padrão

- Para que um parâmetro de uma função se torne opcional, basta atribuir um valor a ele;
- Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar no final da declaração;
- Por quê utilizar parâmetros com valor default?
    - Nos permite ser mais flexíveis ns funções;
    - Evita erros com parâmetros incorretos;
    - Nos permite trabalhar com exemplos mais legíveis de código;
- Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência;
- Não podemos realizar OPERAÇÕES(+, -, * , /) com variáveis globais sem inicializar;
- Evitar variáveis globais;

"""


def exponenciacao(numero, potencia=2):
    return numero ** potencia


print('*******************************************************************************')
print(f' Função com o parâmetro obrigatório e opcional: {exponenciacao(4, 3)}')
print('*******************************************************************************')
print(f' Função apenas com o parâmetro obrigatório: {exponenciacao(4)}')
print('*******************************************************************************')


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem-vindo Instrutor Geek'
    elif nome == 'Geek':
        return f'Pensei que você era instrutor'
    return f'Olá {nome}'


print(f"Função sem passar os argumentos: {mostra_informacao()}")
print('*******************************************************************************')
print(f"Função passando os dois argumentos: {mostra_informacao('Geek', instrutor=True)}")
print('*******************************************************************************')
print(f"Função passando apenas o primeiro argumento: {mostra_informacao('Genivaldo')}")
print('*******************************************************************************')
print(f"Função passando apenas o segundo argumento: {mostra_informacao(instrutor=True)}")
print('*******************************************************************************')


def somar(num1, num2):
    return num1 + num2


def mat(num1, num2, func=somar):
    return func(num1, num2)


def subtrair(num1, num2):
    return num1 - num2


print(f"Função passando outra função como argumento: {mat(2, 2, func=subtrair)}")
print('*******************************************************************************')
print(f"Função sem o argumento opcional: {mat(2, 2)}")
print('*******************************************************************************')




