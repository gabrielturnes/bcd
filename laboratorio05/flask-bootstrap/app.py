from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

SECRET_KEY = 'aula de BCD - string aleatória'

app = Flask(__name__)
app.secret_key = SECRET_KEY

bootstrap = Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo-02.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


nav = Nav()
nav.init_app(app) # menu no topo da página

@nav.navigation()
def menunav():
    menu = Navbar('Minha aplicação')
    menu.items = [View('Home', 'hello_world')]
    menu.items.append(Subgroup('Pessoas', View('Aluno', 'hello_world')))
    menu.items.append(Link('Ajuda', 'https://www.google.com.br'))

    if session.get('logged_in') is True:
        menu.items.append(View('Painel', 'painel'))
        menu.items.append(View('Sair', 'sair'))
    else:
        menu.items.append(View('Login', 'autenticar'))


    return menu

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement= True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(130))
    email = db.Column(db.String(130))

    # def __init__(self,**kwargs):
    #     super.__init__(kwargs)
    #     self.username = kwargs.pop('username')
    #     self.email = kwargs.pop('email')
    #     self.password = generate_password_hash(kwargs.pop('password'))

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

class LoginForm(FlaskForm):
    username = StringField('Nome do usuário',validators=[DataRequired()])
    password = PasswordField('Senha',validators=[DataRequired()])
    submit = SubmitField('Entrar')



@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def autenticar():
    formulario = LoginForm()
    if session.get('logged_in') is False:
        if formulario.validate_on_submit():
            #fazer autenticação do usuário
            usuario = Usuario.query.filter_by(username=formulario.username.data).first_or_404()

            if(usuario.check_password(formulario.password.data)):
                session['logged_in'] = True
                session['usuario'] = usuario.username
                return render_template('autenticado.html', usuario=usuario.get_username())
        return render_template('login.html', form=formulario)

    return redirect(url_for('painel'))

@app.route('/painel')
def painel():
    if session.get('logged_in') is True:
        usuario = Usuario.query.filter_by(username=session.get('usuario')).first_or_404()

        return render_template('painel.html', title="Usuário autenticado", user=usuario)

    return redirect(url_for('hello_world'))

@app.route('/logout')
def sair():
    session['logged_in'] = False
    return redirect(url_for('autenticar'))

if __name__ == '__main__':
    app.run()
