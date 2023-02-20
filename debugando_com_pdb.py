"""
Debuggando com PDB
PDB -> Python Debugger

Comandos básicos para o PDB

l lista onde estamos no código
n próxima linha
p imprime variável
c continua a execuçao - finaliza o debugging


"""
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
nome_completo = nome + ' ' + sobrenome
pdb.set_trace()
curso = 'Programacao em Python: Essencial'
final = nome_completo + 'faz curso ' + curso