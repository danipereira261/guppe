"""
Como cientista de dados, algumas noções de geometria nunca são demais. Vamos atualizar alguns dos fundamentos.
Para um algoritmo de agrupamento sofisticado, você deseja encontrar a circunferência, , e a área, , de um círculo.
Quando o raio do círculo é r, você pode calcular e como:
Para usar a constante pi, você precisará do pacote math. Uma variável r já está codificada no script.
Preencha o código para calcular C e A e veja como as funções print() criam algumas impressões interessantes.
Calcule a circunferência do círculo e armazene-a em C.
Calcule a área do círculo e armazene-a em A.
"""
# Definition of radius
r = 0.43
# Import the math package
import math

# Calculate C
C = 0
C = 2 * r * math.pi

# Calculate A
A = 0
A = math.pi * r * r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

"""
Importação seletiva
As importações gerais, como importar matemática, disponibilizam para você todas as funcionalidades do pacote matemático.
No entanto, se você decidir usar apenas uma parte específica de um pacote, sempre poderá tornar sua 
importação mais seletiva:
da importação de matemática pi
Digamos que a órbita da Lua ao redor do planeta Terra seja um círculo perfeito, com um raio r (em km) definido 
no roteiro.

importação seletiva do pacote math onde você importa apenas a função radianos.
Calcule a distância percorrida pela Lua em 12 graus de sua órbita. Atribua o resultado a dist. 
Você pode calcular isso como r * phi, onde r é o raio e phi é o ângulo em radianos. 
Para converter um ângulo em graus para um ângulo em radianos, use a função radianos(), que você acabou de importar.
Imprimir dist.
"""

# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
