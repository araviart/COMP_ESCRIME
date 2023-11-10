from .app import db, login_manager
from flask_login import UserMixin

# Modèle pour représenter le lieu
class Lieu(db.Model):
    __tablename__ = 'LIEU'
    idLieu = db.Column(db.Integer, primary_key=True)
    nomLieu = db.Column(db.String(50), nullable=False)
    villeLieu = db.Column(db.String(50), nullable=False)
    codePostalLieu = db.Column(db.Integer, nullable=False)
    adresseLieu = db.Column(db.String(50), nullable=False)

# Modèle pour représenter l'arme
class Arme(db.Model):
    __tablename__ = 'ARME'
    idArme = db.Column(db.Integer, primary_key=True)
    nomArme = db.Column(db.String(50), nullable=False)

# Modèle pour représenter la saison
class Saison(db.Model):
    __tablename__ = 'SAISON'
    idSaison = db.Column(db.Integer, primary_key=True)
    nomSaison = db.Column(db.String(50), nullable=False)
    dateDebutSaison = db.Column(db.Date, nullable=False)
    dateFinSaison = db.Column(db.Date, nullable=False)

# Modèle pour représenter la catégorie
class Categorie(db.Model):
    __tablename__ = 'CATEGORIE'
    idCat = db.Column(db.Integer, primary_key=True)
    nomCategorie = db.Column(db.String(50), nullable=False)

# Modèle pour représenter le club
class Club(db.Model):
    __tablename__ = 'CLUB'
    idClub = db.Column(db.Integer, primary_key=True)
    nomClub = db.Column(db.String(50), nullable=False)
    villeClub = db.Column(db.String(50), nullable=False)

# Modèle pour représenter la compétition
class Competition(db.Model):
    __tablename__ = 'COMPETITION'
    idComp = db.Column(db.Integer, primary_key=True)
    idLieu = db.Column(db.Integer, db.ForeignKey('LIEU.idLieu'), nullable=False)
    lieu = db.relationship('Lieu', backref='Lieu.idLieu')
    idSaison = db.Column(db.Integer, db.ForeignKey('SAISON.idSaison'), nullable=False)
    saison = db.relationship('Saison', backref='Saison.idSaison')
    idCat = db.Column(db.Integer, db.ForeignKey('CATEGORIE.idCat'), nullable=False)
    categorie = db.relationship('Categorie', backref='Categorie.idCat')
    idArme = db.Column(db.Integer, db.ForeignKey('ARME.idArme'), nullable=False)
    arme = db.relationship('Arme', backref='Arme.idArme')
    nomComp = db.Column(db.String(50), nullable=False)
    descComp = db.Column(db.String(50), nullable=False)
    dateComp = db.Column(db.Date, nullable=False)
    heureComp = db.Column(db.Time, nullable=False)
    sexeComp = db.Column(db.String(1), nullable=False)
    estIndividuelle = db.Column(db.Boolean, nullable=False)

# Modèle pour représenter la piste
class Piste(db.Model):
    __tablename__ = 'PISTE'
    idPiste = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    nomPiste = db.Column(db.String(50), nullable=False)
    estDispo = db.Column(db.Boolean, nullable=False)

    competition = db.relationship('Competition', backref='Competition.idComp')

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    __tablename__ = 'TYPE_MATCH'
    idTypeMatch = db.Column(db.Integer, primary_key=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)

# Modèle pour représenter l'escrimeur
class Escrimeur(db.Model):
    __tablename__ = 'ESCRIMEUR'
    idEscrimeur = db.Column(db.Integer, primary_key=True)
    idCat = db.Column(db.Integer, db.ForeignKey('CATEGORIE.idCat'), nullable=False)
    prenomE = db.Column(db.String(50), nullable=False)
    nomE = db.Column(db.String(50), nullable=False)
    dateNaissanceE = db.Column(db.Date, nullable=False)
    numeroLicenceE = db.Column(db.Integer, nullable=False)
    sexeE = db.Column(db.String(50), nullable=False)
    numTelE = db.Column(db.Integer)

    categorie = db.relationship('Categorie', backref='categorie')

# Modèle pour représenter les tireurs
class Tireur(db.Model):
    __tablename__ = 'TIREUR'
    idTireur = db.Column(db.Integer, primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('CLUB.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club', backref='Club.idClub')

# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    __tablename__ = 'ARBITRE'
    idArbitre = db.Column(db.Integer, primary_key=True)

# Modèle pour représenter la relation entre les escrimeurs et les armes qu'ils pratiquent
class PratiquerArme(db.Model):
    __tablename__ = 'PRATIQUER_ARME'
    idEscrimeur = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.idEscrimeur'), primary_key=True)
    idArme = db.Column(db.Integer, db.ForeignKey('ARME.idArme'), primary_key=True)

    escrimeur = db.relationship('Escrimeur', backref='Escrimeur.idEscrimeur')
    arme = db.relationship('Arme', backref='arme')

# Modèle pour représenter le classement final
class ClassementFinal(db.Model):
    __tablename__ = 'CLASSEMENT_FINAL'
    idClassementFinal = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    idTireur = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    competition = db.relationship('Competition', backref='competition')
    tireur = db.relationship('Tireur', backref='Tireur.idTireur')

# Modèle pour représenter les poules
class Poule(db.Model):
    __tablename__ = 'POULE'
    idPoule = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('PISTE.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('ARBITRE.idArbitre'), nullable=False)
    nomPoule = db.Column(db.String(50), nullable=False)

    competition = db.relationship('Competition', backref='poules')
    piste = db.relationship('Piste', backref='Piste.idPiste')
    arbitre = db.relationship('Arbitre', backref='Arbitre.idArbitre')

# Modèle pour représenter les participants aux poules
class ParticipantsPoule(db.Model):
    __tablename__ = 'PARTICIPANTS_POULE'
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), primary_key=True)
    idTireur = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), primary_key=True)

    poule = db.relationship('Poule', backref='Poule.idPoule')
    tireur = db.relationship('Tireur', backref='poule_participants')

# Modèle pour représenter les matchs de poule
class MatchPoule(db.Model):
    __tablename__ = 'MATCH_POULE'
    idMatch = db.Column(db.Integer, primary_key=True)
    idTypeMatch = db.Column(db.Integer, db.ForeignKey('TYPE_MATCH.idTypeMatch'), nullable=False)
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('PISTE.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('ARBITRE.idArbitre'), nullable=False)
    idTireur1 = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    idTireur2 = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    dateMatch = db.Column(db.Date, nullable=False)
    heureMatch = db.Column(db.Time, nullable=False)
    touchesRecuesTireur1 = db.Column(db.Integer)
    touchesDonneesTireur1 = db.Column(db.Integer)
    touchesRecuesTireur2 = db.Column(db.Integer)
    touchesDonneesTireur2 = db.Column(db.Integer)

    type_match = db.relationship('TypeMatch', backref='TypeMatch.idTypeMatch')
    poule = db.relationship('Poule', backref='matches')
    piste = db.relationship('Piste', backref='matches')
    arbitre = db.relationship('Arbitre', backref='matches')
    tireur1 = db.relationship('Tireur', foreign_keys=[idTireur1], backref='Tireur.idTireur1')
    tireur2 = db.relationship('Tireur', foreign_keys=[idTireur2], backref='Tireur.idTireur2')

# Modèle pour représenter les feuilles de match
class FeuilleMatch(db.Model):
    __tablename__ = 'FEUILLE_MATCH'
    idFeuille = db.Column(db.Integer, primary_key=True)
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), nullable=False)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    idTireur1 = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    idTireur2 = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    scoreTireur1 = db.Column(db.Integer)
    scoreTireur2 = db.Column(db.Integer)

    poule = db.relationship('Poule', backref='feuille_matches')
    competition = db.relationship('Competition', backref='feuille_matches')
    tireur1 = db.relationship('Tireur', foreign_keys=[idTireur1], backref='matches_as_tireur1')
    tireur2 = db.relationship('Tireur', foreign_keys=[idTireur2], backref='matches_as_tireur2')

class User(db.Model, UserMixin):
    __tablename__ = 'USER'
    idUser = db.Column(db.Integer, primary_key=True)
    pseudoUser = db.Column(db.String (50), unique=True, nullable=False)
    mdpUser = db.Column(db.String (64), nullable=False)
    emailUser = db.Column(db.String (50), unique=True)

    def get_id(self):
        return self.idUser

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

def get_sample():
    return Competition.query.all()

def get_armes():
    armes = Arme.query.all()
    return [arme.nomArme for arme in armes]

def get_type_match():
    type_match = TypeMatch.query.all()
    return [type_match.nomTypeMatch for type_match in type_match]

def get_categories():
    categories = Categorie.query.all()
    return [categorie.nomCategorie for categorie in categories]