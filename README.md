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
- Toure Chris

## Détails Techniques :

L'application prend en compte 6 armes (fleuret homme, fleuret femme, épée homme, épée femme, sabre homme et sabre femme) et 9 catégories (U13, U15, U17, U20, senior, V1, V2, V3, V4). Les règles des matchs varient en fonction des phases de la compétition, avec des critères de classement spécifiques.

## Diagramme de Cas d'Utilisation :

![Diagramme de Cas d'Utilisation](lien)

Ce diagramme représente les fonctionnalités incluses dans notre application.

## Modèle Conceptuel de Données (MCD) :

![Modèle Conceptuel de Données](lien)

Voici les différentes contraintes de notre base de données :

### Table : Compétition
- **Contraintes :**
  - **Clé primaire :** Nom de la compétition (unique).
  - Doit avoir une arme, une catégorie, un lieu, une date et une saison spécifiés.

### Table : Escrimeur
- **Contraintes :**
  - **Clé primaire :** Numéro de licence (unique).
  - Peut pratiquer plusieurs armes.
  - Peut participer à une compétition d'une catégorie supérieure.
  - Doit être affilié à un club.
  - A un classement qui peut être "NC" (s'il n'a jamais participé à une compétition).

### Table : Arbitre
- **Contraintes :**
  - **Clé primaire :** Numéro de licence (unique).
  - Est un escrimeur, mais ne participe pas en tant que tireur.

### Table : Feuille_de_Match_Poule
- **Contraintes :**
  - **Clé primaire :** Identifiant unique de la feuille de match.
  - Contient des informations sur tous les matchs d'une poule.
  - Les matchs se jouent en 5 touches.
  - Doit avoir un lien avec la compétition à laquelle elle appartient.

### Table : Match_Elimination
- **Contraintes :**
  - **Clé primaire :** Identifiant unique du match d'élimination.
  - Les matchs d'élimination se jouent en 15 touches.
  - Doit avoir un lien avec la compétition à laquelle il appartient.


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