import click
from .app import app,db
from .ajout_bd import *
from .models import *
from hashlib import sha256
import os
import csv

@app.cli.command()
@click.argument('filename')
def loaddb(dirname):
    '''Creates the tables and populates them with data.'''
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
            categorie = infos_arme_sex_cat[3]
            try:
                with open(chemin_fichier, 'r', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        infos = row.split(";")
                        nom = infos[0]
                        prenom = infos[1]
                        date_naissance = infos[2]
                        num_license = infos[3]
                        region = infos[5]
                        club = infos[6]
                        points = infos[7]
                        print(ajouter_arme(arme))
                        print(ajouter_categorie(categorie))
                        print(ajouter_club(club, region))
                print(f"Les données du fichier {nom_fichier} ont été ajoutées à la base de données.")

            except Exception as e:
                print(f"Erreur lors du traitement du fichier {nom_fichier}: {e}")
                db.session.rollback()

@app.cli.command ()
@click.argument("username")
@click.argument("password")
def newuser(username , password ):
    '''Adds a new user.'''
    m = sha256()
    m.update(password.encode())
    u = User(pseudoUser=username , mdpUser=m.hexdigest())
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