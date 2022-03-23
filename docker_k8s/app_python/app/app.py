import os
import psycopg
from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def hello_world():
    try:
        conexao = psycopg.connect(host=os.environ['DATABASE_HOST'], 
            dbname=os.environ['DATABASE_NAME'], 
            user=os.environ['DATABASE_USER'],
            port=os.environ['DATABASE_PORT'], 
            password=os.environ['DATABASE_PASS'],)
        test_db="e Banco conectado com sucesso    "
        get_command_linux = os.popen('hostname')
        d_command = get_command_linux.read()
        d_result = d_command + test_db 
        return render_template('index.html', d_output=d_result)
    except Exception:
        err_test_db=" e o BANCO deu RUIM    "
        get_command_linux = os.popen('hostname')
        d_command = get_command_linux.read()
        d_result = d_command + err_test_db
        return render_template('erro.html', d_output=d_result)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)