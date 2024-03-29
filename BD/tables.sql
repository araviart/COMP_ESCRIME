--CREATE DATABASE IF NOT EXISTS `coupe_escrime` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
--USE coupe_escrime;

CREATE OR REPLACE TABLE USER(
    idUser INT NOT NULL AUTO_INCREMENT,
    pseudoUser VARCHAR(99) NOT NULL UNIQUE,
    mdpUser VARCHAR(9999) NOT NULL,
    emailUser VARCHAR(99) UNIQUE,
    statutUser VARCHAR(99) NOT NULL,
    PRIMARY KEY(idUser)
);

CREATE OR REPLACE TABLE LIEU(
    idLieu INT NOT NULL AUTO_INCREMENT,
    nomLieu VARCHAR(50) NOT NULL,
    villeLieu VARCHAR(50) NOT NULL,
    codePostalLieu INT(5) NOT NULL,
    adresseLieu VARCHAR(50) NOT NULL,
    PRIMARY KEY(idLieu)
);

--CREATE OR REPLACE TABLE ARME(
--    idArme INT NOT NULL AUTO_INCREMENT,
--    nomArme VARCHAR(50) NOT NULL,
--    PRIMARY KEY(idArme)
--);

CREATE OR REPLACE TABLE SAISON(
    idSaison INT NOT NULL AUTO_INCREMENT,
    nomSaison VARCHAR(50) NOT NULL,
    dateDebutSaison DATE NOT NULL,
    dateFinSaison DATE NOT NULL,
    PRIMARY KEY(idSaison)
);

--CREATE OR REPLACE TABLE CATEGORIE(
--    idCat INT NOT NULL AUTO_INCREMENT,
--    nomCategorie VARCHAR(50) NOT NULL,
--    PRIMARY KEY(idCat)
--);

--CREATE OR REPLACE TABLE CLUB(
--    idClub INT NOT NULL AUTO_INCREMENT,
--    nomClub VARCHAR(50) NOT NULL,
--    villeClub VARCHAR(50) NOT NULL,
--    PRIMARY KEY(idClub)
--);

CREATE OR REPLACE TABLE COMPETITION(
    idComp INT NOT NULL AUTO_INCREMENT,
    idLieu INT NOT NULL,
    idSaison INT NOT NULL,
    idCat INT NOT NULL,
    idArme INT NOT NULL,
    nomComp VARCHAR(50) NOT NULL,
    descComp VARCHAR(50) NOT NULL,
    dateComp DATE NOT NULL,
    heureComp TIME NOT NULL,
    sexeComp VARCHAR(1) NOT NULL,
    estIndividuelle BOOLEAN NOT NULL,
    PRIMARY KEY(idComp),
    FOREIGN KEY (idLieu) REFERENCES LIEU(idLieu),
    FOREIGN KEY (idSaison) REFERENCES SAISON(idSaison),
    FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat),
    FOREIGN KEY (idArme) REFERENCES ARME(idArme)
);

CREATE OR REPLACE TABLE PISTE(
    idPiste INT NOT NULL AUTO_INCREMENT,
    idComp INT NOT NULL,
    nomPiste VARCHAR(50) NOT NULL,
    estDispo BOOLEAN NOT NULL,
    PRIMARY KEY(idPiste),
    FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp)
);

CREATE OR REPLACE TABLE TYPE_MATCH(
    idTypeMatch INT NOT NULL AUTO_INCREMENT,
    nomTypeMatch VARCHAR(50) NOT NULL,
    nbTouches INT NOT NULL,
    PRIMARY KEY(idTypeMatch)
);

--CREATE OR REPLACE TABLE ESCRIMEUR(
--    idCat INT NOT NULL,
--    prenomE VARCHAR(50) NOT NULL,
--    nomE VARCHAR(50) NOT NULL,
--    dateNaissanceE DATE NOT NULL,
--    numeroLicenceE INT NOT NULL,
--    sexeE VARCHAR(50) NOT NULL,
--    numTelE VARCHAR (10),
--    PRIMARY KEY (numeroLicenceE),
--    FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat)
--);

CREATE OR REPLACE TABLE TIREUR(
    idTireur INT NOT NULL AUTO_INCREMENT,
    numeroLicenceE INT NOT NULL UNIQUE,
    idClub INT NOT NULL,
    classement INT NOT NULL,
    PRIMARY KEY(idTireur),
    FOREIGN KEY (numeroLicenceE) REFERENCES ESCRIMEUR(numeroLicenceE),
    FOREIGN KEY (idClub) REFERENCES CLUB(idClub)
);

CREATE OR REPLACE TABLE ARBITRE(
    idArbitre INT NOT NULL AUTO_INCREMENT,
    numeroLicenceE INT NOT NULL UNIQUE,
    PRIMARY KEY(idArbitre),
    FOREIGN KEY (numeroLicenceE) REFERENCES ESCRIMEUR(numeroLicenceE)
);

CREATE OR REPLACE TABLE PARTICIPANTS_COMPETITION(
    idTireur INT NOT NULL,
    idComp INT NOT NULL,
    PRIMARY KEY(idTireur,idComp),
    FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp),
    FOREIGN KEY (idTireur) REFERENCES TIREUR(idTireur)
);

--CREATE OR REPLACE TABLE PRATIQUER_ARME(
--    numeroLicenceE INT NOT NULL,
--    idArme INT NOT NULL,
--    PRIMARY KEY(numeroLicenceE, idArme),
--    FOREIGN KEY (numeroLicenceE) REFERENCES ESCRIMEUR(numeroLicenceE),
--    FOREIGN KEY (idArme) REFERENCES ARME(idArme)
--);

CREATE OR REPLACE TABLE CLASSEMENT(
    idComp INT NOT NULL,
    idTireur INT NOT NULL,
    position INT,
    PRIMARY KEY(idComp, numeroLicenceE),
    FOREIGN KEY (idComp) REFERENCES COMPETITION(idComp),
    FOREIGN KEY (numeroLicenceE) REFERENCES TIREUR(numeroLicenceE)
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

CREATE OR REPLACE TABLE PARTICIPANTS_POULE(
    idPoule INT NOT NULL,
    idTireur INT NOT NULL,
    PRIMARY KEY(idPoule, idTireur),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule),
    FOREIGN KEY (idTireur) REFERENCES TIREUR(idTireur)
);


CREATE OR REPLACE TABLE MATCH(
    idMatch INT NOT NULL AUTO_INCREMENT,
    idTypeMatch INT NOT NULL,
    idPoule INT NOT NULL,
    idPiste INT NOT NULL,
    idArbitre INT NOT NULL,
    GAGNANT INT,
    idTireur1 INT NOT NULL,
    idTireur2 INT NOT NULL,
    dateMatch DATE NOT NULL,
    heureMatch TIME NOT NULL,
    touchesRecuesTireur1 INT,
    touchesDonneesTireur1 INT,
    touchesRecuesTireur2 INT,
    touchesDonneesTireur2 INT,
    PRIMARY KEY(idMatch),
    FOREIGN KEY (idTireur1) REFERENCES TIREUR(numeroLicenceE),
    FOREIGN KEY (idTireur2) REFERENCES TIREUR(numeroLicenceE),
    FOREIGN KEY(gagnant) REFERENCES TIREUR(numeroLicenceE),
    FOREIGN KEY (idPiste) REFERENCES PISTE(idPiste),
    FOREIGN KEY (idTypeMatch) REFERENCES TYPE_MATCH(idTypeMatch),
    FOREIGN KEY (idArbitre) REFERENCES POULE(idArbitre)
);


CREATE OR REPLACE TABLE CONTENIR(
    idMatch INT NOT NULL,
    idPoule INT NOT NULL,
    PRIMARY KEY(idMatch, idPoule),
    FOREIGN KEY (idMatch) REFERENCES MATCH(idMatch),
    FOREIGN KEY (idPoule) REFERENCES POULE(idPoule)
);