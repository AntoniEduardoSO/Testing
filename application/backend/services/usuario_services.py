from application import db
from application.api.models.usuario import User
from datetime import timedelta
from passlib.hash import pbkdf2_sha256

from flask_jwt_extended import create_access_token


def ver_senha(senha_hash, senha):
    return pbkdf2_sha256.verify(senha, senha_hash)


def criar_usuario(usuario):

    print(usuario.senha)

    


    usuario_db = User(
        id_usuario= usuario.id_usuario,
        nome= usuario.nome,
        senha = pbkdf2_sha256.hash(usuario.senha),
        email = usuario.email,
        cpf = usuario.cpf,
        setor_escola = usuario.setor_escola,
        cargo = usuario.cargo,
        numero_telefone = usuario.numero_telefone,
        supervisor = usuario.supervisor,
        status = "ativo",
        dt_criacao = usuario.dt_criacao,  
        )
    
    db.session.add(usuario_db)
    db.session.commit()

    return usuario_db


    


    
    
