from application import db


class Sessoes(db.Model):
    __tablename__ = 'sessoes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    session_id = db.Column(db.String(100), unique=True, nullable=False)
    dt_inicio = db.Column(db.Date)
    dt_final = db.Column(db.Date)



    def __init__(self, id, user_id, session_id, dt_inicio):
        self.id = id
        self.user_id = user_id
        self.session_id = session_id
        self.dt_inicio = dt_inicio

