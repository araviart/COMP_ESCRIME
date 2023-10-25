from .app import db

class Lieu(db.Model):
    idLieu = db.Column(db.Integer, primary_key =True)
