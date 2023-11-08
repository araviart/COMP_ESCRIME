-- Table USER
INSERT INTO USER (pseudoUser, mdpUser, emailUser)
VALUES
    ('irvyncsm', 'dc02c547057f94d418761ec354cea801bdd9741206e32a83500a3b476485192f', 'irvyncsm@gmail.com');

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
    ('Non rensigné', 'Non rensigné'),
    ('Club Orléans', 'Orléans'),
    ('Club Tours', 'Tours'),
    ('Club Blois', 'Blois');

-- Table TYPE_MATCH
INSERT INTO TYPE_MATCH (nomTypeMatch, nbTouches)
VALUES
    ('Match Poule', 5),
    ('Match Elimination', 15);

-- Table COMPETITION
INSERT INTO COMPETITION (idLieu, idSaison, idArme, idCat, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle)
VALUES
    (1, 2, 1, 1, 'Compétition Saison 2024 Épée U13 M', 'Description de la compétition', '2024-04-15', '09:00:00', 'H', TRUE),
    (1, 2, 1, 2, 'Compétition Saison 2024 Épée U15 M', 'Description de la compétition', '2024-04-16', '10:00:00', 'H', FALSE),
    (1, 2, 2, 1, 'Compétition Saison 2024 Fleuret U13 M', 'Description de la compétition', '2024-04-17', '11:00:00', 'M', TRUE),
    (1, 2, 2, 2, 'Compétition Saison 2024 Fleuret U15 M', 'Description de la compétition', '2024-04-18', '12:00:00', 'H', TRUE),
    (1, 2, 3, 1, 'Compétition Saison 2024 Sabre U13 M', 'Description de la compétition', '2024-04-19', '13:00:00', 'H', FALSE),
    (1, 2, 3, 2, 'Compétition Saison 2024 Sabre U15 M', 'Description de la compétition', '2024-04-20', '14:00:00', 'H', TRUE),
    
    (1, 2, 1, 1, 'Compétition Saison 2024 Épée U13 H', 'Description de la compétition', '2024-04-15', '09:00:00', 'H', FALSE),
    (1, 2, 1, 2, 'Compétition Saison 2024 Épée U15 H', 'Description de la compétition', '2024-04-16', '10:00:00', 'H', TRUE),
    (1, 2, 2, 1, 'Compétition Saison 2024 Fleuret U13 H', 'Description de la compétition', '2024-04-17', '11:00:00', 'H', TRUE),
    (1, 2, 2, 2, 'Compétition Saison 2024 Fleuret U15 H', 'Description de la compétition', '2024-04-18', '12:00:00', 'H', TRUE),
    (1, 2, 3, 1, 'Compétition Saison 2024 Sabre U13 H', 'Description de la compétition', '2024-04-19', '13:00:00', 'H', TRUE),
    (1, 2, 3, 2, 'Compétition Saison 2024 Sabre U15 H', 'Description de la compétition', '2024-04-20', '14:00:00', 'H', FALSE),

    (1, 2, 1, 1, 'Compétition Saison 2024 Épée U13 F', 'Description de la compétition', '2024-04-15', '09:00:00', 'F', TRUE),
    (1, 2, 1, 2, 'Compétition Saison 2024 Épée U15 F', 'Description de la compétition', '2024-04-16', '10:00:00', 'F', TRUE),
    (1, 2, 2, 1, 'Compétition Saison 2024 Fleuret U13 F', 'Description de la compétition', '2024-04-17', '11:00:00', 'F', FALSE),
    (1, 2, 2, 2, 'Compétition Saison 2024 Fleuret U15 F', 'Description de la compétition', '2024-04-18', '12:00:00', 'F', FALSE),
    (1, 2, 3, 1, 'Compétition Saison 2024 Sabre U13 F', 'Description de la compétition', '2024-04-19', '13:00:00', 'F', TRUE),
    (1, 2, 3, 2, 'Compétition Saison 2024 Sabre U15 F', 'Description de la compétition', '2024-04-20', '14:00:00', 'F', TRUE);

-- Table PISTE
INSERT INTO PISTE (idComp, nomPiste, estDispo)
VALUES
    (1, 'Piste 1', TRUE),
    (1, 'Piste 2', TRUE),
    (1, 'Piste 3', TRUE),
    (2, 'Piste 1', TRUE),
    (2, 'Piste 2', TRUE),
    (2, 'Piste 3', TRUE),
    (3, 'Piste 1', TRUE),
    (3, 'Piste 2', TRUE),
    (3, 'Piste 3', TRUE),
    (4, 'Piste 1', TRUE),
    (4, 'Piste 2', TRUE),
    (4, 'Piste 3', TRUE),
    (5, 'Piste 1', TRUE),
    (5, 'Piste 2', TRUE),
    (5, 'Piste 3', TRUE),
    (6, 'Piste 1', TRUE),
    (6, 'Piste 2', TRUE),
    (6, 'Piste 3', TRUE),
    (7, 'Piste 1', TRUE),
    (7, 'Piste 2', TRUE),
    (7, 'Piste 3', TRUE),
    (8, 'Piste 1', TRUE),
    (8, 'Piste 2', TRUE),
    (8, 'Piste 3', TRUE),
    (9, 'Piste 1', TRUE),
    (9, 'Piste 2', TRUE),
    (9, 'Piste 3', TRUE),
    (10, 'Piste 1', TRUE),
    (10, 'Piste 2', TRUE),
    (10, 'Piste 3', TRUE),
    (11, 'Piste 1', TRUE),
    (11, 'Piste 2', TRUE),
    (11, 'Piste 3', TRUE),
    (12, 'Piste 1', TRUE),
    (12, 'Piste 2', TRUE),
    (12, 'Piste 3', TRUE),
    (13, 'Piste 1', TRUE),
    (13, 'Piste 2', TRUE),
    (13, 'Piste 3', TRUE),
    (14, 'Piste 1', TRUE),
    (14, 'Piste 2', TRUE),
    (14, 'Piste 3', TRUE),
    (15, 'Piste 1', TRUE),
    (15, 'Piste 2', TRUE),
    (15, 'Piste 3', TRUE),
    (16, 'Piste 1', TRUE),
    (16, 'Piste 2', TRUE),
    (16, 'Piste 3', TRUE),
    (17, 'Piste 1', TRUE),
    (17, 'Piste 2', TRUE),
    (17, 'Piste 3', TRUE),
    (18, 'Piste 1', TRUE),
    (18, 'Piste 2', TRUE),
    (18, 'Piste 3', TRUE);

-- Table ESCRIMEUR
INSERT INTO ESCRIMEUR (idCat, prenomE, nomE, dateNaissanceE, numeroLicenceE, sexeE, numTelE)
VALUES

-- FLEURET DAMES U15
    (2, 'Adèle', 'ANDRIAMAMPIANINA', '2008-04-10', 133478, 'F', null),
    (2, 'Lise', 'CHOUET', '2009-08-11', 169221, 'F', null),
    (2, 'Mathilde', 'PRATS', '2008-03-09', 163749, 'F', null),
    (2, 'Joëlle', 'NEGRE', '2008-09-11', 116048, 'F', null),
    (2, 'Pauline', 'MAZILLE', '2009-02-09', 133493, 'F', null),
    (2, 'Helene Zhixuan', 'LI', '2010-06-16', 182444, 'F', null),
    (2, 'Lise', 'VALIERE', '2009-05-14', 138405, 'F', null),
    (2, 'Alexina', 'CHAIDAKIS', '2009-05-23', 190486, 'F', null),
    (2, 'Mia', 'LACKOVIC', '2008-10-27', 187370, 'F', null),
    (2, 'Victorine', 'DIRLAOUEN', '2009-09-07', 215767, 'F', null),

-- FLEURET DAMES U17
    (3, 'Keren', 'AYE', '2006-04-17', 135555, 'F', null),
    (3, 'Adele', 'ALIX', '2006-02-18', 109958, 'F', null),
    (3, 'Olivia', 'CAUVET', '2007-04-04', 65718, 'F', null),
    (3, 'Garance', 'MARTIN', '2006-05-03', 100420, 'F', null),
    (3, 'Chloe', 'RODARIE', '2006-10-18', 230041, 'F', null),
    (3, 'Mailys', 'DANSICARE', '2006-10-31', 67982, 'F', null),
    (3, 'Mathilde', 'PRATS', '2008-03-09', 163749, 'F', null),
    (3, 'Marion', 'RAFIN', '2007-01-04', 167483, 'F', null),
    (3, 'Adèle', 'ANDRIAMAMPIANINA', '2008-04-10', 133478, 'F', null),
    (3, 'Eloise', 'GOUTENEGRE', '2009-07-01', 191353, 'F', null),

-- FLEURET DAMES U20
    (4, 'Marion', 'ROUSSEAU', '2003-08-19', 85977, 'F', null),
    (4, 'Alicia', 'AUDIBERT', '2005-07-28', 106336, 'F', null),
    (4, 'Emma', 'MIKA', '2003-10-17', 80966, 'F', null),
    (4, 'Cyrielle', 'DARDE', '2003-02-16', 15432, 'F', null),
    (4, 'Pauline', 'LE CHANJOUR', '2004-08-21', 77431, 'F', null),
    (4, 'Heloise', 'PELLETIER', '2003-07-08', 83032, 'F', null),
    (4, 'Victoire', 'MARCAILLOU', '2003-03-24', 38749, 'F', null),
    (4, 'Garance', 'ROGER', '2005-01-14', 51037, 'F', null),
    (4, 'Keren', 'AYE', '2006-04-17', 135555, 'F', null),
    (4, 'Emily', 'PARRA', '2003-06-29', 82742, 'F', null),

-- FLEURET DAMES SENIORS
    (5, 'Pauline', 'RANVIER', '1994-04-14', 49227, 'F', null),
    (5, 'Ysaora', 'THIBUS', '1991-08-22', 56061, 'F', null),
    (5, 'Solene', 'BUTRUILLE', '1997-11-02', 9456, 'F', null),
    (5, 'Constance', 'CATARZI', '1998-12-22', 130899, 'F', null),
    (5, 'Morgane', 'PATRU', '1998-02-07', 45139, 'F', null),
    (5, 'Coralie', 'BROT', '1995-05-09', 8799, 'F', null),
    (5, 'Eva', 'LACHERAY', '2000-03-11', 32498, 'F', null),
    (5, 'Jade', 'MARECHAL', '2000-10-02', 79731, 'F', null),
    (5, 'Anita', 'BLAZE', '1991-10-29', 5982, 'F', null),
    (5, 'Emmie', 'NAYL', '2002-05-09', 43387, 'F', null),

-- FLEURET DAMES VETERANS 1
    (6, 'Virginie', 'SEBBANE', '1975-05-13', 140691, 'F', null),
    (6, 'Ritva Irene', 'ENRIGHT', '1977-01-18', 21121, 'F', null),
    (6, 'Annaick', 'FERRARI', '1977-11-22', 71384, 'F', null),
    (6, 'Emmanuelle', 'FAURE', '1977-09-17', 208782, 'F', null),
    (6, 'Christina', 'CERNY', '1978-05-11', 11005, 'F', null),
    (6, 'Mathilde', 'GERARD', '1975-11-15', 131194, 'F', null),
    (6, 'Marie', 'LAROCHE MANCEAU', '1982-04-16', 280152, 'F', null),
    (6, 'Anne Sabine', 'GUILLEMINOT ROUX', '1976-07-18', 27812, 'F', null),
    (6, 'Louise', 'CAZILHAC', '1988-10-21', 10914, 'F', null),
    (6, 'Cindy', 'BONJEAN', '1978-12-24', 6658, 'F', null),


-- SABRE DAMES U15
    (2, 'Lucile', 'MOLL', '2008-02-13', 132102, 'F', null),
    (2, 'Carmen', 'WULLUS', '2008-10-08', 133470, 'F', null),
    (2, 'Lucie', 'COURT', '2008-04-21', 149504, 'F', null),
    (2, 'Alix', 'DELANNOY', '2008-08-17', 159059, 'F', null),
    (2, 'Marilou', 'ALLAIRE', '2008-12-04', 116121, 'F', null),
    (2, 'Justine', 'SAUSSINE', '2009-01-06', 190876, 'F', null),
    (2, 'Juliette', 'CAYRE', '2008-06-17', 162846, 'F', null),
    (2, 'Loane', 'COSSY-BRAGLIA', '2008-02-04', 144957, 'F', null),
    (2, 'Hui Xin', 'SEZILLE', '2009-02-28', 293460, 'F', null),
    (2, 'Charlotte', 'TENAILLEAU', '2010-05-31', 176510, 'F', null),

-- SABRE DAMES U17
    (3, 'Aurore', 'PATRICE', '2006-09-26', 122357, 'F', null),
    (3, 'Rita', 'ROBINEAUX', '2006-12-17', 156496, 'F', null),
    (3, 'Marie', 'DEBES', '2006-01-25', 68547, 'F', null),
    (3, 'Emmy', 'LEGARET', '2006-10-05', 143110, 'F', null),
    (3, 'Emma', 'ARRIBET', '2006-05-10', 158514, 'F', null),
    (3, 'Camille', 'GITTON', '2006-03-15', 133317, 'F', null),
    (3, 'Céline', 'GIRAUD', '2006-01-28', 179739, 'F', null),
    (3, 'Mathilde', 'BABANDO', '2007-04-29', 178914, 'F', null),
    (3, 'Salome', 'BERGER', '2006-10-12', 62604, 'F', null),
    (3, 'Laïa', 'BERGEZ', '2007-02-01', 133383, 'F', null),

-- SABRE DAMES U20
    (4, 'Toscane', 'TORI', '2004-03-03', 112853, 'F', null),
    (4, 'Lola', 'TRANQUILLE', '2003-06-16', 98376, 'F', null),
    (4, 'Roxane', 'CHABROL', '2005-06-19', 65868, 'F', null),
    (4, 'Ilona', 'RIBEIRO', '2003-07-08', 93138, 'F', null),
    (4, 'Eléa', 'FAUR', '2005-05-13', 181629, 'F', null),
    (4, 'Lila', 'MARTEL', '2003-02-23', 39305, 'F', null),
    (4, 'Alexandra', 'MANGA', '2005-08-01', 155264, 'F', null),
    (4, 'Cyrielle', 'GIRARDIN', '2003-09-03', 25795, 'F', null),
    (4, 'Mathilde', 'MOUROUX', '2003-09-30', 105462, 'F', null),
    (4, 'Pauline', 'SIMONS', '2004-10-06', 133399, 'F', null),

-- SABRE DAMES SENIORS
    (5, 'Sara', 'BALZER', '1995-04-03', 2628, 'F', null),
    (5, 'Caroline', 'QUEROLI', '1998-06-05', 48804, 'F', null),
    (5, 'Margaux', 'RIFKISS', '1996-06-09', 50341, 'F', null),
    (5, 'Manon', 'APITHY-BRUNET', '1996-02-07', 9036, 'F', null),
    (5, 'Faustine', 'CLAPIER', '2001-12-06', 66675, 'F', null),
    (5, 'Mathilde', 'MOUROUX', '2003-09-30', 105462, 'F', null),
    (5, 'Anne', 'POUPINET', '2000-04-27', 48067, 'F', null),
    (5, 'Cecilia', 'BERDER', '1989-12-13', 4471, 'F', null),
    (5, 'Malina', 'VONGSAVADY', '1997-05-17', 59330, 'F', null),
    (5, 'Kelly', 'LUSINIER', '2000-07-22', 37788, 'F', null),

-- SABRE DAMES VETERANS 1
    (6, 'Jessica', 'DE MORAIS', '1982-12-24', 16205, 'F', null),
    (6, 'Annaick', 'FERRARI', '1977-11-22', 71384, 'F', null),
    (6, 'Catherine', 'CAVERON', '1974-09-04', 140901, 'F', null),
    (6, 'Claire', 'BRISSON', '1982-03-09', 213778, 'F', null),
    (6, 'Zohra', 'BRAHIMI', '1981-06-06', 266339, 'F', null),
    (6, 'Nathalie', 'BOIVIN', '1987-08-10', 6455, 'F', null),
    (6, 'Anne Sophie', 'REYNEN', '1982-09-07', 50031, 'F', null),
    (6, 'Julie', 'FRIBOULET', '1976-03-18', 23635, 'F', null),
    (6, 'Emilie', 'LLAPASSET', '1976-10-21', 148227, 'F', null),
    (6, 'Marie-Pierre', 'HUET-HENAULT', '1978-01-11', 262801, 'F', null),


-- EPEE HOMME U15
    (2, 'Hiroaki', 'TOTO', '2009-02-20', 130253, 'M', null),
    (2, 'Louis', 'LE TREUT', '2008-04-23', 137222, 'M', null),
    (2, 'Thomas', 'GAULIARD', '2008-05-14', 107947, 'M', null),
    (2, 'Jules', 'LEGER', '2008-10-12', 166382, 'M', null),
    (2, 'Xavier', 'CUADRADO', '2008-01-01', 118007, 'M', null),
    (2, 'Lilian', 'CARON', '2008-08-16', 134485, 'M', null),
    (2, 'Noé', 'RAMBAUD', '2008-02-27', 173851, 'M', null),
    (2, 'Pierre', 'NAHAS', '2008-08-22', 120367, 'M', null),
    (2, 'Théodore', 'VINCENT', '2009-05-01', 221192, 'M', null),
    (2, 'Lucien', 'LEBLANC-MOREL', '2009-07-31', 130475, 'M', null),

-- EPEE HOMME U17
    (3, 'Aina', 'RAHAMEFY', '2006-04-21', 90309, 'M', null),
    (3, 'Noam', 'DUCHENE', '2007-07-12', 222879, 'M', null),
    (3, 'Mattéo', 'LESPONNE-DENIS', '2006-03-10', 169495, 'M', null),
    (3, 'Theo', 'MITRAIL', '2007-01-31', 118182, 'M', null),
    (3, 'Maxime', 'BARRE', '2006-03-01', 61872, 'M', null),
    (3, 'Sacha', 'LEBEL', '2007-03-28', 106151, 'M', null),
    (3, 'Odinn', 'BINDAS', '2006-08-18', 279693, 'M', null),
    (3, 'Leo', 'BARRET', '2006-03-14', 61885, 'M', null),
    (3, 'Raphaël', 'DUVALLET', '2006-08-25', 257151, 'M', null),
    (3, 'Tristan', 'REMY', '2006-02-22', 161048, 'M', null),

-- EPEE HOMME U20
    (4, 'Lino', 'HEURLIN-VAZQUEZ', '2003-10-29', 165239, 'M', null),
    (4, 'Gauthier', 'GIORGI', '2004-03-15', 94004, 'M', null),
    (4, 'Mael', 'DENAUX', '2003-07-05', 17597, 'M', null),
    (4, 'Nolan', 'WINGERTER', '2005-10-28', 90018, 'M', null),
    (4, 'Samuel', 'RAVELO DE TOVAR', '2005-05-31', 112647, 'M', null),
    (4, 'Anatole', 'TRIEU-COPPENS', '2004-10-11', 17604, 'M', null),
    (4, 'Ulysse', 'LESIMPLE', '2005-06-30', 90019, 'M', null),
    (4, 'Abdelkader', 'BELMOKHTAR', '2004-05-04', 99410, 'M', null),
    (4, 'Antonin', 'MARCHAL', '2004-07-28', 282196, 'M', null),
    (4, 'Antonin', 'SOUAIL', '2004-01-15', 90020, 'M', null),

-- EPEE HOMME SENIORS
    (5, 'Hakim', 'RAHAMEFY', '2002-08-22', 117880, 'M', null),
    (5, 'Julien', 'HUARD', '1986-08-18', 19208, 'M', null),
    (5, 'Pierre', 'CHABOD', '1999-01-23', 80814, 'M', null),
    (5, 'Tom', 'WILLIAMS', '1993-04-13', 210708, 'M', null),
    (5, 'Ihsan', 'KANOUN', '2000-09-04', 106789, 'M', null),
    (5, 'Sami', 'LOUEDEC', '1996-11-26', 162029, 'M', null),
    (5, 'Lucas', 'HEPP', '1998-02-18', 156636, 'M', null),
    (5, 'Corentin', 'DROZDOWICZ', '1996-07-26', 125678, 'M', null),
    (5, 'Boris', 'BIENAIM', '1998-09-24', 157453, 'M', null),
    (5, 'Lukas', 'NOYER', '1997-01-19', 173822, 'M', null),

-- EPEE HOMME VÉTÉRANS 1
    (6, 'Julien', 'RENAUD', '1982-06-29', 27470, 'M', null),
    (6, 'Renaud', 'PERRET', '1977-12-10', 18978, 'M', null),
    (6, 'Benoit', 'GRENIER', '1980-08-17', 14396, 'M', null),
    (6, 'Pascal', 'BAILLET', '1982-04-06', 24113, 'M', null),
    (6, 'François', 'RENAULT', '1981-07-19', 14382, 'M', null),
    (6, 'Jérôme', 'SIMON', '1978-05-17', 19774, 'M', null),
    (6, 'Alexandre', 'LEMAIRE', '1976-10-23', 13729, 'M', null),
    (6, 'Laurent', 'WAGNER', '1981-04-26', 14078, 'M', null),
    (6, 'Bruno', 'BOUCHET', '1979-09-27', 25083, 'M', null),
    (6, 'Mathieu', 'LARUE', '1978-02-18', 21772, 'M', null),
    
-- FLEURET HOMME U15
    (2, 'Lucien', 'GIRARDOT', '2009-05-13', 204893, 'M', null),
    (2, 'Andreï', 'PLATOV', '2008-09-03', 130121, 'M', null),
    (2, 'Mahel', 'BOUMAZA', '2009-02-03', 147259, 'M', null),
    (2, 'Enzo', 'MIRANDE', '2008-03-12', 185282, 'M', null),
    (2, 'Thomas', 'PEN SAING', '2008-06-26', 128872, 'M', null),
    (2, 'Léo', 'BLANCHARD', '2009-07-19', 142651, 'M', null),
    (2, 'Milo', 'VANDAELE', '2008-01-30', 129422, 'M', null),
    (2, 'Arlo', 'BARTHELEMY', '2008-02-04', 127775, 'M', null),
    (2, 'Maxime', 'DUMAS', '2008-08-25', 213592, 'M', null),
    (2, 'Côme', 'BOUTHILLIER-MOUZIN', '2008-01-23', 142854, 'M', null),

-- FLEURET HOMME U17
    (3, 'Maxime', 'DUBREUIL', '2006-06-20', 110775, 'M', null),
    (3, 'Noah', 'ANDRIAMASINARIVO', '2006-02-26', 60894, 'M', null),
    (3, 'Guillaume', 'WATSON', '2007-05-22', 89901, 'M', null),
    (3, 'Auquelin', 'TOULOT VERDIER', '2006-11-17', 131989, 'M', null),
    (3, 'Lucien', 'FOURDRINOY', '2006-01-22', 71856, 'M', null),
    (3, 'Dylan', 'SEMEDO SANCHES', '2006-06-24', 120674, 'M', null),
    (3, 'Zakaria', 'JEANNIN BANGOURA', '2006-08-10', 141359, 'M', null),
    (3, 'Thibaut', 'GAVEN MARY', '2007-09-27', 72695, 'M', null),
    (3, 'Ulysse', 'PARPEYRAT FOURNEL', '2007-03-22', 112716, 'M', null),
    (3, 'Selyan', 'AOUDIA', '2006-01-06', 104342, 'M', null),

-- FLEURET HOMME U20
    (4, 'Wael', 'ABDELJALIL', '2003-09-23', 33, 'M', null),
    (4, 'Adrien', 'SPICHIGER', '2003-10-27', 54795, 'M', null),
    (4, 'Anas', 'ANANE', '2004-05-13', 129035, 'M', null),
    (4, 'Adrien', 'HELMY-COCOYNACQ', '2005-01-26', 113331, 'M', null),
    (4, 'Jean Charles', 'BESNAULT', '2004-03-01', 5155, 'M', null),
    (4, 'Antoine', 'SPICHIGER', '2005-02-13', 54796, 'M', null),
    (4, 'Numa', 'CRIST', '2005-04-16', 223059, 'M', null),
    (4, 'Eliot', 'CHAGNON', '2004-07-09', 65877, 'M', null),
    (4, 'Louis', 'PRADEL', '2005-11-07', 84283, 'M', null),
    (4, 'Alexis', 'BESSY', '2003-12-27', 5226, 'M', null),

-- FLEURET HOMME SENIORS
    (5, 'Maxime', 'PAUTY', '1993-06-20', 45243, 'M', null),
    (5, 'Alexandre', 'EDIRI', '1998-01-30', 20840, 'M', null),
    (5, 'Rafael', 'SAVIN', '2000-09-15', 53089, 'M', null),
    (5, 'Julien', 'MERTINE', '1988-06-25', 40845, 'M', null),
    (5, 'Pierre', 'LOISEL', '1998-03-06', 37189, 'M', null),
    (5, 'Alexandre', 'SIDO', '1996-10-31', 53998, 'M', null),
    (5, 'Armand', 'SPICHIGER', '2001-06-07', 54797, 'M', null),
    (5, 'Maximilien', 'CHASTANET', '1996-03-15', 11795, 'M', null),
    (5, 'Tyvan', 'BIBARD', '1999-05-22', 5387, 'M', null),
    (5, 'Enzo', 'LEFORT', '1991-09-29', 35524, 'M', null),

-- FLEURET HOMME VETERANTS 1
    (6, 'Jean Charles', 'BESSET', '1982-12-03', 5189, 'M', null),
    (6, 'Jean Paul', 'CAZILHAC', '1982-10-11', 10913, 'M', null),
    (6, 'Xavier', 'ALI', '1974-08-16', 560, 'M', null),
    (6, 'Cedric', 'BENTZ', '1978-08-10', 4405, 'M', null),
    (6, 'Fabrice', 'RICHAUD', '1974-04-01', 50233, 'M', null),
    (6, 'Renaud', 'LASSELIN', '1978-12-21', 77126, 'M', null),
    (6, 'Yannick', 'PIERRE', '1980-02-05', 260817, 'M', null),
    (6, 'Matthieu', 'FROMBAUM', '1983-04-09', 209993, 'M', null),
    (6, 'Benoit', 'PERRIER', '1977-08-15', 45939, 'M', null),
    (6, 'Eric', 'TREPO', '1981-07-31', 57025, 'M', null),

-- SABRE HOMME U15
    (2, 'Antoine', 'SIROU', '2008-09-12', 157156, 'M', null),
    (2, 'Arthur', 'CALLAY', '2008-06-19', 136274, 'M', null),
    (2, 'Maxence', 'BLOIN', '2008-03-30', 123412, 'M', null),
    (2, 'Hugo', 'BAJRACHARYA', '2008-02-09', 183847, 'M', null),
    (2, 'Baptiste', 'HOSPITAL', '2008-04-06', 118849, 'M', null),
    (2, 'Baptiste', 'PICCIOLI', '2008-06-13', 134140, 'M', null),
    (2, 'Esteban', 'POUHAER', '2008-05-08', 141230, 'M', null),
    (2, 'Ulysse', 'LE GAC BRIAND', '2008-03-28', 156760, 'M', null),
    (2, 'Melville', 'DORIN', '2008-08-04', 178798, 'M', null),
    (2, 'Romain', 'TOUCOUERE SCHMITZ', '2009-06-29', 183858, 'M', null),

-- SABRE HOMME U17
    (3, 'Remy', 'BAYSAL', '2006-06-08', 62092, 'M', null),
    (3, 'Victor', 'BEAUBIAT', '2006-01-13', 161794, 'M', null),
    (3, 'Tom', 'COUDERC', '2006-01-13', 67340, 'M', null),
    (3, 'Maximilien', 'TORI', '2006-05-09', 128999, 'M', null),
    (3, 'Roman', 'FRABOULET', '2007-04-26', 157322, 'M', null),
    (3, 'Paul', 'ROUVIERE', '2006-05-15', 86051, 'M', null),
    (3, 'Rodrigue', 'BERARDINI', '2006-09-02', 190335, 'M', null),
    (3, 'Mahe', 'HENON SAYAH', '2006-07-27', 209423, 'M', null),
    (3, 'Michel', 'CHOUEIRY', '2007-09-26', 113671, 'M', null),
    (3, 'Titouan', 'CHAUVEL', '2007-04-30', 92537, 'M', null),

-- SABRE HOMME U20
    (4, 'Remi', 'GARRIGUE', '2004-09-03', 24526, 'M', null),
    (4, 'Evan', 'FRABOULET', '2003-10-07', 71950, 'M', null),
    (4, 'Francois', 'MARUELLE', '2003-03-08', 39689, 'M', null),
    (4, 'Jeremy', 'CUSTINE', '2003-08-25', 67708, 'M', null),
    (4, 'Benjamin', 'DUCERF', '2004-04-26', 90728, 'M', null),
    (4, 'Armand', 'ROCHET', '2003-04-20', 103888, 'M', null),
    (4, 'Alexandre', 'LACAZE', '2003-09-05', 76530, 'M', null),
    (4, 'Lucas', 'GUILLEY', '2005-10-20', 27867, 'M', null),
    (4, 'Ugo', 'LATAPY', '2003-02-16', 33726, 'M', null),
    (4, 'Tom', 'COUDERC', '2006-01-13', 67340, 'M', null),

-- SABRE HOMME SENIORS
    (5, 'Maxime', 'PIANFETTI', '1999-03-15', 46558, 'M', null),
    (5, 'Sebastien', 'PATRICE', '2000-07-04', 82843, 'M', null),
    (5, 'Eliott', 'BIBI', '1999-10-29', 5388, 'M', null),
    (5, 'Tom', 'SEITZ', '1994-05-31', 53630, 'M', null),
    (5, 'Thomas', 'MARTINE', '1999-01-29', 39554, 'M', null),
    (5, 'Bolade', 'APITHY', '1985-08-21', 1240, 'M', null),
    (5, 'Jean Philippe', 'PATRICE', '1997-03-12', 45133, 'M', null),
    (5, 'Charles', 'COLLEAU', '1996-03-06', 13262, 'M', null),
    (5, 'Maxence', 'LAMBERT', '1994-05-13', 33104, 'M', null),
    (5, 'Remi', 'GARRIGUE', '2004-09-03', 24526, 'M', null),

-- SABRE HOMME VETERANS 1
    (6, 'Mathieu', 'BELLET', '1978-09-23', 4032, 'M', null),
    (6, 'Cyrille', 'BELLET', '1975-07-06', 4029, 'M', null),
    (6, 'Christophe', 'TURLIER', '1977-10-29', 241387, 'M', null),
    (6, 'Eric', 'FREMONT', '1977-03-11', 23563, 'M', null),
    (6, 'Jean', 'MOULINIER', '1976-05-02', 181398, 'M', null),
    (6, 'Abdoulaye', 'DIOP', '1979-06-12', 114645, 'M', null),
    (6, 'Fabrice', 'SARREY', '1980-01-05', 52892, 'M', null),
    (6, 'Olivier', 'TEXIER', '1974-07-23', 223600, 'M', null),
    (6, 'Emmanuel', 'REYNEN', '1978-01-22', 50032, 'M', null),
    (6, 'Thomas', 'ZIPPER', '1980-10-16', 130002, 'M', null);

-- -- Table TIREUR
-- INSERT INTO TIREUR (idTireur, idClub, classement)
-- VALUES

-- -- Table ARBITRE
-- INSERT INTO ARBITRE (idArbitre)
-- VALUES
--     (1),
--     (2);

-- Table PRATIQUER_ARME
INSERT INTO PRATIQUER_ARME (idEscrimeur, idArme)
VALUES
-- EPEE DAMES U15
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 1),

-- EPEE DAMES U17
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
    (20, 1),

-- EPEE DAMES U20
    (21, 1),
    (22, 1),
    (23, 1),
    (24, 1),
    (25, 1),
    (26, 1),
    (27, 1),
    (28, 1),
    (29, 1),
    (30, 1),

-- EPEE DAMES SENIORS
    (31, 1),
    (32, 1),
    (33, 1),
    (34, 1),
    (35, 1),
    (36, 1),
    (37, 1),
    (38, 1),
    (39, 1),
    (40, 1),

-- EPEE DAMES VETERANS 1
    (41, 1),
    (42, 1),
    (43, 1),
    (44, 1),
    (45, 1),
    (46, 1),
    (47, 1),
    (48, 1),
    (49, 1),
    (50, 1),

-- FLEURET DAMES U15
    (51, 2),
    (52, 2),
    (53, 2),
    (54, 2),
    (55, 2),
    (56, 2),
    (57, 2),
    (58, 2),
    (59, 2),
    (60, 2),

-- FLEURET DAMES U17
    (61, 2),
    (62, 2),
    (63, 2),
    (64, 2),
    (65, 2),
    (66, 2),
    (67, 2),
    (68, 2),
    (69, 2),
    (70, 2),

-- FLEURET DAMES U20
    (71, 2),
    (72, 2),
    (73, 2),
    (74, 2),
    (75, 2),
    (76, 2),
    (77, 2),
    (78, 2),
    (79, 2),
    (80, 2),

-- FLEURET DAMES SENIORS
    (81, 2),
    (82, 2),
    (83, 2),
    (84, 2),
    (85, 2),
    (86, 2),
    (87, 2),
    (88, 2),
    (89, 2),
    (90, 2),

-- FLEURET DAMES VETERANS 1
    (91, 2),
    (92, 2),
    (93, 2),
    (94, 2),
    (95, 2),
    (96, 2),
    (97, 2),
    (98, 2),
    (99, 2),
    (100, 2),

-- SABRE DAMES U15
    (101, 3),
    (102, 3),
    (103, 3),
    (104, 3),
    (105, 3),
    (106, 3),
    (107, 3),
    (108, 3),
    (109, 3),
    (110, 3),

-- SABRE DAMES U17
    (111, 3),
    (112, 3),
    (113, 3),
    (114, 3),
    (115, 3),
    (116, 3),
    (117, 3),
    (118, 3),
    (119, 3),
    (120, 3),

-- SABRE DAMES U20
    (121, 3),
    (122, 3),
    (123, 3),
    (124, 3),
    (125, 3),
    (126, 3),
    (127, 3),
    (128, 3),
    (129, 3),
    (130, 3),

-- SABRE DAMES SENIORS
    (131, 3),
    (132, 3),
    (133, 3),
    (134, 3),
    (135, 3),
    (136, 3),
    (137, 3),
    (138, 3),
    (139, 3),
    (140, 3),

-- SABRE DAMES VETERANS 1
    (141, 3),
    (142, 3),
    (143, 3),
    (144, 3),
    (145, 3),
    (146, 3),
    (147, 3),
    (148, 3),
    (149, 3),
    (150, 3),

-- EPEE HOMME U15
    (151, 1),
    (152, 1),
    (153, 1),
    (154, 1),
    (155, 1),
    (156, 1),
    (157, 1),
    (158, 1),
    (159, 1),
    (160, 1),

-- EPEE HOMME U17
    (161, 1),
    (162, 1),
    (163, 1),
    (164, 1),
    (165, 1),
    (166, 1),
    (167, 1),
    (168, 1),
    (169, 1),
    (170, 1),

-- EPEE HOMME U20
    (171, 1),
    (172, 1),
    (173, 1),
    (174, 1),
    (175, 1),
    (176, 1),
    (177, 1),
    (178, 1),
    (179, 1),
    (180, 1),

-- EPEE HOMME SENIORS
    (181, 1),
    (182, 1),
    (183, 1),
    (184, 1),
    (185, 1),
    (186, 1),
    (187, 1),
    (188, 1),
    (189, 1),
    (190, 1),

-- EPEE HOMME VÉTÉRANS 1
    (191, 1),
    (192, 1),
    (193, 1),
    (194, 1),
    (195, 1),
    (196, 1),
    (197, 1),
    (198, 1),
    (199, 1),
    (200, 1),

-- FLEURET HOMME U15
    (201, 2),
    (202, 2),
    (203, 2),
    (204, 2),
    (205, 2),
    (206, 2),
    (207, 2),
    (208, 2),
    (209, 2),
    (210, 2),

-- FLEURET HOMME U17
    (211, 2),
    (212, 2),
    (213, 2),
    (214, 2),
    (215, 2),
    (216, 2),
    (217, 2),
    (218, 2),
    (219, 2),
    (220, 2),

-- FLEURET HOMME U20
    (221, 2),
    (222, 2),
    (223, 2),
    (224, 2),
    (225, 2),
    (226, 2),
    (227, 2),
    (228, 2),
    (229, 2),
    (230, 2),

-- FLEURET HOMME SENIORS
    (231, 2),
    (232, 2),
    (233, 2),
    (234, 2),
    (235, 2),
    (236, 2),
    (237, 2),
    (238, 2),
    (239, 2),
    (240, 2),

-- FLEURET HOMME VÉTÉRANS 1
    (241, 2),
    (242, 2),
    (243, 2),
    (244, 2),
    (245, 2),
    (246, 2),
    (247, 2),
    (248, 2),
    (249, 2),
    (250, 2),

-- SABRE HOMME U15
    (251, 3),
    (252, 3),
    (253, 3),
    (254, 3),
    (255, 3),
    (256, 3),
    (257, 3),
    (258, 3),
    (259, 3),
    (260, 3),

-- SABRE HOMME U17
    (261, 3),
    (262, 3),
    (263, 3),
    (264, 3),
    (265, 3),
    (266, 3),
    (267, 3),
    (268, 3),
    (269, 3),
    (270, 3),

-- SABRE HOMME U20
    (271, 3),
    (272, 3),
    (273, 3),
    (274, 3),
    (275, 3),
    (276, 3),
    (277, 3),
    (278, 3),
    (279, 3),
    (280, 3),

-- SABRE HOMME SENIORS
    (281, 3),
    (282, 3),
    (283, 3),
    (284, 3),
    (285, 3),
    (286, 3),
    (287, 3),
    (288, 3),
    (289, 3),
    (290, 3),

-- SABRE HOMME VÉTÉRANS 1
    (291, 3),
    (292, 3),
    (293, 3),
    (294, 3),
    (295, 3),
    (296, 3),
    (297, 3),
    (298, 3),
    (299, 3),
    (300, 3);

-- test escrimeurs pratiquer plusieurs armes
INSERT INTO PRATIQUER_ARME (idEscrimeur, idArme)
VALUES
    (1, 2),
    (2, 2),
    (3, 2),

    (4, 3),
    (5, 3),
    (6, 3),

    (7, 2),
    (7, 3),

    (8, 2),
    (8, 3),

    (9, 2),
    (9, 3),

    (10, 2),
    (10, 3);

-- Table CLASSEMENT_FINAL
INSERT INTO CLASSEMENT_FINAL (idComp, idTireur, position)
VALUES
    (1, 1, 1),
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 4),
    (1, 5, 5),
    (1, 6, 6),
    (1, 7, 7),
    (1, 8, 8),
    (1, 9, 9),
    (1, 10, 10);

-- Table POULE
INSERT INTO POULE (idComp, idPiste, idArbitre, nomPoule)
VALUES
    (1, 1, 1, 'Poule A'),
    (1, 2, 2, 'Poule B'),
    (1, 3, 3, 'Poule C'),
    (1, 4, 4, 'Poule D');

-- Table PARTICIPANTS_POULE
INSERT INTO PARTICIPANTS_POULE (idPoule, idTireur)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (2, 9),
    (2, 10),
    (2, 11),
    (2, 12),
    (2, 13),
    (2, 14),
    (2, 15),
    (2, 16),
    (3, 17),
    (3, 18),
    (3, 19),
    (3, 20),
    (3, 21),
    (3, 22),
    (3, 23),
    (3, 24),
    (4, 25),
    (4, 26),
    (4, 27),
    (4, 28),
    (4, 29),
    (4, 30),
    (4, 31),
    (4, 32);

-- Table MATCH_POULE
INSERT INTO MATCH_POULE (idTypeMatch, idPoule, idPiste, idArbitre, idTireur1, idTireur2, dateMatch, heureMatch, touchesRecuesTireur1, touchesDonneesTireur1, touchesRecuesTireur2, touchesDonneesTireur2)
VALUES
    (1, 1, 1, 1, 1, 8, '2024-04-15', '10:00:00'),
    (1, 1, 1, 1, 2, 7, '2024-04-15', '10:30:00'),
    (1, 1, 1, 1, 3, 6, '2024-04-15', '11:00:00'),
    (1, 1, 1, 1, 4, 5, '2024-04-15', '11:30:00'),

    (1, 2, 2, 2, 9, 16, '2024-04-15', '12:00:00'),
    (1, 2, 2, 2, 10, 15, '2024-04-15', '12:30:00'),
    (1, 2, 2, 2, 11, 14, '2024-04-15', '13:00:00'),
    (1, 2, 2, 2, 12, 13, '2024-04-15', '13:30:00'),

    (1, 3, 3, 3, 17, 24, '2024-04-15', '14:00:00'),
    (1, 3, 3, 3, 18, 23, '2024-04-15', '14:30:00'),
    (1, 3, 3, 3, 19, 22, '2024-04-15', '15:00:00'),
    (1, 3, 3, 3, 20, 21, '2024-04-15', '15:30:00'),

    (1, 4, 4, 4, 25, 32, '2024-04-15', '16:00:00'),
    (1, 4, 4, 4, 26, 31, '2024-04-15', '16:30:00'),
    (1, 4, 4, 4, 27, 30, '2024-04-15', '17:00:00'),
    (1, 4, 4, 4, 28, 29, '2024-04-15', '17:30:00');

-- Table FEUILLE_MATCH
INSERT INTO FEUILLE_MATCH (idPoule, idComp, idTireur1, idTireur2, scoreTireur1, scoreTireur2)
VALUES
    (1, 1, 1, 8),
    (1, 1, 2, 7),
    (1, 1, 3, 6),
    (1, 1, 4, 5),

    (1, 2, 9, 16),
    (1, 2, 10, 15),
    (1, 2, 11, 14),
    (1, 2, 12, 13),

    (1, 3, 17, 24),
    (1, 3, 18, 23),
    (1, 3, 19, 22),
    (1, 3, 20, 21),

    (1, 4, 25, 32),
    (1, 4, 26, 31),
    (1, 4, 27, 30),
    (1, 4, 28, 29);