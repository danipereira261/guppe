"""
Recebendo dados do usuário


"""
# Entrada de dados
print("Qual seu nome?")
nome = input()

# Exemplo de print antigo Python 2.x
# print("Seja bem vindo(a) %s" %nome)

# Exemplo de print antigo Python 3.x
# print("Seja bem vindo {} ".format(nome))

# Exemplo atual Python a partir da versão 3.7
print(f" Seja bem vindo {nome}")
print("Qual é a sua idade?")
idade = input()

# Processamento


# Saída de dados

# Exemplo de print antigo Python 2.x
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print antigo Python 3.x
# print("A {} tem {} anos ".format(nome, idade))

# Exemplo atual Python a partir da versão 3.7
print(f"A {nome} tem {idade} anos")
