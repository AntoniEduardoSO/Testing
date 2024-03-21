from application import db

class Escola(db.Model):
    __tablename__ = 'escolas'
    codigo_escola = db.Column(db.Integer, primary_key=True)
    nome_escola = db.Column(db.String)
    