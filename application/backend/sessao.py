from application import db, app
from application.api.models.sessoes import Sessoes
from flask_login import logout_user, current_user
import datetime

def checar_sessao_expirada():
    if current_user.is_authenticated:
        session = Sessoes.query.filter_by(user_id=current_user.id_usuario).first()
        if session:
            session_creation_time = session.dt_inicio
            session_lifetime = app.config['PERMANENT_SESSION_LIFETIME']
            if datetime.now() - session_creation_time > datetime.timedelta(seconds=session_lifetime):
                db.session.delete(session)
                db.session.commit()
                logout_user()