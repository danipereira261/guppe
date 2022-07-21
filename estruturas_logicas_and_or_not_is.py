"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    not
Operadores binários:
    -and, or , is
"""

ativo = False
logado = False

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if ativo or logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')

# É redundante, não é Pythonico
if ativo is True:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem vindo usuário')