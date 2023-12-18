import datetime
from .app import db, login_manager
from flask_login import UserMixin

# Modèle pour représenter le lieu
class Lieu(db.Model):
    __tablename__ = 'LIEU'
    idLieu = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomLieu = db.Column(db.String(50), nullable=False)
    villeLieu = db.Column(db.String(50), nullable=False)
    codePostalLieu = db.Column(db.Integer, nullable=False)
    adresseLieu = db.Column(db.String(50), nullable=False)
    
    def __init__(self, nom_lieu, ville_lieu, code_postal_lieu, adresse_lieu):
        self.nomLieu = nom_lieu
        self.villeLieu = ville_lieu
        self.codePostalLieu = code_postal_lieu
        self.adresseLieu = adresse_lieu

# Modèle pour représenter l'arme
class Arme(db.Model):
    __tablename__ = 'ARME'
    idArme = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomArme = db.Column(db.String(50), nullable=False)

    def __init__(self, id_arme, nom_arme):
        self._id_arme = id_arme
        self._nom_arme = nom_arme

# Modèle pour représenter la saison
class Saison(db.Model):
    __tablename__ = 'SAISON'
    idSaison = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomSaison = db.Column(db.String(50), nullable=False)
    dateDebutSaison = db.Column(db.Date, nullable=False)
    dateFinSaison = db.Column(db.Date, nullable=False)
    
    def __init__(self, id_saison, nom_saison, date_debut_saison, date_fin_saison):
        self._id_saison = id_saison
        self._nom_saison = nom_saison
        self._date_debut_saison = date_debut_saison
        self._date_fin_saison = date_fin_saison

# Modèle pour représenter la catégorie
class Categorie(db.Model):
    __tablename__ = 'CATEGORIE'
    idCat = db.Column(db.Integer, primary_key=True)
    nomCategorie = db.Column(db.String(50), nullable=False)
    
    def __init__(self, id_cat, nom_categorie):
        self._id_cat = id_cat
        self._nom_categorie = nom_categorie

# Modèle pour représenter le club
class Club(db.Model):
    __tablename__ = 'CLUB'
    idClub = db.Column(db.Integer, primary_key=True)
    nomClub = db.Column(db.String(50), nullable=False)
    villeClub = db.Column(db.String(50), nullable=False)
    
    def __init__(self, id_club, nom_club, ville_club):
        self._id_club = id_club
        self._nom_club = nom_club
        self._ville_club = ville_club

# Modèle pour représenter la compétition
class Competition(db.Model):
    __tablename__ = 'COMPETITION'
    idComp = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    
    def __init__(self, lieu, saison, categorie, arme, nom_comp, desc_comp, date_comp, heure_comp, sexe_comp, est_individuelle):
        self.idLieu = lieu.idLieu
        self.idSaison = saison.idSaison
        self.idCat = categorie.idCat
        self.idArme = arme.idArme
        self.nomComp = nom_comp
        self.descComp = desc_comp
        self.dateComp = date_comp
        self.heureComp = heure_comp
        self.sexeComp = sexe_comp
        self.estIndividuelle = est_individuelle

# Modèle pour représenter la piste
class Piste(db.Model):
    __tablename__ = 'PISTE'
    idPiste = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    nomPiste = db.Column(db.String(50), nullable=False)
    estDispo = db.Column(db.Boolean, nullable=False)

    competition = db.relationship('Competition', backref='Competition.idComp')
    
    def __init__(self, id_piste, competition, nom_piste, est_dispo):
        self._id_piste = id_piste
        self._competition = competition
        self._nom_piste = nom_piste
        self._est_dispo = est_dispo

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    __tablename__ = 'TYPE_MATCH'
    idTypeMatch = db.Column(db.Integer, primary_key=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)
    
    def __init__(self, id_type_match, nom_type_match, nb_touches):
        self._id_type_match = id_type_match
        self._nom_type_match = nom_type_match
        self._nb_touches = nb_touches

# Modèle pour représenter l'escrimeur
class Escrimeur(db.Model):
    __tablename__ = 'ESCRIMEUR'
    idEscrimeur = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idCat = db.Column(db.Integer, db.ForeignKey('CATEGORIE.idCat'), nullable=False)
    prenomE = db.Column(db.String(50), nullable=False)
    nomE = db.Column(db.String(50), nullable=False)
    dateNaissanceE = db.Column(db.Date, nullable=False)
    numeroLicenceE = db.Column(db.Integer, nullable=False)
    sexeE = db.Column(db.String(1), nullable=False)
    numTelE = db.Column(db.String(10), nullable=False)

    def __init__(self, idEscrimeur, idCat, prenomE, nomE, dateNaissanceE, numeroLicenceE, sexeE, numTelE):
        self.idEscrimeur = idEscrimeur
        self.idCat = idCat
        self.prenomE = prenomE
        self.nomE = nomE
        self.dateNaissanceE = dateNaissanceE
        self.numeroLicenceE = numeroLicenceE
        self.sexeE = sexeE
        self.numTelE = numTelE

        
# Modèle pour représenter les tireurs
class Tireur(db.Model):
    __tablename__ = 'TIREUR'
    idTireur = db.Column(db.Integer, primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('CLUB.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club', backref='Club.idClub')

    def __init__(self, escrimeur, club, classement):
        self._escrimeur = escrimeur
        self._club = club
        self._classement = classement
        
# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    __tablename__ = 'ARBITRE'
    idArbitre = db.Column(db.Integer, primary_key=True)
    idEscrimeur = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.idEscrimeur'))

    def __init__(self, escrimeur):
        self._escrimeur = escrimeur
        

# Modèle pour représenter les participants aux compétitions
class ParticipantsCompetition(db.Model):
    __tablename__ = 'PARTICIPANTS_COMPETITION'
    idTireur = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), primary_key=True)

    tireur = db.relationship('Tireur', backref='PartTireur.idTireur')
    competition = db.relationship('Competition', backref='PartCompetition.idComp')
    
    def __init__(self, tireur, competition):
        self._tireur = tireur
        self._competition = competition

# Modèle pour représenter la relation entre les escrimeurs et les armes qu'ils pratiquent
class PratiquerArme(db.Model):
    __tablename__ = 'PRATIQUER_ARME'
    idEscrimeur = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.idEscrimeur'), primary_key=True)
    idArme = db.Column(db.Integer, db.ForeignKey('ARME.idArme'), primary_key=True)

    escrimeur = db.relationship('Escrimeur', backref='Escrimeur.idEscrimeur')
    arme = db.relationship('Arme', backref='arme')
    
    def __init__(self, escrimeur, arme):
        self._escrimeur = escrimeur
        self._arme = arme

# Modèle pour représenter le classement final
class ClassementFinal(db.Model):
    __tablename__ = 'CLASSEMENT_FINAL'
    idClassementFinal = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    idTireur = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    competition = db.relationship('Competition', backref='competition')
    tireur = db.relationship('Tireur', backref='Tireur.idTireur')
    
    def __init__(self, id_classement_final, comp, tireur, position):
        self._id_classement_final = id_classement_final
        self._comp = comp
        self._tireur = tireur
        self._position = position

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
    
    def __init__(self, id_poule, competition, piste, arbitre, nom_poule):
        self._id_poule = id_poule
        self._competition = competition
        self._piste = piste
        self._arbitre = arbitre
        self._nom_poule = nom_poule

# Modèle pour représenter les participants aux poules
class ParticipantsPoule(db.Model):
    __tablename__ = 'PARTICIPANTS_POULE'
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), primary_key=True)
    idTireur = db.Column(db.Integer, db.ForeignKey('TIREUR.idTireur'), primary_key=True)

    poule = db.relationship('Poule', backref='Poule.idPoule')
    tireur = db.relationship('Tireur', backref='poule_participants')
    
    def __init__(self, poule, tireur):
        self._poule = poule
        self._tireur = tireur

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
    
    def __init__(self, id_match, type_match, poule, piste, arbitre, tireur1, tireur2, date_match, heure_match, touches_recues_tireur1, touches_donnees_tireur1, touches_recues_tireur2, touches_donnees_tireur2):
        self._id_match = id_match
        self._type_match = type_match
        self._poule = poule
        self._piste = piste
        self._arbitre = arbitre
        self._tireur1 = tireur1
        self._tireur2 = tireur2
        self._date_match = date_match
        self._heure_match = heure_match
        self._touches_recues_tireur1 = touches_recues_tireur1
        self._touches_donnees_tireur1 = touches_donnees_tireur1
        self._touches_recues_tireur2 = touches_recues_tireur2
        self._touches_donnees_tireur2 = touches_donnees_tireur2

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

    def __init__(self, id_feuille, poule, competition, tireur1, tireur2, score_tireur1, score_tireur2):
        self._id_feuille = id_feuille
        self._poule = poule
        self._competition = competition
        self._tireur1 = tireur1
        self._tireur2 = tireur2
        self._score_tireur1 = score_tireur1
        self._score_tireur2 = score_tireur2
        
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
    return Competition.query.order_by(Competition.dateComp.desc()).all()

def get_categories():
    categories = Categorie.query.all()
    return [categorie.nomCategorie for categorie in categories]

def get_lieux():
    lieux = Lieu.query.all()
    return [lieu.nomLieu for lieu in lieux]

def get_armes():
    armes = Arme.query.all()
    return [arme.nomArme for arme in armes]

def get_type_match():
    type_match = TypeMatch.query.all()
    return [type_match.nomTypeMatch for type_match in type_match]

def get_nb_participants(id_tournoi):
    participants_count = ParticipantsCompetition.query.join(Competition).filter(Competition.idComp == id_tournoi).count()
    return participants_count

def filtrer_competitions(competitions, categorie, arme, sexe, statut):
    comp_filtrer = competitions
    if categorie:
        comp_filtrer = [comp for comp in comp_filtrer if comp.categorie.nomCategorie == categorie]
    if arme:
        comp_filtrer = [comp for comp in comp_filtrer if comp.arme.nomArme == arme]
    if sexe:
        comp_filtrer = [comp for comp in comp_filtrer if comp.sexeComp == sexe]
    if statut:
        if statut == "A venir":
            comp_filtrer = [comp for comp in comp_filtrer if comp.dateComp > datetime.date.today()]
        elif statut == "Terminé":
            comp_filtrer = [comp for comp in comp_filtrer if comp.dateComp <= datetime.date.today()]
    return comp_filtrer

def filtrer_adherent(adherents, categorie, sexeE):
    adherents_filtrer = adherents 
    if categorie:
        adherents_filtrer = [adherent for adherent in adherents_filtrer if adherent.Categorie.nomCategorie == categorie]
    if sexeE:
        adherents_filtrer = [adherent for adherent in adherents_filtrer if adherent.Escrimeur.sexeE == sexeE]
    # if role == 'tireur':
    #     adherents_filtrer = [adherent for adherent in adherents_filtrer if adherent.Arbitre is None]
    # elif role == 'arbitre':
    #     adherents_filtrer = [adherent for adherent in adherents_filtrer if adherent.Arbitre is not None]
    return adherents_filtrer

def get_id_lieu(nom_lieu):
    lieu = Lieu.query.filter_by(nomLieu=nom_lieu).first()
    return lieu.idLieu if lieu else None

def get_id_saison(nom_saison):
    saison = Saison.query.filter_by(nomSaison=nom_saison).first()
    return saison.idSaison if saison else None

def get_adherents():
    res =  db.session.query(Tireur, Escrimeur, Categorie).join(Escrimeur, Escrimeur.idEscrimeur == Tireur.idTireur).join(Club, Club.idClub == Tireur.idClub).join(Categorie, Escrimeur.idCat == Categorie.idCat).filter(Club.nomClub == "Club Blois").add_columns(Tireur.idTireur, Tireur.idClub, Escrimeur.prenomE, Escrimeur.nomE, Escrimeur.dateNaissanceE, Escrimeur.numeroLicenceE, Escrimeur.sexeE, Escrimeur.numTelE, Categorie.nomCategorie).all()
    return res

def dernier_escrimeur_id():
    last_escrimeur = db.session.query(Escrimeur).order_by(Escrimeur.idEscrimeur.desc()).first()
    if last_escrimeur:
        return last_escrimeur.idEscrimeur
    else:
        return 0
