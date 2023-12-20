from .models import *
from .app import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import csv

def get_id_categorie(nom_cat):
    categorie = Categorie.query.filter_by(nomCategorie=nom_cat).first()
    if categorie:
        return categorie.idCat
    else:
        return "La catégorie n'existe pas."
    
def get_id_arme(nom_arme):
    arme = Arme.query.filter_by(nomArme=nom_arme).first()
    if arme:
        return arme.idArme
    else:
        return "L'arme n'existe pas."
    
def get_id_club(nom_club):
    club = Club.query.filter_by(nomClub=nom_club).first()
    if club:
        return club.idClub
    else:
        return "Le club n'existe pas."

def ajouter_arme(nom_arme):
    if not nom_arme.strip():
        return "Le nom de l'arme ne peut pas être vide ou ne contenir que des espaces."
    try:
        # Commencez la transaction
        # Ajoutez l'arme à la base de données
        arme = Arme(nom_arme)
        arme_existe = Arme.query.filter_by(nomArme=nom_arme).first()
        if not arme_existe:
            db.session.add(arme)
        else :
            return f"L'arme {nom_arme} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"L'arme {nom_arme} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de l'arme déjà pris), annulez la transaction
        db.session.rollback()
        return f"L'arme {nom_arme} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'arme {nom_arme}: {str(e)}"

def ajouter_categorie(nom_categorie):
    if not nom_categorie.strip():
        return "Le nom de la catégorie ne peut pas être vide ou ne contenir que des espaces."
    try:
        # Commencez la transaction
        # Ajoutez la catégorie à la base de données
        categorie = Categorie(nom_categorie)
        categorie_existe = Categorie.query.filter_by(nomCategorie=nom_categorie).first()
        if not categorie_existe:
            db.session.add(categorie)
        else :
            return f"La catégorie {nom_categorie} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La catégorie {nom_categorie} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de la catégorie déjà pris), annulez la transaction
        db.session.rollback()
        return f"La catégorie {nom_categorie} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la catégorie {nom_categorie}: {str(e)}"

    
def ajouter_club(nom, region):
    if not nom.strip() or not region.strip():
        return "Le nom et la région du club ne peuvent pas être vides ou ne contenir que des espaces."
    club_existant = Club.query.filter_by(nomClub=nom).first()
    if club_existant:
        return f"Le club {nom} existe déjà."
    try:
        # Ajoutez le club à la base de données
        club = Club(nom, region)
        club_existe = Club.query.filter_by(nomClub=nom).first()
        if not club_existe:
            db.session.add(club)
        else :
            return f"Le club {nom} existe déjà."
        db.session.commit()  # Validez la transaction
        if db.session.is_active:
            print("Une transaction sur le club est en cours.")
        else:
            print("Aucune transaction en cours.")
        return f"Le club {nom} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom du club déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le nom du club {nom} est déjà pris."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du club : {str(e)}"

        
def ajouter_escrimeur(categorie, prenom, nom, str_date_naissance, str_license, sex, numTel):
    try:
        date_naissance = datetime.strptime(str_date_naissance, "%d/%m/%Y").date()
        numLicense = int(str_license)
    except ValueError:
        return "La date de naissance doit être au format valide (jour/mois/année) et le numéro de licence doit être un nombre."    
    if sex not in ("Homme", "Dames"):
        return "Le sexe doit être Homme ou Dames."
    elif sex == "Dames":
        sex = "Femme"    
    # Récupérez l'ID de la catégorie
    id_categorie = get_id_categorie(categorie)
    if isinstance(id_categorie, str):
        return id_categorie
    try:        
        # Ajoutez l'escrimeur à la base de données
        escrimeur = Escrimeur(id_categorie, prenom, nom,
                            date_naissance, numLicense, 
                            sex, numTel)        
        # Utilisez session.add_all pour ajouter les objets en une seule fois
        db.session.add(escrimeur)
        db.session.commit()    
        return f"L'escrimeur {prenom} {nom} a été ajouté avec succès."    
    except IntegrityError:
        db.session.rollback()
        return "L'escrimeur existe déjà dans la base de données."    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'escrimeur : {str(e)}"

        
def ajouter_tireur_via_str(str_licence, nomClub, classement):
    try:
        numLicense = int(str_licence)
    except ValueError:
        return "Le numéro de licence doit être un nombre."
    
    id_club = get_id_club(nomClub)
    if isinstance(id_club, str):
        return id_club
    
    try:
        
        # Ajoutez l'escrimeur à la base de données
        tireur = Tireur(num_licence = numLicense, club = id_club, classement = classement)
        
        # Utilisez session.add_all pour ajouter les objets en une seule fois
        db.session.add(tireur)
        db.session.commit()
        
        prenom = tireur.escrimeur.prenomE
        nom = tireur.escrimeur.nomE
        return f"Le tireur {prenom} {nom} a été ajouté avec succès."
    except IntegrityError:
        db.session.rollback()
        return "Le tireur existe déjà dans la base de données."
    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du tireur : {str(e)}"

        
def pratiquer_arme(str_licence, arme):
    try:
        numLicense = int(str_licence)
    except ValueError:
        return "Le numéro de licence doit être un nombre."

    id_arme = get_id_arme(arme)
    if isinstance(id_arme, str):
        return id_arme

    try:
        # Vérifiez si l'escrimeur pratique déjà cette arme
        escrimeur = Escrimeur.query.filter_by(numeroLicenceE=numLicense).first()
        if escrimeur and any(arme_pratiquee.id_arme_fk == id_arme for arme_pratiquee in escrimeur.armes_pratiquees):
            return f"L'escrimeur {escrimeur.nomE} {escrimeur.prenomE} pratique déjà l'arme {arme}, {id_arme}."

        # Ajoutez l'escrimeur à la base de données
        pratiquer = PratiquerArme(numero_licence_e_fk=numLicense, id_arme_fk=id_arme)
        db.session.add(pratiquer)
        db.session.commit()

        return f"L'escrimeur {escrimeur.nomE} {escrimeur.prenomE} pratique maintenant l'arme {arme}, {id_arme}."

    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'arme {arme}, {id_arme} pratiquée par {numLicense} : {str(e)}"


def creer_competition(nomLieu, nomSaison, nomCat, nomArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle):
    try:
        # Obtenez les identifiants à partir des noms
        idLieu = get_id_lieu(nomLieu)
        idSaison = get_id_saison(nomSaison)
        idCat = get_id_categorie(nomCat)
        idArme = get_id_arme(nomArme)

        # Vérifiez que les identifiants sont valides
        if None in (idLieu, idSaison, idCat, idArme):
            return "Erreur : Impossible d'obtenir les identifiants nécessaires."

        # Convertissez la date et l'heure de format texte en objets datetime et time
        date_comp = datetime.strptime(dateComp, "%Y-%m-%d").date()
        heure_comp = datetime.strptime(heureComp, "%H:%M").time()

        # Ajoutez la compétition à la base de données
        competition = Competition(
            idLieu=idLieu,
            idSaison=idSaison,
            idCat=idCat,
            idArme=idArme,
            nomComp=nomComp,
            descComp=descComp,
            dateComp=date_comp,
            heureComp=heure_comp,
            sexeComp=sexeComp,
            estIndividuelle=estIndividuelle
        )
        db.session.add(competition)
        db.session.commit()

        return f"La compétition {nomComp} a été créée avec succès."
    
    except IntegrityError:
        db.session.rollback()
        return "Une compétition avec ce nom existe déjà."
    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de la création de la compétition {nomComp}: {str(e)}"
    
def ajouter_competition(idLieu, idSaison, idArme, idCat, nomComp, descComp, date_comp, heure_comp, sexeComp, estIndividuelle):
    try:
        idLieu = int(idLieu)
    except ValueError:
        return "L'identifiant du lieu doit être un nombre."
    try:
        idArme = int(idArme)
    except ValueError:
        return "L'identifiant de l'arme doit être un nombre."
    try:
        idCat = int(idCat)
    except ValueError:
        return "L'identifiant de la catégorie doit être un nombre."
    try:
        date_comp = datetime.strptime(date_comp, "%Y-%m-%d").date()
        heure_comp = datetime.strptime(heure_comp, "%H:%M:%S").time()
    except ValueError:
        return "La date et l'heure doivent être au format valide (année-mois-jour heure:minute:seconde)"
    try:
        idSaison = int(idSaison)
    except ValueError:
        return "L'identifiant de la saison doit être un nombre."
    if isinstance(estIndividuelle, str):
        if estIndividuelle.lower() == 'true':
            estIndividuelle = True
        else :
            estIndividuelle = False
    try:
        # Ajoutez la compétition à la base de données
        competition = competition = Competition(
            idLieu=idLieu,
            idSaison=idSaison,
            idCat=idCat,
            idArme=idArme,
            nomComp=nomComp,
            descComp=descComp,
            dateComp=date_comp,
            heureComp=heure_comp,
            sexeComp=sexeComp,
            estIndividuelle=estIndividuelle
        )
        competition_existe = Competition.query.filter_by(nomComp=nomComp).first()
        if not competition_existe:
            db.session.add(competition)
        else :
            return f"La compétition {nomComp} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La compétition {nomComp} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de la compétition déjà pris), annulez la transaction
        db.session.rollback()
        return f"La compétition {nomComp} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur c'est produite lors de l'ajout de la compétition : {str(e)}"
    
def ajouter_lieu(nomLieu, adresseLieu, villeLieu, codePostalLieu):
    try:
        try :
            codePostalLieu = int(codePostalLieu)
        except ValueError:
            return (f"Le code postal doit être un nombre. {codePostalLieu}")
        # Ajoutez le lieu à la base de données
        lieu = Lieu(nom_lieu = nomLieu, ville_lieu = villeLieu, code_postal_lieu = codePostalLieu,adresse_lieu = adresseLieu)
        lieu_existe = Lieu.query.filter_by(nomLieu=nomLieu).first()
        if not lieu_existe:
            db.session.add(lieu)
        else :
            return f"Le lieu {nomLieu} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le lieu {nomLieu} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom du lieu déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le lieu {nomLieu} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du lieu : {str(e)}"
    
def ajouter_saison(nomSaison, dateDebutSaison, dateFinSaison):
    try:
        dateDebutSaison = datetime.strptime(dateDebutSaison, "%Y-%m-%d").date()
        dateFinSaison = datetime.strptime(dateFinSaison, "%Y-%m-%d").date()
        # Ajoutez la saison à la base de données
        saison = Saison(nom_saison = nomSaison, date_debut_saison = dateDebutSaison, date_fin_saison = dateFinSaison)
        saison_existe = Saison.query.filter_by(nomSaison=nomSaison).first()
        if not saison_existe:
            db.session.add(saison)
        else :
            return f"La saison {nomSaison} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La saison {nomSaison} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de la saison déjà pris), annulez la transaction
        db.session.rollback()
        return f"La saison {nomSaison} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la saison : {str(e)}"
    
def ajouter_type_match(nomTypeMatch, nbTouches):
    try:
        # Ajoutez le type de match à la base de données
        try :
            nbTouches = int(nbTouches)
        except ValueError:
            return "Le nombre de touches doit être un nombre."
        type_match = TypeMatch(nom_type_match = nomTypeMatch, nb_touches = nbTouches)
        type_match_existe = TypeMatch.query.filter_by(nomTypeMatch=nomTypeMatch).first()
        if not type_match_existe:
            db.session.add(type_match)
        else :
            return f"Le type de match {nomTypeMatch} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le type de match {nomTypeMatch} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom du type de match déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le type de match {nomTypeMatch} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du type de match : {str(e)}"
    
def ajouter_piste(idComp, nomPiste, estDispo):
    try:
        # Ajoutez la piste à la base de données
        if isinstance(estDispo, str):
            estDispo = estDispo.lower()
            if estDispo == 'true':
                estDispo = True
            else :
                estDispo = False
        piste = Piste(competition = idComp, nom_piste = nomPiste, est_dispo = estDispo)
        piste_existe = Piste.query.filter_by(nomPiste=nomPiste, idComp = idComp).first()
        if not piste_existe:
            db.session.add(piste)
        else :
            return f"La piste {nomPiste} pour la compétition {idComp} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La piste {nomPiste} pour la compétition {idComp} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de la piste déjà pris), annulez la transaction
        db.session.rollback()
        return f"La piste {nomPiste} pour la compétition {idComp} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la piste : {str(e)}"

def ajouter_tireur(numLicenceE, idClub, classement):
    try :
        numLicenceE = int(numLicenceE)
    except ValueError:
        return "Le numéro de licence doit être un nombre."
    try:
        idClub = int(idClub)
    except ValueError:
        return "L'identifiant du club doit être un nombre."
    try:
        classement = int(classement)
    except ValueError:
        return "Le classement doit être un nombre."
    try:
        # Ajoutez le tireur à la base de données
        tireur = Tireur( num_licence = numLicenceE, club = idClub, classement = classement)
        db.session.add(tireur)
        db.session.commit()  # Validez la transaction
        return f"Le tireur {numLicenceE} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le tireur {numLicenceE} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du tireur : {str(e)}"

def ajouter_arbitre(numeroLicenceE):
    try:
        numeroLicenceE = int(numeroLicenceE)
    except ValueError:
        return "Le numéro de licence doit être un nombre."
    try:
        # Ajoutez l'arbitre à la base de données
        arbitre = Arbitre(numeroLicenceE = numeroLicenceE)
        arbitre_existe = Arbitre.query.filter_by(numeroLicenceE=numeroLicenceE).first()
        if not arbitre_existe:
            db.session.add(arbitre)
        else :
            return f"L'arbitre {numeroLicenceE} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"L'arbitre {numeroLicenceE} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"L'arbitre {numeroLicenceE} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'arbitre : {str(e)}"

def ajouter_participant(numeroLicenceE, idComp):
    try:
        numeroLicenceE = int(numeroLicenceE)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        idComp = int(idComp)
    except ValueError:
        return "L'identifiant de la compétition doit être un nombre."
    try:
        # Ajoutez le participant à la base de données
        participant = ParticipantsCompetition(numeroLicenceE = numeroLicenceE, idComp = idComp)
        participant_existe = ParticipantsCompetition.query.filter_by(numeroLicenceE=numeroLicenceE, idComp=idComp).first()
        if not participant_existe:
            db.session.add(participant)
        else :
            return f"Le participant {numeroLicenceE} existe déjà pour la compétition {idComp}."
        db.session.commit()  # Validez la transaction
        return f"Le participant {numeroLicenceE} a été ajouté avec succès pour la compétition {idComp}."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le participant {numeroLicenceE} existe déjà pour la compétition {idComp}."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du participant {numeroLicenceE} pour la compétition {idComp} : {str(e)}"
    
def ajouter_classement_final(idComp, numeroLicenceE, classement):
    try:
        idComp = int(idComp)
    except ValueError:
        return "L'identifiant de la compétition doit être un nombre."
    try:
        numeroLicenceE = int(numeroLicenceE)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        classement = int(classement)
    except ValueError:
        return "Le classement doit être un nombre."
    try:
        # Ajoutez le classement final à la base de données
        classement_final = ClassementFinal(comp = idComp, tireur = numeroLicenceE, position = classement)
        classement_final_existe = ClassementFinal.query.filter_by(idComp=idComp, numeroLicenceE=numeroLicenceE).first()
        if not classement_final_existe:
            db.session.add(classement_final)
        else :
            return f"Le classement final {idComp} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le classement final {idComp} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le classement final {idComp} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du classement final : {str(e)}"

def ajouter_poule(idComp, idPiste, idArbitre, nomPoule):
    try:
        idComp = int(idComp)
    except ValueError:
        return "L'identifiant de la compétition doit être un nombre."
    try:
        idPiste = int(idPiste)
    except ValueError:
        return "L'identifiant de la piste doit être un nombre."
    try:
        idArbitre = int(idArbitre)
    except ValueError:
        return "L'identifiant de l'arbitre doit être un nombre."
    try:
        # Ajoutez la poule à la base de données
        poule = Poule(competition = idComp, piste = idPiste, arbitre = idArbitre, nom_poule = nomPoule)
        poule_existe = Poule.query.filter_by(idComp=idComp, idPiste = idPiste).first()
        if not poule_existe:
            db.session.add(poule)
        else:
            return f"La poule {idComp} pour la piste {idPiste} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La poule {idComp} pour la piste {idPiste} a été ajoutée avec succès."
    # except IntegrityError:
    #     # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
    #     db.session.rollback()
    #     return f"La poule {idComp} pour la piste {idPiste} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la poule : {str(e)}"

def ajouter_participant_poule(idPoule, numeroLicenceE):
    try:
        idPoule = int(idPoule)
    except ValueError:
        return "L'identifiant de la poule doit être un nombre."
    try:
        numeroLicenceE = int(numeroLicenceE)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        # Ajoutez le participant à la base de données
        participant_poule = ParticipantsPoule(poule = idPoule, tireur = numeroLicenceE)
        participant_poule_existe = ParticipantsPoule.query.filter_by(idPoule=idPoule, numeroLicenceE=numeroLicenceE).first()
        if not participant_poule_existe:
            db.session.add(participant_poule)
        else :
            return f"Le participant poule {idPoule} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le participant poule {idPoule} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le participant poule {idPoule} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite participant poule : {str(e)}"
    
def ajouter_match_poule(idTypeMatch, idPoule, idPiste, idArbitre, numeroLicenceE1, numeroLicenceE2, dateMatch, heureMatch, toucheRecuTireur1, toucheDonnerTireur1, toucheRecuTireur2, toucheDonnerTireur2):
    try:
        idTypeMatch = int(idTypeMatch)
        idPoule = int(idPoule)
        idPiste = int(idPiste)
        idArbitre = int(idArbitre)
        numeroLicenceE1 = int(numeroLicenceE1)
        numeroLicenceE2 = int(numeroLicenceE2)
        toucheRecuTireur1 = int(toucheRecuTireur1)
        toucheDonnerTireur1 = int(toucheDonnerTireur1)
        toucheRecuTireur2 = int(toucheRecuTireur2)
        toucheDonnerTireur2 = int(toucheDonnerTireur2)
        dateMatch = datetime.strptime(dateMatch, "%Y-%m-%d").date()
        heureMatch = datetime.strptime(heureMatch, "%H:%M:%S").time()

        # Vérifiez si le match poule existe
        match_poule_existe = (
            MatchPoule.query
            .filter_by(
                idTypeMatch=idTypeMatch,
                idPoule=idPoule,
                idPiste=idPiste,
                idArbitre=idArbitre,
                numeroLicenceE1=numeroLicenceE1,
                numeroLicenceE2=numeroLicenceE2
            )
            .first()
        )

        if not match_poule_existe:
            # Si le match poule n'existe pas, ajoutez-le à la base de données
            match_poule = MatchPoule(
                type_match=idTypeMatch,
                poule=idPoule,
                piste=idPiste,
                arbitre=idArbitre,
                tireur1=numeroLicenceE1,
                tireur2=numeroLicenceE2,
                date_match=dateMatch,
                heure_match=heureMatch,
                touches_recues_tireur1=toucheRecuTireur1,
                touches_donnees_tireur1=toucheDonnerTireur1,
                touches_recues_tireur2=toucheRecuTireur2,
                touches_donnees_tireur2=toucheDonnerTireur2
            )
            db.session.add(match_poule)
            db.session.commit()
            return f"Le match poule {idTypeMatch} a été ajouté avec succès."
        else:
            return f"Le match poule {idTypeMatch} existe déjà."
    except ValueError:
        return "Assurez-vous que les valeurs numériques sont correctes."
    except IntegrityError:
        db.session.rollback()
        return f"Le match poule {idTypeMatch} existe déjà."
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du match poule : {str(e)}"


def ajouter_feuille_match(idPoule, idComp, numeroLicenceE1, numeroLicenceE2, scoreTireur1, scoreTireur2):
    try:
        idPoule = int(idPoule)
        idComp = int(idComp)
        numeroLicenceE1 = int(numeroLicenceE1)
        numeroLicenceE2 = int(numeroLicenceE2)
        
        if scoreTireur1 != 'null' and scoreTireur2 != 'null' and scoreTireur1 != 'Null' and scoreTireur2 != 'Null':
            scoreTireur1 = int(scoreTireur1)
            scoreTireur2 = int(scoreTireur2)
        else:
            scoreTireur1 = None
            scoreTireur2 = None

        # Vérifiez si la feuille de match existe
        feuille_match_existe = (
            FeuilleMatch.query
            .filter_by(
                idPoule=idPoule,
                idComp=idComp,
                numeroLicenceE1=numeroLicenceE1,
                numeroLicenceE2=numeroLicenceE2
            )
            .first()
        )

        if not feuille_match_existe:
            # Si la feuille de match n'existe pas, ajoutez-la à la base de données
            feuille_match = FeuilleMatch(
                poule=idPoule,
                competition=idComp,
                tireur1=numeroLicenceE1,
                tireur2=numeroLicenceE2,
                score_tireur1=scoreTireur1,
                score_tireur2=scoreTireur2
            )
            db.session.add(feuille_match)
            db.session.commit()
            return f"La feuille de match de poule {idPoule} pour la compétition {idComp} entre {numeroLicenceE1} et {numeroLicenceE2} a été ajoutée avec succès."
        else:
            return f"La feuille de match de poule {idPoule} pour la compétition {idComp} entre {numeroLicenceE1} et {numeroLicenceE2} existe déjà."
    except ValueError:
        return "Assurez-vous que les valeurs numériques sont correctes."
    except IntegrityError:
        db.session.rollback()
        return f"La feuille de match de poule {idPoule} pour la compétition {idComp} entre {numeroLicenceE1} et {numeroLicenceE2} existe déjà."
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite feuille de match : {str(e)}"
    
    
def load_lieu(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                nom_lieu = row['nomLieu']
                ville = row['villeLieu']
                codePostale = row['codePostalLieu']
                adresse = row['adresseLieu']
                print(ajouter_lieu(nom_lieu, adresse, ville, codePostale))
            return f"Les données du fichier {file_name} ont été ajoutées à la base de données."
    except Exception as e:
        db.session.rollback()
        return f"Erreur lors du traitement du fichier {file_name}: {e}"
        
def load_saison(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                nom = row['nomSaison']
                debut = row['dateDebutSaison']
                fin = row['dateFinSaison']
                print(ajouter_saison(nom, debut, fin))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_type_match(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                nom = row['nomTypeMatch']
                nbTouches = row['nbTouches']
                return(ajouter_type_match(nom, nbTouches))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")

def load_competition(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                idLieu = row['idLieu']
                saison = row['idSaison']
                idArme = row['idArme']
                idCat = row['idCat']
                nomComp = row['nomComp']
                desc_competition = row['descComp']
                date_competition = row['dateComp']
                heure_competition = row['heureComp']
                sexe_competition = row['sexeComp']
                est_individuelle = row['estIndividuelle']
                print(ajouter_competition(idLieu, saison, idArme, idCat, nomComp, desc_competition, date_competition, heure_competition, sexe_competition, est_individuelle))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")

def load_piste(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                idComp = row['idComp']
                nomPiste = row['nomPiste']
                estDispo = row['estDispo']
                print(ajouter_piste(idComp, nomPiste, estDispo))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
    
def load_tireur(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                numLicence = row['numeroLicenceE']
                idClub = row['idClub']
                classement = row['classement']
                print(ajouter_tireur(numLicence, idClub, classement))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_arbitre(file_name, db):
    try :
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                numLicence = row['numeroLicenceE']
                print(ajouter_arbitre(numLicence))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_participants_comp(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                numeroLicenceE = row['numeroLicenceE']
                idComp = row['idComp']
                print(ajouter_participant(numeroLicenceE, idComp))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")

def load_classement_final(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: 
                numeroLicenceE = row['numeroLicenceE']
                idComp = row['idComp']
                rang = row['position']
                print(ajouter_classement_final(idComp, numeroLicenceE, rang))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")

def load_poule(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: 
                idComp = row['idComp']
                idPiste = row['idPiste']
                idArbitre = row['idArbitre']
                nomPoule = row['nomPoule']
                print(ajouter_poule(idComp, idPiste, idArbitre, nomPoule))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_participants_poule(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: 
                idPoule = row['idPoule']
                numeroLicenceE = row['numeroLicenceE']
                print(ajouter_participant_poule(idPoule, numeroLicenceE))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_match_poule(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: 
                idTypeMatch = row['idTypeMatch']
                idPoule = row['idPoule']
                idPiste = row['idPiste']
                idArbitre = row['idArbitre']
                numeroLicenceE1 = row['numeroLicenceE1']
                numeroLicenceE2 = row['numeroLicenceE2']
                dateMatch = row['dateMatch']
                heureMatch = row['heureMatch']
                toucheRecuTireur1 = row['touchesRecuesTireur1']
                toucheDonnerTireur1 = row['touchesDonneesTireur1']
                toucheRecuTireur2 = row['touchesRecuesTireur2']
                toucheDonnerTireur2 = row['touchesDonneesTireur2']
                print(ajouter_match_poule(idTypeMatch, idPoule, idPiste, idArbitre, numeroLicenceE1, numeroLicenceE2, dateMatch, heureMatch, toucheRecuTireur1, toucheDonnerTireur1, toucheRecuTireur2, toucheDonnerTireur2))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()        
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
        
def load_feuille_match(file_name, db):
    try:
        with open(file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader: 
                idPoule = row['idPoule']
                idComp = row['idComp']
                numeroLicenceE1 = row['numeroLicenceE1']
                numeroLicenceE2 = row['numeroLicenceE2']
                scoreTireur1 = row['scoreTireur1']
                scoreTireur2 = row['scoreTireur2']
                print(ajouter_feuille_match(idPoule, idComp, numeroLicenceE1, numeroLicenceE2, scoreTireur1, scoreTireur2))
        return(f"Les données du fichier {file_name} ont été ajoutées à la base de données.")
    except Exception as e:
        db.session.rollback()
        return(f"Erreur lors du traitement du fichier {file_name}: {e}")
    
fonctions_csv = {
    "lieu.csv": load_lieu,
    "saison.csv": load_saison,
    "type_match.csv": load_type_match,
    "competition.csv": load_competition,
    "piste.csv": load_piste,
    "tireur.csv": load_tireur,
    "arbitre.csv": load_arbitre,
    "participants_comp.csv": load_participants_comp,
    "classement_final.csv": load_classement_final,
    "poule.csv": load_poule,
    "participants_poule.csv": load_participants_poule,
    "match_poule.csv": load_match_poule,
    "feuille_match.csv": load_feuille_match
}

priorite_fichier = {
    "lieu.csv": "1",
    "saison.csv": "2",
    "type_match.csv": "3",
    "competition.csv": "4",
    "piste.csv": "5",
    "tireur.csv": "6",
    "arbitre.csv": "7",
    "participants_comp.csv": "8",
    "classement_final.csv": "9",
    "poule.csv": "10",
    "participants_poule.csv": "11",
    "match_poule.csv": "12",
    "feuille_match.csv": "13"
}