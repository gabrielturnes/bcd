from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

SECRET_KEY = 'aula de BCD - string aleatória'

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo-02.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True, autoincrement= True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(130))
    email = db.Column(db.String(130))

    def __init__(self,**kwargs):
        super.__init__(kwargs)
        self.username = kwargs.pop('username')
        self.email = kwargs.pop('email')
        self.password = generate_password_hash(kwargs.pop('password'))

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(password)

class LoginForm(FlaskForm):
    username = StringField('Nome do usuário',validators=[DataRequired()])
    password = PasswordField('Senha',validators=[DataRequired()])
    submit = SubmitField('Entrar')



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
