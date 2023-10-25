from .app import db

# Modèle pour représenter le lieu
class Lieu(db.Model):
    idLieu = db.Column(db.Integer, primary_key=True)
    nomLieu = db.Column(db.String(50), nullable=False)
    villeLieu = db.Column(db.String(50), nullable=False)
    codePostalLieu = db.Column(db.Integer, nullable=False)
    adresseLieu = db.Column(db.String(50), nullable=False)

# Modèle pour représenter l'arme
class Arme(db.Model):
    idArme = db.Column(db.Integer, primary_key=True)
    nomArme = db.Column(db.String(50), nullable=False)

# Modèle pour représenter la saison
class Saison(db.Model):
    idSaison = db.Column(db.Integer, primary_key=True)
    nomSaison = db.Column(db.String(50), nullable=False)
    dateDebutSaison = db.Column(db.Date, nullable=False)
    dateFinSaison = db.Column(db.Date, nullable=False)

# Modèle pour représenter la catégorie
class Categorie(db.Model):
    idCat = db.Column(db.Integer, primary_key=True)
    nomCategorie = db.Column(db.String(50), nullable=False)

# Modèle pour représenter le club
class Club(db.Model):
    idClub = db.Column(db.Integer, primary_key=True)
    nomClub = db.Column(db.String(50), nullable=False)
    villeClub = db.Column(db.String(50), nullable=False)

# Modèle pour représenter la compétition
class Competition(db.Model):
    idComp = db.Column(db.Integer, primary_key=True)
    idLieu = db.Column(db.Integer, db.ForeignKey('lieu.idLieu'), nullable=False)
    idSaison = db.Column(db.Integer, db.ForeignKey('saison.idSaison'), nullable=False)
    idCat = db.Column(db.Integer, db.ForeignKey('categorie.idCat'), nullable=False)
    idArme = db.Column(db.Integer, db.ForeignKey('arme.idArme'), nullable=False)
    nomComp = db.Column(db.String(50), nullable=False)
    descComp = db.Column(db.String(50), nullable=False)
    dateComp = db.Column(db.Date, nullable=False)
    heureComp = db.Column(db.Time, nullable=False)
    sexeComp = db.Column(db.String(1), nullable=False)
    estIndividuelle = db.Column(db.Boolean, nullable=False)

    lieu = db.relationship('Lieu')
    saison = db.relationship('Saison')
    categorie = db.relationship('Categorie')
    arme = db.relationship('Arme')

# Modèle pour représenter la piste
class Piste(db.Model):
    idPiste = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('competition.idComp'), nullable=False)
    nomPiste = db.Column(db.String(50), nullable=False)
    estDispo = db.Column(db.Boolean, nullable=False)

    competition = db.relationship('Competition')

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    idTypeMatch = db.Column(db.Integer, primary_key=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)

# Modèle pour représenter l'escrimeur
class Escrimeur(db.Model):
    idEscrimeur = db.Column(db.Integer, primary_key=True)
    idCat = db.Column(db.Integer, db.ForeignKey('categorie.idCat'), nullable=False)
    prenomE = db.Column(db.String(50), nullable=False)
    nomE = db.Column(db.String(50), nullable=False)
    dateNaissanceE = db.Column(db.Date, nullable=False)
    numeroLicenceE = db.Column(db.Integer, nullable=False)
    sexeE = db.Column(db.String(50), nullable=False)
    numTelE = db.Column(db.Integer)

    categorie = db.relationship('Categorie')

# Modèle pour représenter les tireurs
class Tireur(db.Model):
    idTireur = db.Column(db.Integer, primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('club.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club')

# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    idArbitre = db.Column(db.Integer, primary_key=True)

# Modèle pour représenter la relation entre les escrimeurs et les armes qu'ils pratiquent
class PratiquerArme(db.Model):
    idEscrimeur = db.Column(db.Integer, db.ForeignKey('escrimeur.idEscrimeur'), primary_key=True)
    idArme = db.Column(db.Integer, db.ForeignKey('arme.idArme'), primary_key=True)

    escrimeur = db.relationship('Escrimeur')
    arme = db.relationship('Arme')

# Modèle pour représenter le classement final
class ClassementFinal(db.Model):
    idClassementFinal = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('competition.idComp'), nullable=False)
    idTireur = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    competition = db.relationship('Competition')
    tireur = db.relationship('Tireur')

# Modèle pour représenter les poules
class Poule(db.Model):
    idPoule = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('competition.idComp'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('piste.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('arbitre.idArbitre'), nullable=False)
    nomPoule = db.Column(db.String(50), nullable=False)

    competition = db.relationship('Competition')
    piste = db.relationship('Piste')
    arbitre = db.relationship('Arbitre')

# Modèle pour représenter les participants aux poules
class ParticipantsPoule(db.Model):
    idPoule = db.Column(db.Integer, db.ForeignKey('poule.idPoule'), primary_key=True)
    idTireur = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), primary_key=True)

    poule = db.relationship('Poule')
    tireur = db.relationship('Tireur')

# Modèle pour représenter les matchs de poule
class MatchPoule(db.Model):
    idMatch = db.Column(db.Integer, primary_key=True)
    idTypeMatch = db.Column(db.Integer, db.ForeignKey('type_match.idTypeMatch'), nullable=False)
    idPoule = db.Column(db.Integer, db.ForeignKey('poule.idPoule'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('piste.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('arbitre.idArbitre'), nullable=False)
    idTireur1 = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    idTireur2 = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    dateMatch = db.Column(db.Date, nullable=False)
    heureMatch = db.Column(db.Time, nullable=False)
    touchesRecuesTireur1 = db.Column(db.Integer)
    touchesDonneesTireur1 = db.Column(db.Integer)
    touchesRecuesTireur2 = db.Column(db.Integer)
    touchesDonneesTireur2 = db.Column(db.Integer)

    type_match = db.relationship('TypeMatch')
    poule = db.relationship('Poule')
    piste = db.relationship('Piste')
    arbitre = db.relationship('Arbitre')
    tireur1 = db.relationship('Tireur', foreign_keys=[idTireur1])
    tireur2 = db.relationship('Tireur', foreign_keys=[idTireur2])

# Modèle pour représenter les feuilles de match
class FeuilleMatch(db.Model):
    idFeuille = db.Column(db.Integer, primary_key=True)
    idPoule = db.Column(db.Integer, db.ForeignKey('poule.idPoule'), nullable=False)
    idComp = db.Column(db.Integer, db.ForeignKey('competition.idComp'), nullable=False)
    idTireur1 = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    idTireur2 = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    scoreTireur1 = db.Column(db.Integer)
    scoreTireur2 = db.Column(db.Integer)

    poule = db.relationship('Poule')
    competition = db.relationship('Competition')
    tireur1 = db.relationship('Tireur', foreign_keys=[idTireur1])
    tireur2 = db.relationship('Tireur', foreign_keys=[idTireur2])
