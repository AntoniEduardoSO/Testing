from flask import flash, request
from flask_login import login_user
from application.api.models.usuario import User, RegisterForm, LoginForm

def verificar_login(form):
    user = User.query.filter_by(cpf = form.cpf.data).one_or_none()


    try:
        if user:
            if user.ver_senha(senha = form.password.data):
                login_user(user)
                return True
        
            else:
                flash("Usuário ou senha errados.", "error")
                return False
        else:
            flash("Usuário não existe, Cadastre-se.", "error")
            return False
        
    except Exception as e:
        flash(f'Ocorreu um erro:{e}', "error")
        
