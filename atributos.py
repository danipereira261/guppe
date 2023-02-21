"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python dividimos os atributos em 3 grupos
    - Atributos de Instância
    - Atributos de Classe
    - Atributos de Dinâmicos

"""


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(f'A senha é: {self.__senha}')


# Atributos privados
user = Acesso('dpereira261@gmail.com', '123')
print('############################################################################################')

# Criando uma instância da classe e retornando para uma variável
user.mostra_senha()
print('############################################################################################')


class Produto:
    # Atributos de classe
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PS5', 'Video Game', 5000)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(Produto.imposto)  # Acesso correto atributo de classe
print('############################################################################################')
print(p1.id)
print(p2.id)
print('############################################################################################')

# Atributos dinâmicos - Atributos de instância que pode ser criado em tempo de execução
# OBS: O atributo dinâmico será exclusivo da instância que o criou
p3 = Produto('Arroz', 'Mercearia', 5.88)
# Criando um atributo dinâmico em tempo de execução
p3.peso = '5kg'  # Note que o atributo peso não existe na classe Produto
print(f'Nome: {p3.nome}, Descrição: {p3.descricao}, Valor: {p3.valor}, Peso: {p3.peso}')

print('############################################################################################')

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

del p3.peso
del p2.valor
del p2.descricao
print('############################################################################################')
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
