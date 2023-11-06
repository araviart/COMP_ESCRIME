import csv
from .app import db
from models import *

colonnes_lieu = ['nomLieu', 'adresseLieu', 'villeLieu', 'codePostalLieu']
colonnes_arme = ['nomArme']
colonnes_saison = ['nomSaison', 'dateDebutSaison', 'dateFinSaison']
colonnes_categorie = ['nomCategorie']
colonnes_club = ['idClub', 'nomClub', 'villeClub']
colonnes_type_match = ['nomTypeMatch', 'nbTouches']
colonnes_competition = ['idLieu', 'idSaison', 'idArme', 'idCat', 'nomComp', 'descComp', 'dateComp', 'heureComp', 'sexeComp', 'estIndividuelle']
colonnes_piste = ['idComp', 'nomPiste', 'estDispo']
colonnes_escrimeur = ['idCat', 'prenomE', 'nomE', 'dateNaissanceE', 'numeroLicenceE', 'sexeE', 'numTelE']
colonnes_escrimeur_arme = ['idEscrimeur', 'idArme']
colonnes_pratiquer_arme = ['idEscrimeur', 'idArme']
colonnes_classement_final = ['idComp', 'idTireur', 'position']
colonnes_poule = ['idComp', 'idPiste', 'idArbitre', 'nomPoule']
colonnes_participant_poule = ['idPoule', 'idTireur']
colonnes_match_poule = ['idTypeMatch','idPoule','idPiste','idArbitre','idTireur1','idTireur2','dateMatch','heureMatch','touchesRecuesTireur1','touchesDonneesTireur1','touchesRecuesTireur2','touchesDonneesTireur2']
colonnes_feuille_match = ['idPoule','idComp','idTireur1','idTireur2','scoreTireur1','scoreTireur2']

# Ouvrir le fichier CSV en mode lecture
with open('chemin/vers/votre/fichier.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Traiter la table 'lieu'
        if all(colonne in row for colonne in colonnes_lieu):
            nouveau_lieu = Lieu(nomLieu=row['nomLieu'], adresseLieu=row['adresseLieu'],
                                villeLieu=row['villeLieu'], codePostalLieu=row['codePostalLieu'])
            db.session.add(nouveau_lieu)
        # Traiter la table 'arme'
        elif all(colonne in row for colonne in colonnes_arme):
            nouvelle_arme = Arme(nomArme=row['nomArme'])
            db.session.add(nouvelle_arme)
        # Traiter la table 'saison'
        elif all(colonne in row for colonne in colonnes_saison):
            nouvelle_saison = Saison(nomSaison=row['nomSaison'], dateDebutSaison=row['dateDebutSaison'],
                                     dateFinSaison=row['dateFinSaison'])
            db.session.add(nouvelle_saison)
        # Traiter la table 'categorie'
        elif all(colonne in row for colonne in colonnes_categorie):
            nouvelle_categorie = Categorie(nomCategorie=row['nomCategorie'])
            db.session.add(nouvelle_categorie)
        # Traiter la table 'club'
        elif all(colonne in row for colonne in colonnes_club):
            nouveau_club = Club(idClub=row['idClub'], nomClub=row['nomClub'], villeClub=row['villeClub'])
            db.session.add(nouveau_club)
        # Traiter la table 'type_match'
        elif all(colonne in row for colonne in colonnes_type_match):
            nouveau_type_match = TypeMatch(nomTypeMatch=row['nomTypeMatch'], nbTouches=row['nbTouches'])
            db.session.add(nouveau_type_match)
        # Traiter la table 'competition'
        elif all(colonne in row for colonne in colonnes_competition):
            nouvelle_competition = Competition(idLieu=row['idLieu'], idSaison=row['idSaison'], idArme=row['idArme'],
                                               idCat=row['idCat'], nomComp=row['nomComp'], descComp=row['descComp'],
                                               dateComp=row['dateComp'], heureComp=row['heureComp'],
                                               sexeComp=row['sexeComp'], estIndividuelle=row['estIndividuelle'])
            db.session.add(nouvelle_competition)
        # Traiter la table 'piste'
        elif all(colonne in row for colonne in colonnes_piste):
            nouvelle_piste = Piste(idComp=row['idComp'], nomPiste=row['nomPiste'], estDispo=row['estDispo'])
            db.session.add(nouvelle_piste)
        # Traiter la table 'escrimeur'
        elif all(colonne in row for colonne in colonnes_escrimeur):
            nouvel_escrimeur = Escrimeur(idCat=row['idCat'], prenomE=row['prenomE'], nomE=row['nomE'],
                                         dateNaissanceE=row['dateNaissanceE'], numeroLicenceE=row['numeroLicenceE'],
                                         sexeE=row['sexeE'], numTelE=row['numTelE'])
            db.session.add(nouvel_escrimeur)
        # Traiter la table 'escrimeur_arme'
        elif all(colonne in row for colonne in colonnes_escrimeur_arme):
            nouvel_escrimeur_arme = EscrimeurArme(idEscrimeur=row['idEscrimeur'], idArme=row['idArme'])
            db.session.add(nouvel_escrimeur_arme)
        # Traiter la table 'pratiquer_arme'
        elif all(colonne in row for colonne in colonnes_pratiquer_arme):
            nouvel_pratiquer_arme = PratiquerArme(idEscrimeur=row['idEscrimeur'], idArme=row['idArme'])
            db.session.add(nouvel_pratiquer_arme)
        # Traiter la table 'classement_final'
        elif all(colonne in raw for colonne in colonnes_classement_final):
            nouveau_classement_final = ClassementFinal(idComp=row['idComp'], idTireur=row['idTireur'], position=row['position'])
            db.session.add(nouveau_classement_final)
        # Traiter la table 'poule'
        elif all(colonne in row for colonne in colonnes_poule):
            nouvelle_poule = Poule(idComp=row['idComp'], idPiste=row['idPiste'], idArbitre=row['idArbitre'], nomPoule=row['nomPoule'])
            db.session.add(nouvelle_poule)
        # Traiter la table 'participant_poule
        elif all(colonne in row for colonne in colonnes_participant_poule):
            nouvel_participer_poule = ParticipantsPoule(idPoule=row['idPoule'], idTireur=row['idTireur'])
            db.session.add(nouvel_participer_poule)
        # Traiter la table 'match_poule'
        elif all(colonne in row for colonne in colonnes_match_poule):
            nouvel_match_poule = MatchPoule(idTypeMatch=row['idTypeMatch'], idPoule=row['idPoule'], idPiste=row['idPiste'], idArbitre=row['idArbitre'], idTireur1=row['idTireur1'], idTireur2=row['idTireur2'], dateMatch=row['dateMatch'], heureMatch=row['heureMatch'], touchesRecuesTireur1=row['touchesRecuesTireur1'], touchesDonneesTireur1=row['touchesDonneesTireur1'], touchesRecuesTireur2=row['touchesRecuesTireur2'], touchesDonneesTireur2=row['touchesDonneesTireur2'])
            db.session.add(nouvel_match_poule)
        # Traiter la table 'feuille_match'
        elif all(colonne in row for colonne in colonnes_feuille_match):
            nouvelle_feuille_match = FeuilleMatch(idPoule=row['idPoule'], idComp=row['idComp'], idTireur1=row['idTireur1'], idTireur2=row['idTireur2'], scoreTireur1=row['scoreTireur1'], scoreTireur2=row['scoreTireur2'])
            db.session.add(nouvelle_feuille_match)
        else:
            # Les donnée ne corresponde pas à une table de la base de donnée il y a donc un problème dans le csv
            print("Les données ne corresponde a aucune table de la base de donnée.")
        

# Valider la session pour ajouter les nouveaux objets à la base de données
db.session.commit()
