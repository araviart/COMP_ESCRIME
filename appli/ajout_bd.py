from .models import *
from .app import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError

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

        
def ajouter_tireur(str_licence, nomClub, classement):
    try:
        numLicense = int(str_licence)
    except ValueError:
        return "Le numéro de licence doit être un nombre."
    
    id_club = get_id_club(nomClub)
    if isinstance(id_club, str):
        return id_club
    
    try:
        
        # Ajoutez l'escrimeur à la base de données
        tireur = Tireur(numLicense, id_club, classement)
        
        # Utilisez session.add_all pour ajouter les objets en une seule fois
        db.session.add(tireur)
        db.session.commit()
        
        prenom = tireur.num_licence.prenomE
        nom = tireur.num_licence.nomE
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
    
def ajouter_lieu(nomLieu, adresseLieu, villeLieu, codePostalLieu):
    try:
        try :
            codePostalLieu = int(codePostalLieu)
        except ValueError:
            return "Le code postal doit être un nombre."
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
        estDispo = estDispo.lower() == 'true'
        piste = Piste(competition = idComp, nom_piste = nomPiste, est_dispo = estDispo)
        piste_existe = Piste.query.filter_by(nomPiste=nomPiste).first()
        if not piste_existe:
            db.session.add(piste)
        else :
            return f"La piste {nomPiste} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La piste {nomPiste} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom de la piste déjà pris), annulez la transaction
        db.session.rollback()
        return f"La piste {nomPiste} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la piste : {str(e)}"

def ajouter_tireur(numLicence, idClub, classement):
    try :
        numLicence = int(numLicence)
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
        tireur = Tireur( num_licence = numLicence, club = idClub, classement = classement)
        tireur_existe = Tireur.query.filter_by(numLicence=numLicence).first()
        if not tireur_existe:
            db.session.add(tireur)
        else :
            return f"Le tireur {numLicence} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le tireur {numLicence} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le tireur {numLicence} existe déjà."
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

def ajouter_participant(idTireur, idComp):
    try:
        idTireur = int(idTireur)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        idComp = int(idComp)
    except ValueError:
        return "L'identifiant de la compétition doit être un nombre."
    try:
        # Ajoutez le participant à la base de données
        tireur = Tireur.query.filter_by(numLicence=idTireur).first()
        participant = ParticipantsCompetition(numeroLicenceE = tireur.numeroLicenceE, idComp = idComp)
        participant_existe = ParticipantsCompetition.query.filter_by(idTireur=idTireur, idComp=idComp).first()
        if not participant_existe:
            db.session.add(participant)
        else :
            return f"Le participant {idTireur} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le participant {idTireur} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le participant {idTireur} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du participant : {str(e)}"
    
def ajouter_classement_final(idComp, idTireur, classement):
    try:
        idComp = int(idComp)
    except ValueError:
        return "L'identifiant de la compétition doit être un nombre."
    try:
        idTireur = int(idTireur)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        classement = int(classement)
    except ValueError:
        return "Le classement doit être un nombre."
    try:
        # Ajoutez le classement final à la base de données
        classement_final = ClassementFinal(idComp = idComp, idTireur = idTireur, classement = classement)
        classement_final_existe = ClassementFinal.query.filter_by(idComp=idComp, idTireur=idTireur).first()
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
        poule_existe = Poule.query.filter_by(idComp=idComp).first()
        if not poule_existe:
            db.session.add(poule)
        else :
            return f"La poule {idComp} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"La poule {idComp} a été ajoutée avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"La poule {idComp} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de la poule : {str(e)}"

def ajouter_participant_poule(idPoule, idTireur):
    try:
        idPoule = int(idPoule)
    except ValueError:
        return "L'identifiant de la poule doit être un nombre."
    try:
        idTireur = int(idTireur)
    except ValueError:
        return "L'identifiant du tireur doit être un nombre."
    try:
        # Ajoutez le participant à la base de données
        tireur = Tireur.query.filter_by(numLicence=idTireur).first()
        participant_poule = ParticipantsPoule(poule = idPoule, tireur = tireur.numeroLicenceE)
        participant_poule_existe = ParticipantsPoule.query.filter_by(idPoule=idPoule, idTireur=idTireur).first()
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
    
def ajouter_match_poule(idTypeMatch, idPoule, idPiste, idArbitre, idTireur1, idTireur2, dateMatch, heureMatch, toucheRecuTireur1, toucheDonnerTireur1, toucheRecuTireur2, toucheDonnerTireur2):
    try :
        idTypeMatch = int(idTypeMatch)
    except ValueError:
        return "L'identifiant du type de match doit être un nombre."
    try:
        idPoule = int(idPoule)
    except ValueError:
        return "L'identifiant de la poule doit être un nombre."
    try:
        idPiste = int(idPiste)
    except ValueError:
        return "L'identifiant de la piste doit être un nombre."
    try:
        idArbitre = int(idArbitre)
    except ValueError:
        return "L'identifiant de l'arbitre doit être un nombre."
    try:
        idTireur1 = int(idTireur1)
        idTireur2 = int(idTireur2)
    except ValueError:
        return "L'identifiant des tireurs doivent être un nombre."
    try:
        toucheRecuTireur1 = int(toucheRecuTireur1)
        toucheDonnerTireur1 = int(toucheDonnerTireur1)
        toucheRecuTireur2 = int(toucheRecuTireur2)
        toucheDonnerTireur2 = int(toucheDonnerTireur2)
    except ValueError:
        return "Le nombre de touches doit être un nombre."
    try:
        dateMatch = datetime.strptime(dateMatch, "%Y-%m-%d").date()
        heureMatch = datetime.strptime(heureMatch, "%H:%M").time()
    except ValueError:
        return "La date et l'heure doivent être au format valide (jour/mois/année)"
    try:
        # Ajoutez le match poule à la base de données
        match_poule = MatchPoule(type_match = idTypeMatch, poule = idPoule, piste = idPiste, arbitre = idArbitre, tireur1 = idTireur1, tireur2 = idTireur2, date_match = dateMatch, heure_match = heureMatch, touche_recu_tireur1 = toucheRecuTireur1, touche_donner_tireur1 = toucheDonnerTireur1, touche_recu_tireur2 = toucheRecuTireur2, touche_donner_tireur2 = toucheDonnerTireur2)
        match_poule_existe = MatchPoule.query.filter_by(type_match=idTypeMatch, poule=idPoule, piste=idPiste, arbitre=idArbitre, tireur1=idTireur1, tireur2=idTireur2).first()
        if not match_poule_existe:
            db.session.add(match_poule)
        else :
            return f"Le match poule {idTypeMatch} existe déjà."
        db.session.commit()  # Validez la transaction
        return f"Le match poule {idTypeMatch} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (numéro de licence déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le match poule {idTypeMatch} existe déjà."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produitematch poule : {str(e)}"