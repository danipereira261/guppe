"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

for chave, valor in receita.items():
    print(f'{chave} {valor}')

# Soma, *Valor Máximo, *Valor Mínino, Tamanho
# * Se os valores forem inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

