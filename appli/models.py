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
    nomArme = db.Column(db.String(50), nullable=False, unique = True)

    def __init__(self, nom_arme):
        self.nomArme = nom_arme

# Modèle pour représenter la saison
class Saison(db.Model):
    __tablename__ = 'SAISON'
    idSaison = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomSaison = db.Column(db.String(50), nullable=False)
    dateDebutSaison = db.Column(db.Date, nullable=False)
    dateFinSaison = db.Column(db.Date, nullable=False)
    
    def __init__(self, id_saison, nom_saison, date_debut_saison, date_fin_saison):
        self.idSaison = id_saison
        self.nomSaison = nom_saison
        self.dateDebutSaison = date_debut_saison
        self.dateFinSaison = date_fin_saison

# Modèle pour représenter la catégorie
class Categorie(db.Model):
    __tablename__ = 'CATEGORIE'
    idCat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomCategorie = db.Column(db.String(50), nullable=False, unique=True)
    
    def __init__(self, nom_categorie):
        self.nomCategorie = nom_categorie

# Modèle pour représenter le club
class Club(db.Model):
    __tablename__ = 'CLUB'
    idClub = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomClub = db.Column(db.String(50), nullable=False, unique = True)
    regionClub = db.Column(db.String(50), nullable=False)
    
    def __init__(self, nom_club, region_club):
        self.nomClub = nom_club
        self.regionClub = region_club

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
    
    def __init__(self, id_lieu, id_saison, id_categorie, id_arme, nom_comp, desc_comp, date_comp, heure_comp, sexe_comp, est_individuelle):
        self.idLieu = id_lieu
        self.idSaison = id_saison
        self.idCat = id_categorie  # Correction ici
        self.idArme = id_arme
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
        self.idPiste = id_piste
        self.idComp = competition
        self.nomPiste = nom_piste
        self.estDispo = est_dispo

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    __tablename__ = 'TYPE_MATCH'
    idTypeMatch = db.Column(db.Integer, primary_key=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)
    
    def __init__(self, id_type_match, nom_type_match, nb_touches):
        self.idTypeMatch = id_type_match
        self.nomTypeMatch = nom_type_match
        self.nbTouches = nb_touches

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
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'), primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('CLUB.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club', backref='Club.idClub')
    num_licence = db.relationship('Escrimeur', backref='Escrimeur.numeroLicenceE')
    
    def __init__(self, num_licence, club, classement):
        self.numeroLicenceE = num_licence
        self.idClub = club
        self.classement = classement
        
# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    __tablename__ = 'ARBITRE'
    idArbitre = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'))
    
    arbitre = db.relationship('Escrimeur', backref='Arbitre.numeroLicenceE')

    def __init__(self, escrimeur):
        self._escrimeur = escrimeur
        

# Modèle pour représenter les participants aux compétitions
class ParticipantsCompetition(db.Model):
    __tablename__ = 'PARTICIPANTS_COMPETITION'
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), primary_key=True)

    tireur = db.relationship('Tireur', backref='PartTireur', foreign_keys=[numeroLicenceE])
    competition = db.relationship('Competition', backref='PartCompetition.idComp')
    
    def __init__(self, tireur, competition):
        self.numeroLicenceE = tireur
        self.idComp = competition

       
# Modèle pour représenter la relation entre les escrimeurs et les armes qu'ils pratiquent
class PratiquerArme(db.Model):
    __tablename__ = 'PRATIQUER_ARME'
    numero_licence_e_fk = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'), primary_key=True)
    id_arme_fk = db.Column(db.Integer, db.ForeignKey('ARME.idArme'), primary_key=True)

    escrimeur = db.relationship('Escrimeur', backref='armes_pratiquees')
    arme = db.relationship('Arme', backref='pratiquee_par')
    
    def __init__(self, numero_licence_e_fk, id_arme_fk):
        self.numero_licence_e_fk = numero_licence_e_fk
        self.id_arme_fk = id_arme_fk

# Modèle pour représenter le classement final
class ClassementFinal(db.Model):
    __tablename__ = 'CLASSEMENT_FINAL'
    idClassementFinal = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    competition = db.relationship('Competition', backref='competition')
    tireur = db.relationship('Tireur', backref='Tireur.numeroLicenceE')
    
    def __init__(self, id_classement_final, comp, tireur, position):
        self.idClassementFinal = id_classement_final
        self.idComp = comp
        self.numeroLicenceE = tireur
        self.position = position

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
        self.idPoule = id_poule
        self.idComp = competition
        self.idPiste = piste
        self.idArbitre = arbitre
        self.nomPoule = nom_poule

# Modèle pour représenter les participants aux poules
class ParticipantsPoule(db.Model):
    __tablename__ = 'PARTICIPANTS_POULE'
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), primary_key=True)
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), primary_key=True)

    poule = db.relationship('Poule', backref='Poule.idPoule')
    tireur = db.relationship('Tireur', backref='poule_participants')
    
    def __init__(self, poule, tireur):
        self.idPoule = poule
        self.numeroLicenceE = tireur

# Modèle pour représenter les matchs de poule
class MatchPoule(db.Model):
    __tablename__ = 'MATCH_POULE'
    idMatch = db.Column(db.Integer, primary_key=True)
    idTypeMatch = db.Column(db.Integer, db.ForeignKey('TYPE_MATCH.idTypeMatch'), nullable=False)
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('PISTE.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('ARBITRE.idArbitre'), nullable=False)
    numeroLicenceE1 = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=False)
    numeroLicenceE2 = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=False)
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
    tireur1 = db.relationship('Tireur', foreign_keys=[numeroLicenceE1], backref='Tireur.numeroLicenceE1')
    tireur2 = db.relationship('Tireur', foreign_keys=[numeroLicenceE2], backref='Tireur.numeroLicenceE2')
    
    def __init__(self, id_match, type_match, poule, piste, arbitre, tireur1, tireur2, date_match, heure_match, touches_recues_tireur1, touches_donnees_tireur1, touches_recues_tireur2, touches_donnees_tireur2):
        self.idMatch = id_match
        self.idTypeMatch = type_match
        self.idPoule = poule
        self.idPiste = piste
        self.idArbitre = arbitre
        self.numeroLicenceE1 = tireur1
        self.numeroLicenceE2 = tireur2
        self.dateMatch = date_match
        self.heureMatch = heure_match
        self.touchesRecuesTireur1 = touches_recues_tireur1
        self.touchesDonneesTireur1 = touches_donnees_tireur1
        self.touchesRecuesTireur2 = touches_recues_tireur2
        self.touchesDonneesTireur2 = touches_donnees_tireur2

# Modèle pour représenter les feuilles de match
class FeuilleMatch(db.Model):
    __tablename__ = 'FEUILLE_MATCH'
    idFeuille = db.Column(db.Integer, primary_key=True)
    idPoule = db.Column(db.Integer, db.ForeignKey('POULE.idPoule'), nullable=False)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    numeroLicenceE1 = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=False)
    numeroLicenceE2 = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=False)
    scoreTireur1 = db.Column(db.Integer)
    scoreTireur2 = db.Column(db.Integer)
    
    poule = db.relationship('Poule', backref='feuille_matches')
    competition = db.relationship('Competition', backref='feuille_matches')
    tireur1 = db.relationship('Tireur', foreign_keys=[numeroLicenceE1], backref='matches_as_tireur1')
    tireur2 = db.relationship('Tireur', foreign_keys=[numeroLicenceE2], backref='matches_as_tireur2')

    def __init__(self, id_feuille, poule, competition, tireur1, tireur2, score_tireur1, score_tireur2):
        self.idFeuille = id_feuille
        self.idPoule = poule
        self.idComp = competition
        self.numeroLicenceE1 = tireur1
        self.numeroLicenceE2 = tireur2
        self.scoreTireur1 = score_tireur1
        self.scoreTireur2 = score_tireur2
        
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

def get_adherents():
    res =  db.session.query(Tireur, Escrimeur, Categorie, Arbitre).join(Escrimeur, Escrimeur.idEscrimeur == Tireur.numeroLicenceE).join(Club, Club.idClub == Tireur.idClub).join(Categorie, Escrimeur.idCat == Categorie.idCat).outerjoin(Arbitre, Arbitre.idEscrimeur == Escrimeur.idEscrimeur).filter(Club.nomClub == "Club Blois").add_columns(Tireur.numeroLicenceE, Tireur.idClub, Escrimeur.prenomE, Escrimeur.nomE, Escrimeur.dateNaissanceE, Escrimeur.numeroLicenceE, Escrimeur.sexeE, Escrimeur.numTelE, Categorie.nomCategorie).all()
    print(res)
    return res

def get_categories():
    categories = Categorie.query.all()
    return [categorie.nomCategorie for categorie in categories]

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
