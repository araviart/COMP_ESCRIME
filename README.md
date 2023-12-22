# Application de Gestion de Compétition d'Escrime

Projet proposé par le Cercle d’Escrime de Blois

## But de l’application :

L'objectif de cette application est de gérer le déroulement d'une compétition d'escrime en assurant le suivi complet du processus. Les principales fonctionnalités incluent :

- Définition de la compétition.
- Inscription des tireurs et des arbitres.
- Répartition automatique des compétiteurs en poules selon les règles de la fédération.
- Gestion des phases d'élimination directe.
- Édition des feuilles de match pour les arbitres.
- Établissement d'un classement provisoire et final.
- Affichage des classements et de l'arbre du tableau d'élimination sur grand écran.
- Intégration des escrimeurs dans une base de données régionale.
- Archivage des compétitions et mise à jour des classements des compétiteurs.

## Participants :

Les membres impliqués dans ce projet sont :

- <u>**Raviart Alexandre**</u> (*Chef de projet*)
- Coursimault Irvin
- Masérati Amael
- Pigoreau Nathan 
- Toure Kris



## Chargement de la BD

Pour charger la base de données, si l'environnement flask est dans le dossier COMP_ESCRIME, il suffit de taper la commande : 

```bash
flask laoddb appli/data
```

Ensuite, pour créer un compte administrateur, il faut taper la commande :

```bash
flask newuser username password mail
```

Faites attention à respecter la condition pour le mot de passe présente dans la page de connexion.