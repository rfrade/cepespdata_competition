'''
Created on 3 de nov de 2017

@author: Rafael
'''

import unittest
from cepesp_python import cepesp

#numero_candidato = Numero na URNA
# Retorna um json com os 
def gerar_dados_mapa_brasil(turno = 1):
    df = cepesp.votos_x_candidatos(cargo=cepesp.CARGO.PRESIDENTE,
                                    ano=2014, 
                                    agregacao_politica=cepesp.AGR_POLITICA.CANDIDATO, 
                                    agregacao_regional=cepesp.AGR_REGIONAL.UF, 
                                    estado=None, 
                                    numero_candidato=None)

    #["UF", "COD_SIT_TOT_TURNO"]

    colunas = ["ANO_ELEICAO", "UF", "COD_SIT_TOT_TURNO", "SIGLA_UE", "NUM_TURNO", "CPF_CANDIDATO",
    "NOME_URNA_CANDIDATO", "SIGLA_PARTIDO", "COMPOSICAO_LEGENDA", "QTDE_VOTOS"]
#    print(df[df["NUMERO_CANDIDATO"].isin(['13', '45'])]);

    frame1 = df[colunas]
    frame2 = frame1.dropna(subset=['CPF_CANDIDATO']).query("UF != 'ZZ'");
    for id, row in frame2.iterrows():
#        print(frame2.iloc[id-1:id])
        print row;
    return frame2.to_json();

class TestaGeradorMapa(unittest.TestCase):
    def test_gerar_dados_mapa_brasil(self):
        gerar_dados_mapa_brasil()
