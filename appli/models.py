import datetime

from sqlalchemy import func
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
    
    def __init__(self, nom_saison, date_debut_saison, date_fin_saison):
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
    
    def __init__(self, idLieu, idSaison, idCat, idArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle):
        self.idLieu = idLieu
        self.idSaison = idSaison
        self.idCat = idCat
        self.idArme = idArme
        self.nomComp = nomComp
        self.descComp = descComp
        self.dateComp = dateComp
        self.heureComp = heureComp
        self.sexeComp = sexeComp
        self.estIndividuelle = estIndividuelle

# Modèle pour représenter la piste
class Piste(db.Model):
    __tablename__ = 'PISTE'
    idPiste = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    nomPiste = db.Column(db.String(50), nullable=False)
    estDispo = db.Column(db.Boolean, nullable=False)

    competition = db.relationship('Competition', backref='Competition.idComp')
    
    def __init__(self, competition, nom_piste, est_dispo):
        self.idComp = competition
        self.nomPiste = nom_piste
        self.estDispo = est_dispo

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    __tablename__ = 'TYPE_MATCH'
    idTypeMatch = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)
    
    def __init__(self, nom_type_match, nb_touches):
        self.nomTypeMatch = nom_type_match
        self.nbTouches = nb_touches

# Modèle pour représenter l'escrimeur
class Escrimeur(db.Model):
    __tablename__ = 'ESCRIMEUR'
    numeroLicenceE = db.Column(db.Integer, nullable=False, primary_key=True)
    idCat = db.Column(db.Integer, db.ForeignKey('CATEGORIE.idCat'), nullable=False)
    prenomE = db.Column(db.String(50), nullable=False)
    nomE = db.Column(db.String(50), nullable=False)
    dateNaissanceE = db.Column(db.Date, nullable=False)
    sexeE = db.Column(db.String(50), nullable=False)
    numTelE = db.Column(db.Integer, nullable=True)

    categorie = db.relationship('Categorie', backref='categorie')

    def __init__(self, categorie, prenom_e, nom_e, date_naissance_e, numero_licence_e, sexe_e, num_tel_e):
        self.idCat = categorie
        self.numeroLicenceE = numero_licence_e
        self.idCat = categorie
        self.prenomE = prenom_e
        self.nomE = nom_e
        self.dateNaissanceE = date_naissance_e
        self.sexeE = sexe_e
        self.numTelE = num_tel_e
        
    def to_dict(self):
        return {
            'idCat': self.idCat,
            'prenomE': self.prenomE,
            'nomE': self.nomE,
            'dateNaissanceE': self.dateNaissanceE.isoformat() if self.dateNaissanceE else None,
            'numeroLicenceE': self.numeroLicenceE,
            'sexeE': self.sexeE,
            'numTelE': self.numTelE,
            'categorie': self.categorie.nomCategorie
        }

    
# Modèle pour représenter les tireurs
class Tireur(db.Model):
    __tablename__ = 'TIREUR'
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'), primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('CLUB.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club', backref='Club.idClub')
    escrimeur = db.relationship('Escrimeur', backref='Escrimeur.tireur')

    def __init__(self, num_licence, club, classement):
        self.numeroLicenceE = num_licence
        self.idClub = club
        self.classement = classement
    
    def to_dict(self):
        dic_tireur = self.escrimeur.to_dict()
        dic_tireur['idClub'] = self.idClub
        dic_tireur['nomClub'] = self.club.nomClub
        dic_tireur['classement'] = self.classement
        return dic_tireur
        
# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    __tablename__ = 'ARBITRE'
    idArbitre = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'))
    
    arbitre = db.relationship('Escrimeur', backref='Arbitre.numeroLicenceE')

    def __init__(self, numeroLicenceE):
        self.numeroLicenceE = numeroLicenceE
        

# Modèle pour représenter les participants aux compétitions
class ParticipantsCompetition(db.Model):
    __tablename__ = 'PARTICIPANTS_COMPETITION'
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('ESCRIMEUR.numeroLicenceE'), primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), primary_key=True)

    tireur = db.relationship('Escrimeur', backref='PartEscrimeur', foreign_keys=[numeroLicenceE])
    competition = db.relationship('Competition', backref='PartCompetition.idComp')
    
    def __init__(self, numeroLicenceE, idComp):
        self.numeroLicenceE = numeroLicenceE
        self.idComp = idComp

       
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
class Classement(db.Model):
    __tablename__ = 'CLASSEMENT'    
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), primary_key=True, nullable=False)
    numeroLicenceE = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), primary_key=True, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    competition = db.relationship('Competition', backref='competition')
    tireur = db.relationship('Tireur', backref='Tireur.numeroLicenceE')
    
    
    def __init__(self, comp, tireur, position):
        self.idComp = comp
        self.numeroLicenceE = tireur
        self.position = position

# Modèle pour représenter les poules
class Poule(db.Model):
    __tablename__ = 'POULE'
    idPoule = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idComp = db.Column(db.Integer, db.ForeignKey('COMPETITION.idComp'), nullable=False)
    idPiste = db.Column(db.Integer, db.ForeignKey('PISTE.idPiste'), nullable=False)
    idArbitre = db.Column(db.Integer, db.ForeignKey('ARBITRE.idArbitre'), nullable=False)
    nomPoule = db.Column(db.String(50), nullable=False)

    competition = db.relationship('Competition', backref='poules')
    piste = db.relationship('Piste', backref='Piste.idPiste')
    arbitre = db.relationship('Arbitre', backref='Arbitre.idArbitre')
    
    def __init__(self, competition, piste, arbitre, nom_poule):
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
class Match(db.Model):
    __tablename__ = 'MATCH'
    idMatch = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idTypeMatch = db.Column(db.Integer, db.ForeignKey('TYPE_MATCH.idTypeMatch'), nullable=False)
    gagnant = db.Column(db.Integer, db.ForeignKey('TIREUR.numeroLicenceE'), nullable=True)
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
    piste = db.relationship('Piste', backref='matches')
    arbitre = db.relationship('Arbitre', backref='matches')
    tireur1 = db.relationship('Tireur', foreign_keys=[numeroLicenceE1], backref='Tireur.numeroLicenceE1')
    tireur2 = db.relationship('Tireur', foreign_keys=[numeroLicenceE2], backref='Tireur.numeroLicenceE2')
    
    def __init__(self, type_match, poule, piste, arbitre, tireur1, tireur2, date_match, heure_match, touches_recues_tireur1, touches_donnees_tireur1, touches_recues_tireur2, touches_donnees_tireur2):
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
        
    def to_dict(self):
        return {
            'idTypeMatch': self.idTypeMatch,
            'idPoule': self.idPoule,
            'idPiste': self.idPiste,
            'idArbitre': self.idArbitre,
            'tireur1': Tireur.query.filter_by(numeroLicenceE = self.numeroLicenceE1).first(),
            'tireur2': Tireur.query.filter_by(numeroLicenceE = self.numeroLicenceE2).first(),
            'dateMatch': self.dateMatch.isoformat() if self.dateMatch else None,
            'heureMatch': self.heureMatch.isoformat() if self.heureMatch else None,
            'touchesRecuesTireur1': self.touchesRecuesTireur1,
            'touchesDonneesTireur1': self.touchesDonneesTireur1,
            'touchesRecuesTireur2': self.touchesRecuesTireur2,
            'touchesDonneesTireur2': self.touchesDonneesTireur2
        }

class User(db.Model, UserMixin):
    __tablename__ = 'USER'
    idUser = db.Column(db.Integer, primary_key=True)
    pseudoUser = db.Column(db.String (50), unique=True, nullable=False)
    mdpUser = db.Column(db.String (64), nullable=False)
    emailUser = db.Column(db.String (50), unique=True)
    statutUser = db.Column(db.String(50), nullable=False)
    def get_id(self):
        return self.idUser

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

def get_sample():
    return Competition.query.order_by(Competition.dateComp.desc()).all()

def get_competition_by_id(id_comp):
    return Competition.query.filter_by(idComp=id_comp).first()

def get_categories():
    categories = Categorie.query.all()
    return [categorie.nomCategorie for categorie in categories]


def get_saisons():
    saisons = Saison.query.all()
    return [saison.nomSaison for saison in saisons]

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
        if sexeE == "M":
            sexeE = "Homme"
        adherents_filtrer = [adherent for adherent in adherents_filtrer if adherent.Escrimeur.sexeE == sexeE]
    return adherents_filtrer

def get_id_lieu(nom_lieu):
    lieu = Lieu.query.filter_by(nomLieu=nom_lieu).first()
    return lieu.idLieu if lieu else None

def get_id_saison(nom_saison):
    saison = Saison.query.filter_by(nomSaison=nom_saison).first()
    return saison.idSaison if saison else None

def get_liste_participants_competitions_tireurs(id_comp):
    return ParticipantsCompetition.query.join(Tireur, ParticipantsCompetition.numeroLicenceE == Tireur.numeroLicenceE).filter(ParticipantsCompetition.idComp == id_comp).all()

def get_liste_tireurs_escrimeurs_poule(id_comp, id_poule):
    return Escrimeur.query.join(Tireur, Escrimeur.numeroLicenceE == Tireur.numeroLicenceE).join(ParticipantsPoule, Tireur.numeroLicenceE == ParticipantsPoule.numeroLicenceE).join(Poule, ParticipantsPoule.idPoule == Poule.idPoule).filter(Poule.idComp == id_comp).filter(Poule.idPoule == id_poule).all()

def get_club_tireur_escrimeur(tireur):
    return Club.query.join(Tireur, Club.idClub == Tireur.idClub).filter(Tireur.numeroLicenceE == tireur.numeroLicenceE).first()

def get_arbitre_escrimeur_poule(id_comp, id_poule):
    return Escrimeur.query.join(Arbitre, Escrimeur.numeroLicenceE == Arbitre.numeroLicenceE).join(Poule, Arbitre.idArbitre == Poule.idArbitre).filter(Poule.idComp == id_comp).filter(Poule.idPoule == id_poule).first()

def get_id_arbitre_poule(id_comp, id_poule):
    return Arbitre.query.join(Poule, Arbitre.idArbitre == Poule.idArbitre).filter(Poule.idComp == id_comp).filter(Poule.idPoule == id_poule).first().idArbitre

def get_piste_poule(id_comp, id_poule):
    # retourne la piste de la poule de cette compétition
    return Piste.query.join(Poule, Poule.idPiste == Piste.idPiste).filter(Poule.idComp == id_comp).filter(Poule.idPoule == id_poule).first()

def get_liste_participants_competitions_arbitres(id_comp):
    return ParticipantsCompetition.query.join(Arbitre, ParticipantsCompetition.numeroLicenceE == Arbitre.numeroLicenceE).filter(ParticipantsCompetition.idComp == id_comp).all()

def get_classement_tireur(num_licence):
    return Tireur.query.filter_by(numeroLicenceE=num_licence).first().classement

def get_id_club_tireur(num_licence):
    return Tireur.query.filter_by(numeroLicenceE=num_licence).first().idClub

def get_id_arbitre_from_escrimeur(numero_licence):
    arbitre = Arbitre.query.filter_by(numeroLicenceE=numero_licence).first()
    if arbitre:
        return arbitre.idArbitre
    
def get_nom_club_by_id(id_club):
    return Club.query.filter_by(idClub=id_club).first().nomClub

def classer_tireurs(tireurs):
    return sorted(tireurs, key=lambda tireur : get_classement_tireur(tireur.numeroLicenceE), reverse=True)

def poules_fabriquables(tireurs, arbitres):
    return True if 3 <= len(tireurs) // len(arbitres) <= 7 and len(tireurs) > 3 else False

def nb_poules_fabriquables(arbitres):
    return [[] for _ in range(len(arbitres))]

def get_nb_arbitres(id_comp):
    return ParticipantsCompetition.query.join(Arbitre, ParticipantsCompetition.numeroLicenceE == Arbitre.numeroLicenceE).filter(ParticipantsCompetition.idComp == id_comp).count()

def get_nb_tireurs(id_comp):
    return ParticipantsCompetition.query.join(Tireur, ParticipantsCompetition.numeroLicenceE == Tireur.numeroLicenceE).filter(ParticipantsCompetition.idComp == id_comp).count()

def get_liste_pistes_selon_nb_arbitres(id_comp, nb_arbitres):
    return Piste.query.filter_by(idComp=id_comp).limit(nb_arbitres).all()
    
            

def fabriquer_poules_selon_classement(tireurs, arbitres, pistes):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"
    
    liste_triee = classer_tireurs(tireurs)
    liste_poules = nb_poules_fabriquables(arbitres)
    tireurs_dans_poule = set()
    arbitres_dans_poule = set()
    pistes_associees = set()

    # Add one arbitre to each poule first
    for i in range(len(liste_poules)):
        if arbitres[i] not in arbitres_dans_poule and pistes[i] not in pistes_associees:
            escrimeur = Escrimeur.query.filter_by(numeroLicenceE=arbitres[i].numeroLicenceE).first()
            piste = pistes[i]
            nom_complet = f"{escrimeur.prenomE} {escrimeur.nomE}, {piste.nomPiste}"
            liste_poules[i].append((escrimeur, nom_complet))
            arbitres_dans_poule.add(arbitres[i])
            pistes_associees.add(pistes[i])
    for i in range(len(liste_triee)):
        if liste_triee[i] not in tireurs_dans_poule and liste_triee[i] not in arbitres_dans_poule:
            min_poule = min(liste_poules, key=len)
            escrimeur = Escrimeur.query.filter_by(numeroLicenceE=liste_triee[i].numeroLicenceE).first()
            nom_complet = f"{escrimeur.prenomE} {escrimeur.nomE}, Classement : {get_classement_tireur(escrimeur.numeroLicenceE)}"
            min_poule.append((escrimeur, nom_complet))
            tireurs_dans_poule.add(liste_triee[i])

    for i in range(len(liste_poules)):
        if liste_poules[i].count(liste_poules[i][0]) > 1:
            for j in range(len(liste_poules[i])):
                if liste_poules[i][j] == liste_poules[i][0]:
                    liste_poules[i][j] = liste_poules[i].pop()
                    break   

    mal_trie = False
    indice_mal_trie = None
    for i in range(len(liste_poules)):
        if len(liste_poules[i]) - 1 < 3:
            mal_trie = True
            indice_mal_trie = i
            break
    if mal_trie:
        for i in range(len(liste_poules)):
            if len(liste_poules[i]) - 1 > 3:
                liste_poules[indice_mal_trie].append(liste_poules[i].pop())
                break
    return liste_poules

def fabriquer_poules_decalage_club(tireurs, arbitres, pistes):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"

    liste_triee = classer_tireurs(tireurs)
    liste_poules = nb_poules_fabriquables(arbitres)
    num_poule = 0
    arbitres_dans_poule = set()
    pistes_associees = set()
    tireurs_dans_poule = set()
    for i in range(len(liste_triee)):
        if arbitres[i % len(arbitres)] not in arbitres_dans_poule and pistes[i % len(arbitres)] not in pistes_associees:
            escrimeur = Escrimeur.query.filter_by(numeroLicenceE=arbitres[i].numeroLicenceE).first()
            piste = pistes[i % len(arbitres)]
            nom_complet = f"{escrimeur.prenomE} {escrimeur.nomE}, {piste.nomPiste}"
            liste_poules[i].append((escrimeur, nom_complet))
            arbitres_dans_poule.add(arbitres[i])
            pistes_associees.add(pistes[i % len(arbitres)])
        if liste_triee[i] not in tireurs_dans_poule and liste_triee[i] not in arbitres_dans_poule:
            if len(liste_poules[i % len(arbitres)]) < 8:
                escrimeur = Escrimeur.query.filter_by(numeroLicenceE=liste_triee[i].numeroLicenceE).first()
                id_club_tireur = get_id_club_tireur(escrimeur.numeroLicenceE)
                nom_club_tireur = get_nom_club_by_id(id_club_tireur)
                nom_complet = f"{escrimeur.prenomE} {escrimeur.nomE}, Club : {nom_club_tireur}"
                if (escrimeur, nom_complet) not in liste_poules[i % len(arbitres)]:
                    liste_poules[i % len(arbitres)].append((escrimeur, nom_complet))
                else:
                    num_poule += 1
                    if num_poule % len(arbitres) == 0:
                        liste_poules[i % len(arbitres)].append((escrimeur, nom_complet))
                        num_poule = 0
                    else:
                        liste_poules[i % len(arbitres) + num_poule].append((escrimeur, nom_complet))
    mal_trie = False
    indice_mal_trie = None
    for i in range(len(liste_poules)):
        if len(liste_poules[i]) - 1 < 3:
            mal_trie = True
            indice_mal_trie = i
            break
    if mal_trie:
        for i in range(len(liste_poules)):
            if len(liste_poules[i]) - 1 > 3:
                liste_poules[indice_mal_trie].append(liste_poules[i].pop())
                break
    for i in range(len(liste_poules)):
        for j in range(len(liste_poules[i])):
            if liste_poules[i][j][0] in tireurs_dans_poule:
                tireurs_dans_poule.remove(liste_poules[i][j][0])
    return liste_poules

def fabriquer_poules(tireurs, arbitres, pistes, type_poule):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"
    match type_poule:
        case "Classement":
            liste_poules = fabriquer_poules_selon_classement(tireurs, arbitres, pistes)
        case "Club":
            liste_poules = fabriquer_poules_decalage_club(tireurs, arbitres, pistes)
    return liste_poules


def get_nb_arbitres(id_comp):
    return ParticipantsCompetition.query.join(Arbitre, ParticipantsCompetition.numeroLicenceE == Arbitre.numeroLicenceE).filter(ParticipantsCompetition.idComp == id_comp).count()

def get_nb_tireurs(id_comp):
    return ParticipantsCompetition.query.filter_by(idComp=id_comp).count() - get_nb_arbitres(id_comp)

def get_nb_poules(id_comp):
    return Poule.query.filter_by(idComp=id_comp).count()

def get_adherents():
    res =  db.session.query(Tireur, Escrimeur, Categorie) \
        .join(Escrimeur, Escrimeur.numeroLicenceE == Tireur.numeroLicenceE) \
        .join(Club, Club.idClub == Tireur.idClub) \
        .join(Categorie, Escrimeur.idCat == Categorie.idCat) \
        .filter(Club.nomClub == "BLOIS CE") \
        .add_columns(
            Tireur.idClub,
            Escrimeur.prenomE,
            Escrimeur.nomE,
            Escrimeur.dateNaissanceE,
            Escrimeur.numeroLicenceE,
            Escrimeur.sexeE,
            Escrimeur.numTelE,
            Categorie.nomCategorie
        ) \
        .all()
    return res

def get_adherents_adapte_json(gender=None):
    gender_filter = None
    if gender == 'H': 
        gender_filter = "Homme"
    elif gender == "F":
        gender_filter = "Femme"
    query = db.session.query(Escrimeur).join(Tireur, Escrimeur.numeroLicenceE == Tireur.numeroLicenceE).join(Club, Club.idClub == Tireur.idClub).join(Categorie, Escrimeur.idCat == Categorie.idCat).filter(Club.nomClub == "BLOIS CE")
    if gender_filter is not None:
        query = query.filter(Escrimeur.sexeE == gender_filter)
    return query.all()

def dernier_escrimeur_id():
    last_escrimeur = db.session.query(Escrimeur).order_by(Escrimeur.numeroLicenceE.desc()).first()
    if last_escrimeur:
        return last_escrimeur.numeroLicenceE
    else:
        return 0

def get_participants(id_comp, club=None):
    res = (
        db.session.query(ParticipantsCompetition, Escrimeur, Categorie)
        .join(Escrimeur, ParticipantsCompetition.numeroLicenceE == Escrimeur.numeroLicenceE)
        .join(Categorie, Escrimeur.idCat == Categorie.idCat)
        .join(Tireur, Tireur.numeroLicenceE == Escrimeur.numeroLicenceE)
        .join(Club, Club.idClub == Tireur.idClub)
        .outerjoin(Arbitre, Arbitre.numeroLicenceE == Escrimeur.numeroLicenceE)
        .filter(ParticipantsCompetition.idComp == id_comp)
        .filter(Arbitre.idArbitre == None)
    )
    if club is not None:
        if club == "!":
            res = res.filter(Club.nomClub != "BLOIS CE")
        else:
            res = res.filter(Club.nomClub == club)
    return res.add_columns(Escrimeur.prenomE, Escrimeur.nomE, Categorie.nomCategorie).all()

def get_liste_participants_competitions(id_comp):
    return ParticipantsCompetition.query.filter_by(idComp=id_comp).all()

def get_informations_escrimeur(numero_licence):
    return Escrimeur.query.filter_by(numeroLicenceE=numero_licence).first()

def get_id_poule(id_comp, id_piste, id_arbitre, nom_poule):
    return Poule.query.filter_by(idComp=id_comp, idPiste=id_piste, idArbitre=id_arbitre, nomPoule=nom_poule).first().idPoule

def get_arbitres(idcomp):
    arbitres = db.session.query(Arbitre, Escrimeur, Categorie).join(Escrimeur, Arbitre.numeroLicenceE == Escrimeur.numeroLicenceE).join(
        Categorie, Escrimeur.idCat == Categorie.idCat
    ).join(
        ParticipantsCompetition,
        ParticipantsCompetition.numeroLicenceE == Escrimeur.numeroLicenceE
    ).filter(ParticipantsCompetition.idComp == idcomp).all()
    print(arbitres)
    return arbitres

def get_competition_statut(competition):
    participants = ParticipantsCompetition.query.filter_by(idComp=competition.idComp).first()
    if participants:
        # verifie si les poules ont été créées pour la compétition
        poules = Poule.query.filter_by(idComp=competition.idComp).first()
        if poules:
            # verifie si l’appel a été fait donc sil ya des scores entrés pour des matchs de poules)
            try:
                match_poule = Match.query.filter_by(idComp=competition.idComp).first()
            except:
                match_poule = None
            if match_poule and (match_poule.touchesRecuesTireur1 is not None or match_poule.touchesDonneesTireur1 is not None
                                or match_poule.touchesRecuesTireur2 is not None or match_poule.touchesDonneesTireur2 is not None):
                return 'score'
            else:
                return 'appel'
        else:
            return 'participants'
    else:
        return 'participants'

def get_tireurs_from_poule(poule_id):
    return Tireur.query.join(ParticipantsPoule, Tireur.numeroLicenceE == ParticipantsPoule.numeroLicenceE).filter(ParticipantsPoule.idPoule == poule_id).all()

def count_victoires_for_tireur(tireur_num_licence):
    return Match.query.filter(Match.numeroLicenceE1 == tireur_num_licence, Match.touchesDonneesTireur1 > Match.touchesDonneesTireur2).count() + Match.query.filter(Match.numeroLicenceE2 == tireur_num_licence, Match.touchesDonneesTireur2 > Match.touchesDonneesTireur1).count()

def sum_touches_donnees_for_tireur(tireur_num_licence):
    sum1 = Match.query.filter(Match.numeroLicenceE1 == tireur_num_licence).with_entities(func.sum(Match.touchesDonneesTireur1)).scalar()
    sum2 = Match.query.filter(Match.numeroLicenceE2 == tireur_num_licence).with_entities(func.sum(Match.touchesDonneesTireur2)).scalar()
    return (sum1 if sum1 is not None else 0) + (sum2 if sum2 is not None else 0)

def sum_touches_recues_for_tireur(tireur_num_licence):
    sum1 = Match.query.filter(Match.numeroLicenceE1 == tireur_num_licence).with_entities(func.sum(Match.touchesRecuesTireur1)).scalar() or 0
    sum2 = Match.query.filter(Match.numeroLicenceE2 == tireur_num_licence).with_entities(func.sum(Match.touchesRecuesTireur2)).scalar() or 0
    return sum1 + sum2

def get_poule_stats(poule_id):
    poule_stats = {}
    tireurs = get_tireurs_from_poule(poule_id)
    for tireur in tireurs:
        victoires = count_victoires_for_tireur(tireur.numeroLicenceE)
        touches_donnees = sum_touches_donnees_for_tireur(tireur.numeroLicenceE)
        touches_recues = sum_touches_recues_for_tireur(tireur.numeroLicenceE)
        poule_stats[tireur.numeroLicenceE] = {
            'V': victoires,
            'TD': touches_donnees,
            'TR': touches_recues,
            'TD-TR': touches_donnees - touches_recues
        }
    return poule_stats

def get_matchs_poules(poule_id):
    return Match.query.filter_by(idPoule=poule_id).all()
    
def est_terminer_match(idMatch):
    match_poule = Match.query.filter_by(idMatch=idMatch).first()
    return match_poule.touchesDonneesTireur1 >= match_poule.type_match.nbnbTouches or match_poule.touchesDonneesTireur2 >= match_poule.type_match.nbnbTouches
    
def est_terminer_poule(idPoule):
    match_poules = Match.query.filter_by(idPoule=idPoule).all()
    for match_poule in match_poules:
        if not est_terminer_match(match_poule.idMatch):
            return False
    return True

def est_terminer_phase_poule(idComp):
    poules = Poule.query.filter_by(idComp=idComp).all()
    for poule in poules:
        if not est_terminer_poule(poule.idPoule):
            return False
    return True

def get_all_club():
    return Club.query.all()

def get_all_categories():
    return Categorie.query.all()

def get_nom_club_by_id(idClub):
    return Club.query.filter_by(idClub=idClub).first().nomClub
