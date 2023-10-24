CREATE OR REPLACE TABLE LIEU(
    idLieu INT NOT NULL AUTO_INCREMENT,
    nomLieu VARCHAR(50) NOT NULL,
    villeLieu VARCHAR(50) NOT NULL,
    codePostalLieu VARCHAR(50) NOT NULL,
    adresseLieu VARCHAR(50) NOT NULL,
    PRIMARY KEY(idLieu)
);

CREATE OR REPLACE TABLE ARME(
    idArme INT NOT NULL AUTO_INCREMENT,
    nomArme VARCHAR(50) NOT NULL,
    PRIMARY KEY(idArme)
);

CREATE OR REPLACE TABLE SAISON(
    idSaison INT NOT NULL AUTO_INCREMENT,
    nomSaison VARCHAR(50) NOT NULL,
    dateDebutSaison DATE NOT NULL,
    dateFinSaison DATE NOT NULL,
    PRIMARY KEY(idSaison)
);

CREATE OR REPLACE TABLE CATEGORIE(
    idCat INT NOT NULL AUTO_INCREMENT,
    nomCategorie VARCHAR(50) NOT NULL,
    PRIMARY KEY(idCat)
);

CREATE OR REPLACE TABLE CLUB(
    idClub INT NOT NULL AUTO_INCREMENT,
    nomClub VARCHAR(50) NOT NULL,
    villeClub VARCHAR(50) NOT NULL,
    PRIMARY KEY(idClub)
);

CREATE OR REPLACE TABLE PISTE(
    idPiste INT NOT NULL AUTO_INCREMENT,
    nomPiste VARCHAR(50) NOT NULL,
    estDispo BOOLEAN NOT NULL,
    PRIMARY KEY(idPiste)
);

CREATE OR REPLACE TABLE CLASSEMENT_FINAL(
    idClassementFinal INT NOT NULL AUTO_INCREMENT,
    idComp INT NOT NULL,
    nomClassementFinal VARCHAR(1) NOT NULL,
    PRIMARY KEY(idClassementFinal)
);

CREATE OR REPLACE TABLE TYPE_MATCH(
    idTypeMatch INT NOT NULL AUTO_INCREMENT,
    nomTypeMatch VARCHAR(50) NOT NULL,
    nbTouches INT NOT NULL,
    PRIMARY KEY(idTypeMatch)
);

CREATE OR REPLACE TABLE COMPETITION(
    idComp INT NOT NULL AUTO_INCREMENT,
    idLieu INT NOT NULL,
    idSaison INT NOT NULL,
    idCat INT NOT NULL,
    idClassementFinal INT NOT NULL,
    idArme INT NOT NULL,
    nomComp VARCHAR(50) NOT NULL,
    defComp VARCHAR(50) NOT NULL,
    dateComp DATE NOT NULL,
    PRIMARY KEY(idComp),
    FOREIGN KEY (idLieu) REFERENCES LIEU(idLieu),
    FOREIGN KEY (idSaison) REFERENCES SAISON(idSaison),
    FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat),
    FOREIGN KEY (idClassementFinal) REFERENCES CLASSEMENT_FINAL(idClassementFinal),
    FOREIGN KEY (idArme) REFERENCES ARME(idArme)
);

ALTER TABLE CLASSEMENT_FINAL ADD FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp);

CREATE OR REPLACE TABLE ESCRIMEUR(
    idEscrimeur INT NOT NULL AUTO_INCREMENT,
    idCat INT NOT NULL,
    prenomEscrimeur VARCHAR(50) NOT NULL,
    nomEscrimeur VARCHAR(50) NOT NULL,
    dateDeNaissanceEscrimeur DATE NOT NULL,
    numeroLicenceEscrimeur INT NOT NULL,
    sexeEscrimeur VARCHAR(50) NOT NULL,
    PRIMARY KEY (idEscrimeur),
    FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat)
);

CREATE OR REPLACE TABLE TIREUR(
    idTireur INT NOT NULL,
    idClub INT NOT NULL,
    classement INT NOT NULL,
    FOREIGN KEY (idTireur) REFERENCES ESCRIMEUR(idEscrimeur),
    FOREIGN KEY (idClub) REFERENCES CLUB(idClub)
);

CREATE OR REPLACE TABLE ARBITRE(
    idArbitre INT NOT NULL,
    FOREIGN KEY (idArbitre) REFERENCES ESCRIMEUR(idEscrimeur)
);

CREATE OR REPLACE TABLE POULE(
    idPoule INT NOT NULL AUTO_INCREMENT,
    idComp INT NOT NULL,
    idPiste INT NOT NULL,
    idArbitre INT NOT NULL,
    nomPoule VARCHAR(50) NOT NULL,
    PRIMARY KEY(idPoule),
    FOREIGN KEY (idPiste) REFERENCES PISTE(idPiste),
    FOREIGN KEY (idArbitre) REFERENCES ARBITRE(idArbitre),
    FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp)
);

CREATE OR REPLACE TABLE PARTICIPANTS_POULE(
    idPoule INT NOT NULL,
    idTireur INT NOT NULL,
    PRIMARY KEY(idPoule, idTireur),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule),
    FOREIGN KEY (idTireur) REFERENCES TIREUR(idTireur)
);

CREATE OR REPLACE TABLE MATCH_POULE(
    idMatch INT NOT NULL AUTO_INCREMENT,
    idTypeMatch INT NOT NULL,
    idPoule INT NOT NULL,
    idPiste INT NOT NULL,
    idArbitre INT NOT NULL,
    idTireur1 INT NOT NULL,
    idTireur2 INT NOT NULL,
    dateMatch DATE NOT NULL,
    heureMatch TIME NOT NULL,
    touchesRecuesTireur1 INT NOT NULL,
    touchesDonneesTireur1 INT NOT NULL,
    touchesRecuesTireur2 INT NOT NULL,
    touchesDonneesTireur2 INT NOT NULL,
    PRIMARY KEY(idMatch),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule),
    FOREIGN KEY (idPiste) REFERENCES PISTE(idPiste),
    FOREIGN KEY (idTypeMatch) REFERENCES TYPE_MATCH(idTypeMatch),
    FOREIGN KEY (idArbitre) REFERENCES POULE(idArbitre),
    FOREIGN KEY (idTireur1) REFERENCES TIREUR(idTireur),
    FOREIGN KEY (idTireur2) REFERENCES TIREUR(idTireur)
);

CREATE OR REPLACE TABLE FEUILLE_MATCH(
    idFeuille INT NOT NULL AUTO_INCREMENT,
    idPoule INT NOT NULL,
    idComp INT NOT NULL,
    idTireur1 INT NOT NULL,
    idTireur2 INT NOT NULL,
    scoreTireur1 INT NOT NULL,
    scoreTireur2 INT NOT NULL,
    PRIMARY KEY(idFeuille),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule),
    FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp),
    FOREIGN KEY (idTireur1) REFERENCES TIREUR(idTireur),
    FOREIGN KEY (idTireur2) REFERENCES TIREUR(idTireur)
);