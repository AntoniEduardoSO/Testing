import datetime
from flask import flash, request
from flask_login import login_user
from application.api.models.usuario import User
from flask import session
from application import db
import uuid

from application.api.models.sessoes import Sessoes

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
        


def verificar_sessao(user_id):
    sessao =  Sessoes.query.filter_by(user_id=user_id).one_or_none()


    if(sessao):
        return False
    
    
    proximo_id_disponivel = db.session.query(db.func.max(Sessoes.id)).scalar() or 0
    novo_id = proximo_id_disponivel + 1
    
    nova_sessao = Sessoes(id=novo_id, user_id=user_id, session_id= str(uuid.uuid4()), dt_inicio = datetime.datetime.now() )
    db.session.add(nova_sessao)
    db.session.commit()

    return True