-- Table LIEU
INSERT INTO LIEU (nomLieu, villeLieu, codePostalLieu, adresseLieu)
VALUES
    ('SalleBlois', 'Blois', '41000', '25 Rue Lucien Joubert');

-- Table ARME
INSERT INTO ARME (nomArme)
VALUES
    ('Épée'),
    ('Fleuret'),
    ('Sabre');

-- Table SAISON
INSERT INTO SAISON (nomSaison, dateDebutSaison, dateFinSaison)
VALUES
    ('Saison 2023', '2023-01-01', '2023-12-31'),
    ('Saison 2024', '2024-01-01', '2024-12-31');

-- Table CATEGORIE
INSERT INTO CATEGORIE (nomCategorie)
VALUES
    ('U13'),
    ('U15'),
    ('U17'),
    ('U20'),
    ('Senior'),
    ('V1'),
    ('V2'),
    ('V3'),
    ('V4');

-- Table CLUB
INSERT INTO CLUB (nomClub, villeClub)
VALUES
    ('Club Blois', 'Blois');

-- Table TYPE_MATCH
INSERT INTO TYPE_MATCH (nomTypeMatch, nbTouches)
VALUES
    ('Match Poule', 5),
    ('Match Elimination', 15);

-- Table COMPETITION

-- Table PISTE

-- Table ESCRIMEUR

-- Table TIREUR

-- Table ARBITRE

-- Table PRATIQUER_ARME

-- Table CLASSEMENT_FINAL

-- Table POULE

-- Table PARTICIPANTS_POULE

-- Table MATCH_POULE

-- Table FEUILLE_MATCH

