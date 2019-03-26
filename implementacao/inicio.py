from cepesp_python import cepesp
from flask import Flask, render_template, request
import gerador_de_graficos

app = Flask(__name__)

@app.route('/tela_mapas')
def carregar_tela_mapas():
    return render_template('/tela_mapas.html')

@app.route('/cepesp')
def carregar_tela_grafico():
    return render_template('/tela_graficos.html')

@app.route('/gerarMapa')
def gerarMapa():
    print(request.args.get('grafico'))
    return '{"nome":"jose", "idade":37, "carro":"golf" }'

@app.route('/gerarGrafico')
def gerarGrafico():
    tipo_grafico = request.args.get('grafico')
    cargo = request.args.get('cargo')
    agregacao_regional = request.args.get('ar')
    agregacao_politica = request.args.get('ap')
    
    return gerador_de_graficos.get_json_grafico(tipo_grafico, cargo, None, agregacao_politica, agregacao_regional)


