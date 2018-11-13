from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

SECRET_KEY = "stringAleatoria"  #proteção contra ataques
app.secret_key = SECRET_KEY

engine = create_engine("sqlite:///lab05-flask.sqlite")
Session = sessionmaker(bind=engine)
Base = automap_base()
Base.prepare(engine,reflect=True)

Pessoa = Base.classes.Pessoa
Telefones = Base.classes.Telefones

@app.route('/listar')
def listar_pessoas():
    sessionSQL = Session()

    pessoas = sessionSQL.query(Pessoa).all()

    sessionSQL.close()

    return render_template('listar.html',lista_pessoas=pessoas)








@app.route('/index')
@app.route('/')
def hello_world():
    return render_template('index.html',titulo="Título da Página")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)  #apache,nginx, GUnicorn na produção   host= para rodar em todas as interfaces, sem roda somente localhost, debug funciona no terminal


