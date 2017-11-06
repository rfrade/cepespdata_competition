'''
Created on 3 de nov de 2017

Consulta os dados do TSE por meio da API cepesp-python
e preenche as tabelas do banco de dados.

@author: Rafael
'''
import unittest;
from cepesp_python import cepesp

def importa_tse():
    print(cepesp.votos_x_legendas())


class TestaImportacao(unittest.TestCase):
    def test_importa_tse(self):
        importa_tse()
        