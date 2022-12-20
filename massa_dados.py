import csv
import names
from rstr import rstr
from string import digits
import datetime
import re
from random import randint
from time import ctime

# def data_registro():
#     ''':return data'''
#     seconds = int('{}{}'.format(
#         randint(12, 14),
#         rstr(digits, 8)
#     ))
#     return ctime(seconds)

def get_id():
    ''' retorna string de placa'''
    while True:
        return '{}'.format(
            ("organico"),
            ("reciclavel"),

        )





def gen_massa(qlinhas, cvsname):
    '''cria cvsname com a quantidade de linhas informadas em qlinhas '''
    try:
        header = "cpf, matricula, sobrenome, nome, email, data de ingresso"
        with open(cvsname, 'w') as file:
            csvhandler = csv.writer(file)
            csvhandler.writerow(header.split(', '))
            for i in range(qlinhas):
                # date = data_registro()

                linha = '{}'.format(
                    get_id()
                    )
                csvhandler.writerow(linha.split(','))
        return True
    except:
        raise


if __name__ == '__main__':
    print(gen_massa(500, 'file.csv'))