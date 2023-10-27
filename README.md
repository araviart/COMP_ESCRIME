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

## Détails Techniques :

L'application prend en compte 6 armes (fleuret homme, fleuret femme, épée homme, épée femme, sabre homme et sabre femme) et 9 catégories (U13, U15, U17, U20, senior, V1, V2, V3, V4). Les règles des matchs varient en fonction des phases de la compétition, avec des critères de classement spécifiques.

## Diagramme de Cas d'Utilisation :

![Diagramme de Cas d'Utilisation](lien)

**Escrimeur :**
- *Description :* Les escrimeurs ont les permissions de base sur la plateforme. Ils peuvent simplement se connecter, consulter les compétitions à venir et gérer leur propre compte.

**Membre du Staff :**
- *Description :* Les membres du staff ont des privilèges étendus par rapport aux escrimeurs. Ils peuvent effectuer toutes les actions d'un utilisateur standard. De plus, ils ont le pouvoir d'inscrire de nouveaux adhérents au club, ce qui implique d'entrer les informations détaillées sur les escrimeurs.

**Organisateur :**
- *Description :* Les organisateurs ont le plus haut niveau d'accès sur la plateforme. Ils peuvent effectuer toutes les tâches d'un membre du staff. En outre, ils peuvent définir des compétitions, gérer les inscriptions des escrimeurs (ajout et suppression), organiser les poules à l'aide d'un service automatique, choisir les arbitres, établir des classements (provisoires et finaux, avec la possibilité de clôturer la compétition), éditer les détails de la compétition, supprimer des compétitions, afficher des informations de compétition, faire l'appel, entrer les scores, annuler des compétitions et consulter et modifier les informations des adhérents du club.

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