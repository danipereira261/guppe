"""
Definindo Funções
- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma  saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a
função seja simplificada.

Em Python, a forma geral de definir uma função é:
def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por _ underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece;
Neste bloco, por ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def'. Abrimos o bloco de código com os dois
pontos ':' .

"""


# Exemplo de utilização de funções:
# cores = ['verde', 'amarelo', 'azul', 'branco']
# Utilizando a função integrada (Built-in) do Python print()
# print(cores)

# Definindo a primeira função

def diz_oi():
    print('oi!')
    print('********************')


# Chamada de execução da função
diz_oi()


# Exemplo 2

def cantar_parabens():
    print('Parabéns pra vc')
    print('Nessa data querida')
    print('Muitas Felicidades')
    print('Muitos anos de vida')
    print('********************')


for n in range(5):
    cantar_parabens()
