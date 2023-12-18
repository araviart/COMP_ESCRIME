import click
from .app import app,db
from .ajout_bd import *
from .models import *
from hashlib import sha256
import os
import csv

@app.cli.command()
@click.argument('dirname')
def loaddb(dirname):
    '''Creates the tables and populates them with data.'''
    db.drop_all()
    # Create tables 
    db.create_all()

    # Parcours de tous les fichiers du dossier
    for nom_fichier in os.listdir(dirname):
        chemin_fichier = os.path.join(dirname, nom_fichier)
        if os.path.isfile(chemin_fichier) and nom_fichier.endswith('.csv'):
            print(f"Traitement du fichier CSV {nom_fichier} :")
            fichier_sans_extention = os.path.splitext(nom_fichier)[0]
            infos_arme_sex_cat = fichier_sans_extention.split("_")
            arme = infos_arme_sex_cat[1]
            sex = infos_arme_sex_cat[2]
            nom_categorie = infos_arme_sex_cat[3]
            print(ajouter_arme(arme))
            print(ajouter_categorie(nom_categorie))
            try:
                with open(chemin_fichier, 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        nom = row['nom']
                        prenom = row['prenom']
                        date_naissance = row['date naissance']
                        num_license = row['adherent']
                        region = row['comite regional']
                        club = row['club']
                        points = row['points']
                        print(ajouter_club(club, region))
                        print(ajouter_escrimeur(nom_categorie, prenom, nom, date_naissance, num_license, sex, None))
                        print(ajouter_tireur(num_license, club, points))
                        print(pratiquer_arme(num_license, arme))
                print(f"Les données du fichier {nom_fichier} ont été ajoutées à la base de données.")

            except Exception as e:
                print(f"Erreur lors du traitement du fichier {nom_fichier}: {e}")
                db.session.rollback()

@app.cli.command ()
@click.argument("username")
@click.argument("password")
@click.argument("email")
def newuser(username , password, email):
    '''Adds a new user.'''
    m = sha256()
    m.update(password.encode())
    u = User(pseudoUser=username , mdpUser=m.hexdigest(), emailUser=email)
    db.session.add(u)
    db.session.commit()

@app.cli.command()
@click.argument("username")
@click.argument("password")
def passwd(username, password):
    """Changes the password of a user. """
    m = sha256()
    m.update(password.encode())
    u = User.query.get(username)
    u.mdpUser = m.hexdigest()
    db.session.commit()
    
        
@app.cli.command()
@click.argument("nom_lieu")
@click.argument("saison")
@click.argument("categorie")
@click.argument("arme")
@click.argument("nom_competition")
@click.argument("desc_competition")
@click.argument("date_competition")
@click.argument("heure_competition")
@click.argument("sexe_competition")
@click.argument("est_individuelle")
def add_competition(nom_lieu, saison, categorie, arme, nom_competition, desc_competition, date_competition, heure_competition, sexe_competition, est_individuelle):
    try:
        id_lieu = get_id_lieu(nom_lieu)
        id_saison = get_id_saison(saison)
        id_categorie = get_id_categorie(categorie)
        id_arme = get_id_arme(arme)
        est_individuelle = est_individuelle.lower() == 'true'

        print(f"Avant la création de l'objet Competition - idCat: {id_categorie}")

        nouvelle_comp = Competition(id_lieu, id_saison, id_categorie, id_arme, nom_competition, desc_competition, date_competition, heure_competition, sexe_competition, est_individuelle)

        print(f"Avant l'ajout à la base de données - idCat: {id_categorie}")

        print(db.session.query(Competition).filter_by(idCat=id_categorie).statement)
        db.session.add(nouvelle_comp)
        db.session.commit()
        print("La compétition a été ajoutée avec succès.")

    except IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")
        db.session.rollback()
        return "Une compétition avec ce nom existe déjà."

    except Exception as e:
        print(id_categorie)
        print(f"Erreur lors de l'ajout de la compétition : {e}")
        db.session.rollback()
