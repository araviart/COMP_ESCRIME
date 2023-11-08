from .models import *
from .app import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError

def ajouter_arme(nom_arme):
    if not nom_arme.strip():
        return "Le nom de l'arme ne peut pas être vide ou ne contenir que des espaces."

    try:
        # Commencez la transaction
        db.session.begin()

        # Ajoutez l'arme à la base de données
        arme = Arme(nomArme=nom_arme)
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
        return f"Une erreur s'est produite lors de l'ajout de l'arme : {str(e)}"


def ajouter_categorie(nom_categorie):
    if not nom_categorie.strip():
        return "Le nom de la catégorie ne peut pas être vide ou ne contenir que des espaces."

    try:
        # Commencez la transaction
        db.session.begin()

        # Ajoutez la catégorie à la base de données
        categorie = Categorie(nomCategorie=nom_categorie)
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
        return f"Une erreur s'est produite lors de l'ajout de la catégorie : {str(e)}"


def ajouter_club(nom, region):
    if not nom.strip() or not region.strip():
        return "Le nom et la région du club ne peuvent pas être vides ou ne contenir que des espaces."

    try:
        # Commencez la transaction
        db.session.begin()

        # Ajoutez le club à la base de données
        club = Club(nomClub=nom, regionClub=region)
        db.session.add(club)
        db.session.commit()  # Validez la transaction

        return f"Le club {nom} a été ajouté avec succès."
    except IntegrityError:
        # En cas d'erreur d'intégrité (nom du club déjà pris), annulez la transaction
        db.session.rollback()
        return f"Le nom du club {nom} est déjà pris."
    except Exception as e:
        # En cas d'autres erreurs, annulez la transaction
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout du club : {str(e)}"

    
def get_id_categorie(nom_cat):
    categorie = Categorie.query.filter_by(nomCategorie=nom_cat).first()
    if categorie:
        return categorie.idCategorie
    else:
        return "La catégorie n'existe pas."

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
    if id_categorie is None:
        return "La catégorie n'existe pas."
    
    try:
        db.session.begin()
        
        # Ajoutez l'escrimeur à la base de données
        escrimeur = Escrimeur(categorie=id_categorie, prenomE=prenom, nomE=nom,
                              dateNaissanceE=date_naissance, numeroLicenceE=numLicense,
                              sexeE=sex, numTelE=numTel)
        
        # Utilisez session.add_all pour ajouter les objets en une seule fois
        db.session.add_all([escrimeur])
        db.session.commit()
        
        return f"L'escrimeur {prenom} {nom} a été ajouté avec succès."
    
    except IntegrityError:
        db.session.rollback()
        return "L'escrimeur existe déjà dans la base de données."
    
    except Exception as e:
        db.session.rollback()
        return f"Une erreur s'est produite lors de l'ajout de l'escrimeur : {str(e)}"