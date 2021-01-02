'''
Proyecto Final de Modulo Python Developer
-----------------------------------------------------
Se realiza un website con informacion extraida de un json, pasado a una base de datos
SQL. Donde al mismo a traves de diversas consultas se realizan calculos, que finalizan
en diversos graficos utilizando Matplotlib.
'''

__author__ = "Pablo Martin Ruiz Diaz"
__email__ = "rd.pablo@gmail.com"
__version__ = "1.0"

import data_base
import graphs
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_table')
def create_table():
    data_base.create_table_SQL()
    return render_template('index.html')


@app.route('/actualise_table')
def actualise_table():
    data_base.actualise_table_SQL()
    return render_template('index.html')


@app.route('/bar_graph_continent()')
def bar_graph_continent():
    graphs.bar_graph_continent()
    return render_template('index.html')


@app.route('/bar_graph_continent_death')
def bar_graph_continent_death():
    graphs.bar_graph_continent_death()
    return render_template('index.html')


@app.route('/ranking_table_graph')
def ranking_table_graph():
    graphs.ranking_table_graph()
    return render_template('index.html')


@app.route('/ranking_table_graph_death')
def ranking_table_graph_death():
    graphs.ranking_table_graph_death()
    return render_template('index.html')


@app.route('/line_graph')
def line_graph():
    graphs.line_graph()
    return render_template('index.html')


@app.route('/line_graph_death')
def line_graph_death():
    graphs.line_graph_death()
    return render_template('index.html')


@app.route('/line_graph_per_country')
def line_graph_per_country(country):
    graphs.line_graph_per_country(country)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)