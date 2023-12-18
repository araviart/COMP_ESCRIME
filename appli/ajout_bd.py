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
        db.session.add(arme)
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
        db.session.add(categorie)
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
        db.session.add(club)
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
        # Ajoutez l'escrimeur à la base de données
        pratiquer = PratiquerArme(id_arme, numLicense)
        
        # Utilisez session.add_all pour ajouter les objets en une seule fois
        db.session.add(pratiquer)
        db.session.commit()
        
        return f"L'escrimeur {numLicense} pratique l'arme {arme}."
    
    except IntegrityError:
        db.session.rollback()
        return "L'escrimeur pratique déjà l'arme."
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'arme {arme} pratiquée par {numLicense} : {str(e)}"

def creer_competition(nomLieu,adresseLieu,villeLieu,cpLieu, nomSaison, nomCat, nomArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle):
    try:
        if nomLieu and adresseLieu and villeLieu and cpLieu:  # Vérifiez si tous les champs cachés sont fournis
            lieu = Lieu.query.filter_by(nomLieu=nomLieu).first()
            if lieu is None:
                lieu = Lieu(nom_lieu=nomLieu, adresse_lieu=adresseLieu, ville_lieu=villeLieu, code_postal_lieu=cpLieu)
                db.session.add(lieu)
            else:
                # Si le lieu existe déjà, mais que vous souhaitez mettre à jour les informations
                lieu.adresse_lieu = adresseLieu
                lieu.ville_lieu = villeLieu
                lieu.code_postal_lieu = cpLieu
            db.session.commit()
        # Obtenez les objets à partir des noms
        saison = Saison.query.filter_by(nomSaison=nomSaison).first()
        categorie = Categorie.query.filter_by(nomCategorie=nomCat).first()
        arme = Arme.query.filter_by(nomArme=nomArme).first()

        print(lieu, saison, categorie, arme)

        # Vérifiez que les objets sont valides
        if not all([lieu, saison, categorie, arme]):
            return "Erreur : Un ou plusieurs éléments nécessaires sont introuvables."

        # Convertissez la date et l'heure
        date_comp = datetime.strptime(dateComp, "%Y-%m-%d").date()
        heure_comp = datetime.strptime(heureComp, "%H:%M").time()

        # Créez la compétition
        competition = Competition(
            lieu, saison, categorie, arme, nomComp, descComp, date_comp, heure_comp, sexeComp, estIndividuelle
        )
        db.session.add(competition)
        db.session.commit()

        return f"La compétition {nomComp} a été créée avec succès."
    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de la création de la compétition {nomComp}: {e}"
    
    except IntegrityError:
        db.session.rollback()
        return "Une compétition avec ce nom existe déjà."
    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de la création de la compétition {nomComp}: {str(e)}"