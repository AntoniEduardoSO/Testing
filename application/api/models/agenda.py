from application import db


class Agenda(db.Model):
    __tablename__ = 'agenda'
    id = db.Column(db.String, primary_key=True)
    autor = db.Column(db.String,  nullable=False)
    responsavel = db.Column(db.String, nullable=False)
    horario = db.Column(db.String, nullable=False)
    data = db.Column(db.String)



    def __init__(self, id, autor, responsavel, horario, data):
        self.id = id
        self.autor = autor
        self.responsavel = responsavel
        self.horario = horario
        self.data = data