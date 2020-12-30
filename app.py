import data_base
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basic.html')


@app.route('/create_table')
def create_table():
    data_base.create_table_SQL()
    return render_template('basic.html')


@app.route('/actualise_table')
def actualise_table():
    data_base.actualise_table_SQL()
    return render_template('basic.html')


if __name__ == "__main__":
    app.run()