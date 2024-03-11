from application import db, app
from flask_login import UserMixin
from flask_wtf import FlaskForm
from passlib.hash import pbkdf2_sha256
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, Email,  ValidationError, EqualTo, Regexp
import os


class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    senha = db.Column(db.String(length = 255))
    email = db.Column(db.String)
    cpf = db.Column(db.String(length = 50))
    setor_escola = db.Column(db.String)
    cargo = db.Column(db.String)
    numero_telefone = db.Column(db.String)
    supervisor = db.Column(db.String)
    status = db.Column(db.String)
    dt_criacao = db.Column(db.Date)
    foto = db.Column(db.String)

    def __init__(self, id_usuario, nome, senha, email, cpf, setor_escola, cargo, numero_telefone, supervisor, status, dt_criacao):
        self.id_usuario = id_usuario
        self.nome = nome
        self.senha = senha
        self.email = email
        self.cpf = cpf
        self.setor_escola = setor_escola
        self.cargo = cargo
        self.numero_telefone = numero_telefone
        self.supervisor = supervisor
        self.status = status
        self.dt_criacao = dt_criacao
        self.foto = "usuario_vazio.svg"

    
    def foto_path(self):
        return os.path.join(app.config['UPLOAD_FOLDER'], f"{self.id_usuario}_foto.png")


    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)
    

    def set_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)


    def create(db, body):
        user = User.from_json(body)
        db.session.add(user)
        db.session.commit()

        return user
    
    def get_id(self):
        return str(self.id_usuario)



class RegisterForm(FlaskForm):
    cpf = StringField(validators=[InputRequired(), Length(min=11, max=11)])
    email = EmailField(validators=[InputRequired(), Length(min=4, max=30), Email()])
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField(validators=[InputRequired(),
                                                 EqualTo('password', message='As senhas precisam ser iguais.')
                                                 ])
    submit = SubmitField("Cadastre")


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)



class LoginForm(FlaskForm):
    cpf = StringField(validators=[InputRequired(), 
                                  Length(min = 11, max = 11)],
                                  render_kw= {"placeholder": "CPF e E-mail", "class": "credential"})

    password = PasswordField(validators=[InputRequired(), 
                                  Length(min = 8, max = 20)],
                                  render_kw= {"placeholder": "Senha", "class": "credential"})
    
    submit = SubmitField("Entrar")


