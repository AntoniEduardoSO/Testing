import datetime

from flask import request, flash
from application import db
from application.api.models.usuario import User
from application.backend.services.usuario_services import criar_usuario
from passlib.hash import pbkdf2_sha256

def verificar_cadastro(form):
    if request.method == 'POST':
            email = form.email.data
            cpf = form.cpf.data

            senha = form.password.data
            confirm_senha = form.confirm_password.data

            if verificar_erros(cpf, senha, confirm_senha) == False:
                return False
            

            
            
            

            id_usuario = User.query.count() + 1

            
            nome = request.form.get('credencial-nome') 
            sobrenome = " " + request.form.get('credencial-sobrenome')
            setor_escola = request.form.get('credencial-setor-escola')
            cargo = request.form.get('credencial-cargo')
            telefone = request.form.get('credencial-telefone')
            supervisor = request.form.get('credencial-supervisor')
            status = "Plebe"
            dt_criacao = datetime.datetime.now()

            # print('nome: ' + nome) 
            # print('senha: ' + senha)
            # print('email: ' + email)
            # print('cpf: ' + cpf)
            # print('setor_escola: ' + setor_escola)
            # print('cargo: ' + cargo)
            # print('telefone: ' + telefone)
            # print('supervisor: ' + supervisor)
            # print('status: ' + status)
            # print(dt_criacao)
            
            novo_usuario  = User(
                id_usuario,
                nome + sobrenome,
                senha,
                email,
                cpf,
                setor_escola,
                cargo,
                telefone,
                supervisor,
                status,
                dt_criacao
            )

            
            novo_usuario.set_senha()

            db.session.add(novo_usuario)
            db.session.commit()

            return True


def verificar_erros(cpf, senha, confirm_senha):
    erros = True
    if senha != confirm_senha:
        erros= False
        flash("As senhas não são iguais.", "error")
               

    if verificar_cpf(cpf) == False:
        erros= False
        flash("O CPF fornecido já está cadastrado, por favor, recupere sua senha com a CGTI", "error")


    return erros


def verificar_cpf(cpf):
    user = User.query.filter_by(cpf=cpf).one_or_none()

    if not user:
         return True
    
    return False
