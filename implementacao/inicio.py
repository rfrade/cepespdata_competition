from cepesp_python import cepesp
from flask import Flask, render_template, request
import gerador_de_mapas

app = Flask(__name__)

@app.route('/cepesp')
def inicio_aplicacao():
    return render_template('/inicio.html')

@app.route('/gerarMapa')
def gerarMapa():
    print(request.args.get('request_data'))
    return '{"nome":"jose", "idade":37, "carro":"golf" }'

@app.route('/gerarGrafico')
def gerarGrafico():
    return '{"nome":"jose", "idade":37, "carro":"golf" }'