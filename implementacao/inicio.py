from cepesp_python import cepesp
from flask import Flask, render_template
import gerador_de_mapas

app = Flask(__name__)

@app.route('/cepesp')
def inicio_aplicacao():
    return render_template('/inicio.html')

@app.route('/gerarMapa')
def gerarMapa():
    return '{"nome":"jose", "idade":37, "carro":"golf" }';

#print(cepesp.votos_x_legendas())