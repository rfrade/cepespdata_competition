'''
Created on 7 de nov de 2017

@author: Rafael
'''

import unittest
from cepesp_python import cepesp
import pandas as pd
import jsonpickle

# Tipos de grafico
GRAFICO_HISTORICO = "HV"  # Historico de votos


# numero_candidato = Numero na URNA
# Retorna um json com os 
def get_json_grafico(tipo_grafico=GRAFICO_HISTORICO,
                    cargo=cepesp.CARGO.PRESIDENTE,
                    ano=2014,
                    agregacao_politica=cepesp.AGR_POLITICA.CANDIDATO,
                    agregacao_regional=cepesp.AGR_REGIONAL.UF):
    
    if tipo_grafico == GRAFICO_HISTORICO:
        return get_json_grafico_historico_de_votos(cargo,
                                                   None,
                                                   agregacao_politica,
                                                   agregacao_regional)

'''Retorna o total e o percentual de votos por partido para determinado
cargo e localidade'''
def get_json_grafico_historico_de_votos(cargo=cepesp.CARGO.PRESIDENTE,
                    ano=2014,
                    agregacao_politica=cepesp.AGR_POLITICA.CANDIDATO,
                    agregacao_regional=cepesp.AGR_REGIONAL.UF):
    

    resultados = []
    
    pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
   # for k in range(2010,2010):#get_anos_presidente():
    df = cepesp.votos_x_candidatos(cargo=cepesp.CARGO.PRESIDENTE,
                                    ano=2010,
                                    agregacao_politica=1,#cepesp.AGR_POLITICA.PARTIDO,
                                    agregacao_regional=cepesp.AGR_REGIONAL.UF,
                                    estado=None)
    colunas = ['UF', "ANO_ELEICAO", "SIGLA_PARTIDO", "NUM_TURNO",
    "NOME_URNA_CANDIDATO", "QTDE_VOTOS"]
    
# .dropna(subset=['CPF_CANDIDATO'])and DATA_GERACAO_x != '28/01/2016'
    # datas : [2010, '23/03/2012', 2014, '28/01/2016']
    frame = df.dropna(subset=['NUMERO_CANDIDATO']).query("UF != 'ZZ' and NUM_TURNO == '1' and DATA_GERACAO_x != '28/01/2016'");

    # ["UF", "COD_SIT_TOT_TURNO"]
    count = 0
    
    for x in range(1,4):
        partido = Partido()
        partido.partido = "P" + str(x)
        partido.eleicoes = [2000, 2004, 2008]
        partido.votos_por_eleicao = [x*2, x*3, x*4]
        resultados.append(partido)

    return jsonpickle.encode(resultados, unpicklable=False);
''' for id, row in frame[colunas].iterrows():
        
    
        count += 1
        print(frame.iloc[id - 1:id])
    
        print(count) '''

def get_anos_presidente():
    return [1998, 2002, 2006, 2010, 2014]

def get_anos_prefeito():
    return [2000, 2004, 2008, 2012, 2016]

class Partido():
    
    def __init__(self, partido = None, eleicoes = None, votos_por_eleicao = None):
        self.partido = partido
        self.eleicoes = eleicoes
        self.votos_por_eleicao = votos_por_eleicao
    

class TestaGeradorGrafico(unittest.TestCase):

    def test_get_json_grafico_historico_de_votos(self):
        print(get_json_grafico_historico_de_votos())
