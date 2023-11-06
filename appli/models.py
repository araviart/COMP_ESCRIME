from .app import db

# Modèle pour représenter le lieu
class Lieu(db.Model):
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
    idArme = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomArme = db.Column(db.String(50), nullable=False)

    def __init__(self, id_arme, nom_arme):
        self._id_arme = id_arme
        self._nom_arme = nom_arme

# Modèle pour représenter la saison
class Saison(db.Model):
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
    idCat = db.Column(db.Integer, primary_key=True)
    nomCategorie = db.Column(db.String(50), nullable=False)
    
    def __init__(self, id_cat, nom_categorie):
        self._id_cat = id_cat
        self._nom_categorie = nom_categorie

# Modèle pour représenter le club
class Club(db.Model):
    idClub = db.Column(db.Integer, primary_key=True)
    nomClub = db.Column(db.String(50), nullable=False)
    villeClub = db.Column(db.String(50), nullable=False)
    
    def __init__(self, id_club, nom_club, ville_club):
        self._id_club = id_club
        self._nom_club = nom_club
        self._ville_club = ville_club

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
    
    def __init__(self, id_comp, lieu, saison, categorie, arme, nom_comp, desc_comp, date_comp, heure_comp, sexe_comp, est_individuelle):
        self._id_comp = id_comp
        self._lieu = lieu
        self._saison = saison
        self._categorie = categorie
        self._id_arme = arme
        self._nom_comp = nom_comp
        self._desc_comp = desc_comp
        self._date_comp = date_comp
        self._heure_comp = heure_comp
        self._sexe_comp = sexe_comp
        self._est_individuelle = est_individuelle

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
    
    def __init__(self, id_piste, competition, nom_piste, est_dispo):
        self._id_piste = id_piste
        self._competition = competition
        self._nom_piste = nom_piste
        self._est_dispo = est_dispo

# Modèle pour représenter le type de match
class TypeMatch(db.Model):
    idTypeMatch = db.Column(db.Integer, primary_key=True)
    nomTypeMatch = db.Column(db.String(50), nullable=False)
    nbTouches = db.Column(db.Integer, nullable=False)
    
    def __init__(self, id_type_match, nom_type_match, nb_touches):
        self._id_type_match = id_type_match
        self._nom_type_match = nom_type_match
        self._nb_touches = nb_touches

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

    def __init__(self, id_escrimeur, categorie, prenom_e, nom_e, date_naissance_e, numero_licence_e, sexe_e, num_tel_e):
        self._id_escrimeur = id_escrimeur
        self._categorie = categorie
        self._prenom_e = prenom_e
        self._nom_e = nom_e
        self._date_naissance_e = date_naissance_e
        self._numero_licence_e = numero_licence_e
        self._sexe_e = sexe_e
        self._num_tel_e = num_tel_e
        
# Modèle pour représenter les tireurs
class Tireur(db.Model):
    idTireur = db.Column(db.Integer, primary_key=True)
    idClub = db.Column(db.Integer, db.ForeignKey('club.idClub'), nullable=False)
    classement = db.Column(db.Integer, nullable=False)

    club = db.relationship('Club')

    def __init__(self, escrimeur, club, classement):
        self._escrimeur = escrimeur
        self._club = club
        self._classement = classement
        
# Modèle pour représenter les arbitres
class Arbitre(db.Model):
    idArbitre = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, escrimeur):
        self._escrimeur = escrimeur

# Modèle pour représenter la relation entre les escrimeurs et les armes qu'ils pratiquent
class PratiquerArme(db.Model):
    idEscrimeur = db.Column(db.Integer, db.ForeignKey('escrimeur.idEscrimeur'), primary_key=True)
    idArme = db.Column(db.Integer, db.ForeignKey('arme.idArme'), primary_key=True)

    escrimeur = db.relationship('Escrimeur')
    arme = db.relationship('Arme')
    
    def __init__(self, escrimeur, arme):
        self._escrimeur = escrimeur
        self._arme = arme

# Modèle pour représenter le classement final
class ClassementFinal(db.Model):
    idClassementFinal = db.Column(db.Integer, primary_key=True)
    idComp = db.Column(db.Integer, db.ForeignKey('competition.idComp'), nullable=False)
    idTireur = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    competition = db.relationship('Competition')
    tireur = db.relationship('Tireur')
    
    def __init__(self, id_classement_final, comp, tireur, position):
        self._id_classement_final = id_classement_final
        self._comp = comp
        self._tireur = tireur
        self._position = position

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
    
    def __init__(self, id_poule, competition, piste, arbitre, nom_poule):
        self._id_poule = id_poule
        self._competition = competition
        self._piste = piste
        self._arbitre = arbitre
        self._nom_poule = nom_poule

# Modèle pour représenter les participants aux poules
class ParticipantsPoule(db.Model):
    idPoule = db.Column(db.Integer, db.ForeignKey('poule.idPoule'), primary_key=True)
    idTireur = db.Column(db.Integer, db.ForeignKey('tireur.idTireur'), primary_key=True)

    poule = db.relationship('Poule')
    tireur = db.relationship('Tireur')
    
    def __init__(self, poule, tireur):
        self._poule = poule
        self._tireur = tireur

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
    
    def __init__(self, id_feuille, poule, competition, tireur1, tireur2, score_tireur1, score_tireur2):
        self._id_feuille = id_feuille
        self._poule = poule
        self._competition = competition
        self._tireur1 = tireur1
        self._tireur2 = tireur2
        self._score_tireur1 = score_tireur1
        self._score_tireur2 = score_tireur2
