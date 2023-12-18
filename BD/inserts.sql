-- Table USER
INSERT INTO USER (pseudoUser, mdpUser, emailUser)
VALUES
    ('irvyncsm', 'dc02c547057f94d418761ec354cea801bdd9741206e32a83500a3b476485192f', 'irvyncsm@gmail.com'),
    ('alexandre', 'alexandre', 'alexandre@gmail.com');

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

-- EPEE DAMES U15
    (2, 'Maëlys', 'LEVALLOIS', '2009-03-29', 175387, 'F', null),
    (2, 'Rubeen', 'REMBI', '2008-11-15', 17545, 'F', null),
    (2, 'Maïlys', 'DALLEAS', '2008-01-01', 177583, 'F', null),
    (2, 'Toscane', 'GRUSON', '2008-05-07', 185987, 'F', null),
    (2, 'Soha', 'DOUCI HABANE', '2009-02-16', 164751, 'F', null),
    (2, 'Laura', 'VERGES', '2009-01-19', 168928, 'F', null),
    (2, 'Faustine', 'GASPARD', '2009-01-22', 205331, 'F', null),
    (2, 'Charlotte', 'LOUE', '2010-03-17', 224542, 'F', null),
    (2, 'Audrey', 'BERNADO', '2008-05-23', 148250, 'F', null),
    (2, 'Margaux', 'DUMETZ', '2010-06-01', 228366, 'F', null),

-- EPEE DAMES U17
    (3, 'Lana', 'TARIN', '2006-01-13', 129212, 'F', null),
    (3, 'Gwendoline Agathe', 'LAHAROTTE', '2006-05-17', 76700, 'F', null),
    (3, 'Judith', 'ROMAN', '2007-08-06', 147282, 'F', null),
    (3, 'Sophie', 'STEIMER', '2007-03-27', 113544, 'F', null),
    (3, 'Ophélie', 'MOYA', '2006-10-12', 113759, 'F', null),
    (3, 'Ambre', 'MOURCEAU', '2006-07-27', 174028, 'F', null),
    (3, 'Anais', 'PESSAROSSI', '2007-01-04', 161090, 'F', null),
    (3, 'Charlie', 'BARON', '2006-10-13', 131480, 'F', null),
    (3, 'Rubeen', 'REMBI', '2008-11-15', 175451, 'F', null),
    (3, 'Cléophée', 'BARTHEL', '2006-11-21', 259042, 'F', null),

-- EPEE DAMES U20
    (4, 'Oceane', 'FRANCILLONNE', '2004-09-18', 71982, 'F', null),
    (4, 'Anaelle', 'DOQUET', '2005-01-06', 98466, 'F', null),
    (4, 'Elena', 'SEILLE', '2003-05-01', 135870, 'F', null),
    (4, 'Elea', 'JOUVE', '2004-06-25', 31330, 'F', null),
    (4, 'Thaïs', 'NAUCELLE-JARDEL', '2004-11-08', 144492, 'F', null),
    (4, 'Garance', 'PALPACUER', '2004-12-30', 129588, 'F', null),
    (4, 'Faustine', 'GENIEZ', '2005-08-24', 25072, 'F', null),
    (4, 'Maëlyne', 'MUGNIER', '2004-04-28', 42935, 'F', null),
    (4, 'Emilie', 'BERNIGAUD', '2004-07-10', 187363, 'F', null),
    (4, 'Rachel', 'FERREOL', '2004-01-04', 149821, 'F', null),

-- EPEE DAMES SENIORS
    (5, 'Marie Florence', 'CANDASSAMY', '1991-02-26', 9918, 'F', null),
    (5, 'Auriane', 'MALLO-BRETON', '1993-10-11', 38480, 'F', null),
    (5, 'Alexandra', 'LOUIS MARIE', '1996-03-03', 37514, 'F', null),
    (5, 'Josephine', 'JACQUES ANDRE COQUIN', '1990-09-21', 30369, 'F', null),
    (5, 'Camille', 'NABETH', '1998-01-05', 43182, 'F', null),
    (5, 'Lauren', 'REMBI', '1992-09-03', 49657, 'F', null),
    (5, 'Jade', 'SERSOT', '2000-10-15', 53830, 'F', null),
    (5, 'Diane', 'VON KERSSENBROCK', '1998-09-28', 59316, 'F', null),
    (5, 'Eloise', 'VANRYSSEL', '1999-05-01', 57866, 'F', null),
    (5, 'Coraline', 'VITALIS', '1995-09-05', 59193, 'F', null),

-- EPEE DAMES VETERANS 1
    (6, 'Pascale', 'ERGAND', '1979-04-14', 210895, 'F', null),
    (6, 'Sandrine', 'DUMOULIN', '1976-01-09', 20166, 'F', null),
    (6, 'Lia', 'CHEVALIER', '1981-02-11', 12231, 'F', null),
    (6, 'Carole', 'MAJOREL', '1975-06-21', 38334, 'F', null),
    (6, 'Stephanie', 'LASMOLLES', '1980-11-17', 130778, 'F', null),
    (6, 'Marie', 'WACQUEZ', '1978-04-08', 238600, 'F', null),
    (6, 'Fabienne', 'TERRYN', '1979-04-03', 55799, 'F', null),
    (6, 'Cindy', 'BONJEAN', '1978-12-24', 6658, 'F', null),
    (6, 'Anne Sabine', 'GUILLEMINOT ROUX', '1976-07-18', 27812, 'F', null),
    (6, 'Marie Laure', 'BRIANCHON', '1983-11-12', 64584, 'F', null),

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
    (3, 'Mathilde', 'PRATS', '2008-03-09', 163748, 'F', null),
    (3, 'Marion', 'RAFIN', '2007-01-04', 167483, 'F', null),
    (3, 'Adèle', 'ANDRIAMAMPIANINA', '2008-04-10', 133479, 'F', null),
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
    (4, 'Keren', 'AYE', '2006-04-17', 135556, 'F', null),
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
    (6, 'Anne Sabine', 'GUILLEMINOT ROUX', '1976-07-18', 278121, 'F', null),
    (6, 'Louise', 'CAZILHAC', '1988-10-21', 10914, 'F', null),
    (6, 'Cindy', 'BONJEAN', '1978-12-24', 66581, 'F', null),


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
    (5, 'Mathilde', 'MOUROUX', '2003-09-30', 1054621, 'F', null),
    (5, 'Anne', 'POUPINET', '2000-04-27', 48067, 'F', null),
    (5, 'Cecilia', 'BERDER', '1989-12-13', 4471, 'F', null),
    (5, 'Malina', 'VONGSAVADY', '1997-05-17', 59330, 'F', null),
    (5, 'Kelly', 'LUSINIER', '2000-07-22', 37788, 'F', null),

-- SABRE DAMES VETERANS 1
    (6, 'Jessica', 'DE MORAIS', '1982-12-24', 16205, 'F', null),
    (6, 'Annaick', 'FERRARI', '1977-11-22', 713841, 'F', null),
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
    (3, 'Tom', 'COUDERC', '2006-01-13', 673401, 'M', null),
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
    (5, 'Remi', 'GARRIGUE', '2004-09-03', 245261, 'M', null),

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
INSERT INTO TIREUR (numeroLicenceE, idClub, classement)
VALUES
    -- insertions avec les bon numeros de licence, idclub=1 et classement de 1 à 10
    -- EPEE DAMES U15
    (175387, 1, 1),
    (17545, 1, 2),
    (177583, 1, 3),
    (185987, 1, 4),
    (164751, 1, 5),
    (168928, 1, 6),
    (205331, 1, 7),
    (224542, 1, 8),
    (148250, 1, 9),
    (228366, 1, 10),

    -- EPEE DAMES U17
    (129212, 1, 1),
    (76700, 1, 2),
    (147282, 1, 3),
    (113544, 1, 4),
    (113759, 1, 5),
    (174028, 1, 6),
    (161090, 1, 7),
    (131480, 1, 8),
    (175451, 1, 9),
    (259042, 1, 10),

    -- EPEE DAMES U20
    (71982, 1, 1),
    (98466, 1, 2),
    (135870, 1, 3),
    (31330, 1, 4),
    (144492, 1, 5),
    (129588, 1, 6),
    (25072, 1, 7),
    (42935, 1, 8),
    (187363, 1, 9),
    (149821, 1, 10),

    -- EPEE DAMES SENIORS
    (9918, 1, 1),
    (38480, 1, 2),
    (37514, 1, 3),
    (30369, 1, 4),
    (43182, 1, 5),
    (49657, 1, 6),
    (53830, 1, 7),
    (59316, 1, 8),
    (57866, 1, 9),
    (59193, 1, 10),

    -- EPEE DAMES VETERANS 1
    (210895, 1, 1),
    (20166, 1, 2),
    (12231, 1, 3),
    (38334, 1, 4),
    (130778, 1, 5),
    (238600, 1, 6),
    (55799, 1, 7),
    (6658, 1, 8),
    (27812, 1, 9),
    (64584, 1, 10),

    -- FLEURET DAMES U15
    (133478, 1, 1),
    (169221, 1, 2),
    (163749, 1, 3),
    (116048, 1, 4),
    (133493, 1, 5),
    (182444, 1, 6),
    (138405, 1, 7),
    (190486, 1, 8),
    (187370, 1, 9),
    (215767, 1, 10),

    -- FLEURET DAMES U17
    (135555, 1, 1),
    (109958, 1, 2),
    (65718, 1, 3),
    (100420, 1, 4),
    (230041, 1, 5),
    (67982, 1, 6),
    (163748, 1, 7),
    (167483, 1, 8),
    (133479, 1, 9),
    (191353, 1, 10),

    -- FLEURET DAMES U20
    (85977, 1, 1),
    (106336, 1, 2),
    (80966, 1, 3),
    (15432, 1, 4),
    (77431, 1, 5),
    (83032, 1, 6),
    (38749, 1, 7),
    (51037, 1, 8),
    (135556, 1, 9),
    (82742, 1, 10),

    -- FLEURET DAMES SENIORS
    (49227, 1, 1),
    (56061, 1, 2),
    (9456, 1, 3),
    (130899, 1, 4),
    (45139, 1, 5),
    (8799, 1, 6),
    (32498, 1, 7),
    (79731, 1, 8),
    (5982, 1, 9),
    (43387, 1, 10),

    -- FLEURET DAMES VETERANS 1
    (140691, 1, 1),
    (21121, 1, 2),
    (71384, 1, 3),
    (208782, 1, 4),
    (11005, 1, 5),
    (131194, 1, 6),
    (280152, 1, 7),
    (278121, 1, 8),
    (10914, 1, 9),
    (66581, 1, 10),

    -- SABRE DAMES U15
    (132102, 1, 1),
    (133470, 1, 2),
    (149504, 1, 3),
    (159059, 1, 4),
    (116121, 1, 5),
    (190876, 1, 6),
    (162846, 1, 7),
    (144957, 1, 8),
    (293460, 1, 9),
    (176510, 1, 10),

-- SABRE DAMES U17
    (122357, 1, 1),
    (156496, 1, 2),
    (68547, 1, 3),
    (143110, 1, 4),
    (158514, 1, 5),
    (133317, 1, 6),
    (179739, 1, 7),
    (178914, 1, 8),
    (62604, 1, 9),
    (133383, 1, 10),

-- SABRE DAMES U20
    (112853, 1, 1),
    (98376, 1, 2),
    (65868, 1, 3),
    (93138, 1, 4),
    (181629, 1, 5),
    (39305, 1, 6),
    (155264, 1, 7),
    (25795, 1, 8),
    (105462, 1, 9),
    (133399, 1, 10),

-- SABRE DAMES SENIORS
    (2628, 1, 1),
    (48804, 1, 2),
    (50341, 1, 3),
    (9036, 1, 4),
    (66675, 1, 5),
    (1054621, 1, 6),
    (48067, 1, 7),
    (4471, 1, 8),
    (59330, 1, 9),
    (37788, 1, 10),

-- SABRE DAMES VETERANS 1
    (16205, 1, 1),
    (713841, 1, 2),
    (140901, 1, 3),
    (213778, 1, 4),
    (266339, 1, 5),
    (6455, 1, 6),
    (50031, 1, 7),
    (23635, 1, 8),
    (148227, 1, 9),
    (262801, 1, 10),

-- EPEE HOMME U15
    (130253, 1, 1),
    (137222, 1, 2),
    (107947, 1, 3),
    (166382, 1, 4),
    (118007, 1, 5),
    (134485, 1, 6),
    (173851, 1, 7),
    (120367, 1, 8),
    (221192, 1, 9),
    (130475, 1, 10),

-- EPEE HOMME U17
    (90309, 1, 1),
    (222879, 1, 2),
    (169495, 1, 3),
    (118182, 1, 4),
    (61872, 1, 5),
    (106151, 1, 6),
    (279693, 1, 7),
    (61885, 1, 8),
    (257151, 1, 9),
    (161048, 1, 10),

-- EPEE HOMME U20
    (165239, 1, 1),
    (94004, 1, 2),
    (17597, 1, 3),
    (90018, 1, 4),
    (112647, 1, 5),
    (17604, 1, 6),
    (90019, 1, 7),
    (99410, 1, 8),
    (282196, 1, 9),
    (90020, 1, 10),

-- EPEE HOMME SENIORS
    (117880, 1, 1),
    (19208, 1, 2),
    (80814, 1, 3),
    (210708, 1, 4),
    (106789, 1, 5),
    (162029, 1, 6),
    (156636, 1, 7),
    (125678, 1, 8),
    (157453, 1, 9),
    (173822, 1, 10),

-- EPEE HOMME VÉTÉRANS 1
    (27470, 1, 1),
    (18978, 1, 2),
    (14396, 1, 3),
    (24113, 1, 4),
    (14382, 1, 5),
    (19774, 1, 6),
    (13729, 1, 7),
    (14078, 1, 8),
    (25083, 1, 9),
    (21772, 1, 10),

    -- FLEURET HOMME U15
    (204893, 1, 1),
    (130121, 1, 2),
    (147259, 1, 3),
    (185282, 1, 4),
    (128872, 1, 5),
    (142651, 1, 6),
    (129422, 1, 7),
    (127775, 1, 8),
    (213592, 1, 9),
    (142854, 1, 10),

    -- FLEURET HOMME U17
    (110775, 1, 1),
    (60894, 1, 2),
    (89901, 1, 3),
    (131989, 1, 4),
    (71856, 1, 5),
    (120674, 1, 6),
    (141359, 1, 7),
    (72695, 1, 8),
    (112716, 1, 9),
    (104342, 1, 10),

    -- FLEURET HOMME U20
    (33, 1, 1),
    (54795, 1, 2),
    (129035, 1, 3),
    (113331, 1, 4),
    (5155, 1, 5),
    (54796, 1, 6),
    (223059, 1, 7),
    (65877, 1, 8),
    (84283, 1, 9),
    (5226, 1, 10),

    -- FLEURET HOMME SENIORS
    (45243, 1, 1),
    (20840, 1, 2),
    (53089, 1, 3),
    (40845, 1, 4),
    (37189, 1, 5),
    (53998, 1, 6),
    (54797, 1, 7),
    (11795, 1, 8),
    (5387, 1, 9),
    (35524, 1, 10),

    -- FLEURET HOMME VETERANS 1
    (5189, 1, 1),
    (10913, 1, 2),
    (560, 1, 3),
    (4405, 1, 4),
    (50233, 1, 5),
    (77126, 1, 6),
    (260817, 1, 7),
    (209993, 1, 8),
    (45939, 1, 9),
    (57025, 1, 10),

    -- SABRE HOMME U15
    (157156, 1, 1),
    (136274, 1, 2),
    (123412, 1, 3),
    (183847, 1, 4),
    (118849, 1, 5),
    (134140, 1, 6),
    (141230, 1, 7),
    (156760, 1, 8),
    (178798, 1, 9),
    (183858, 1, 10),

    -- SABRE HOMME U17
    (62092, 1, 1),
    (161794, 1, 2),
    (67340, 1, 3),
    (128999, 1, 4),
    (157322, 1, 5),
    (86051, 1, 6),
    (190335, 1, 7),
    (209423, 1, 8),
    (113671, 1, 9),
    (92537, 1, 10),

    -- SABRE HOMME U20
    (24526, 1, 1),
    (71950, 1, 2),
    (39689, 1, 3),
    (67708, 1, 4),
    (90728, 1, 5),
    (103888, 1, 6),
    (76530, 1, 7),
    (27867, 1, 8),
    (33726, 1, 9),
    (673401, 1, 10),

    -- SABRE HOMME SENIORS
    (46558, 1, 1),
    (82843, 1, 2),
    (5388, 1, 3),
    (53630, 1, 4),
    (39554, 1, 5),
    (1240, 1, 6),
    (45133, 1, 7),
    (13262, 1, 8),
    (33104, 1, 9),
    (245261, 1, 10),

    -- SABRE HOMME VETERANS 1
    (4032, 1, 1),
    (4029, 1, 2),
    (241387, 1, 3),
    (23563, 1, 4),
    (181398, 1, 5),
    (114645, 1, 6),
    (52892, 1, 7),
    (223600, 1, 8),
    (50032, 1, 9),
    (130002, 1, 10);

-- -- Table ARBITRE
INSERT INTO ARBITRE (numeroLicenceE)
VALUES
    (175387),
    (17545),
    (177583),
    (185987),
    (164751),
    (168928),
    (205331),
    (224542),
    (148250),
    (228366),
    (129212),
    (76700),
    (147282),
    (113544),
    (113759),
    (174028),
    (161090),
    (131480),
    (175451),
    (259042),
    (71982),
    (98466),
    (135870),
    (31330),
    (144492),
    (129588),
    (25072),
    (42935),
    (187363),
    (149821),
    (9918),
    (38480),
    (37514),
    (30369),
    (43182),
    (49657),
    (53830),
    (59316),
    (57866),
    (59193),
    (210895),
    (20166),
    (12231),
    (38334),
    (130778),
    (238600),
    (55799),
    (6658),
    (27812),
    (64584),
    (133478),
    (169221),
    (163749),
    (116048),
    (133493),
    (182444),
    (138405),
    (190486),
    (187370),
    (215767),
    (135555),
    (109958),
    (65718),
    (100420),
    (230041),
    (67982),
    (163748),
    (167483),
    (133479),
    (191353),
    (85977),
    (106336),
    (80966),
    (15432),
    (77431),
    (83032),
    (38749),
    (51037),
    (135556),
    (82742),
    (49227),
    (56061),
    (9456),
    (130899),
    (45139),
    (8799),
    (32498),
    (79731),
    (5982),
    (43387),
    (140691),
    (21121),
    (71384),
    (208782),
    (11005),
    (131194),
    (280152);

-- PARTICIPANTS_COMPETITION
INSERT INTO PARTICIPANTS_COMPETITION (idTireur, idComp)
VALUES
    (1, 1),  -- Compétition 1 avec le tireur 1
    (2, 1),  -- Compétition 1 avec le tireur 2
    (3, 1),  -- Compétition 1 avec le tireur 3
    (4, 1),  -- Compétition 1 avec le tireur 4
    (5, 1),  -- Compétition 1 avec le tireur 5
    (6, 1),  -- Compétition 1 avec le tireur 6
    (7, 1),  -- Compétition 1 avec le tireur 7
    (8, 1),  -- Compétition 1 avec le tireur 8
    (9, 2),  -- Compétition 2 avec le tireur 1
    (10, 2), -- Compétition 2 avec le tireur 2
    (11, 2), -- Compétition 2 avec le tireur 3
    (12, 2), -- Compétition 2 avec le tireur 4
    (13, 2), -- Compétition 2 avec le tireur 5
    (14, 2), -- Compétition 2 avec le tireur 6
    (15, 2), -- Compétition 2 avec le tireur 7
    (16, 2), -- Compétition 2 avec le tireur 8
    (17, 3), -- Compétition 3 avec le tireur 1
    (18, 3), -- Compétition 3 avec le tireur 2
    (19, 3), -- Compétition 3 avec le tireur 3
    (20, 3), -- Compétition 3 avec le tireur 4
    (21, 3), -- Compétition 3 avec le tireur 5
    (22, 3), -- Compétition 3 avec le tireur 6
    (23, 3), -- Compétition 3 avec le tireur 7
    (24, 3), -- Compétition 3 avec le tireur 8
    (25, 4), -- Compétition 4 avec le tireur 1
    (26, 4), -- Compétition 4 avec le tireur 2
    (27, 4), -- Compétition 4 avec le tireur 3
    (28, 4), -- Compétition 4 avec le tireur 4
    (29, 4), -- Compétition 4 avec le tireur 5
    (30, 4), -- Compétition 4 avec le tireur 6
    (31, 4), -- Compétition 4 avec le tireur 7
    (32, 4), -- Compétition 4 avec le tireur 8
    (33, 5), -- Compétition 5 avec le tireur 1
    (34, 5), -- Compétition 5 avec le tireur 2
    (35, 5), -- Compétition 5 avec le tireur 3
    (36, 5), -- Compétition 5 avec le tireur 4
    (37, 5), -- Compétition 5 avec le tireur 5
    (38, 5), -- Compétition 5 avec le tireur 6
    (39, 5), -- Compétition 5 avec le tireur 7
    (40, 5), -- Compétition 5 avec le tireur 8
    (41, 6), -- Compétition 6 avec le tireur 1
    (42, 6), -- Compétition 6 avec le tireur 2
    (43, 6), -- Compétition 6 avec le tireur 3
    (44, 6), -- Compétition 6 avec le tireur 4
    (45, 6), -- Compétition 6 avec le tireur 5
    (46, 6), -- Compétition 6 avec le tireur 6
    (47, 6), -- Compétition 6 avec le tireur 7
    (48, 6), -- Compétition 6 avec le tireur 8
    (49, 7), -- Compétition 7 avec le tireur 1
    (50, 7), -- Compétition 7 avec le tireur 2
    (51, 7), -- Compétition 7 avec le tireur 3
    (52, 7), -- Compétition 7 avec le tireur 4
    (53, 7), -- Compétition 7 avec le tireur 5
    (54, 7), -- Compétition 7 avec le tireur 6
    (55, 7), -- Compétition 7 avec le tireur 7
    (56, 7), -- Compétition 7 avec le tireur 8
    (57, 8), -- Compétition 8 avec le tireur 1
    (58, 8), -- Compétition 8 avec le tireur 2
    (59, 8), -- Compétition 8 avec le tireur 3
    (60, 8); -- Compétition 8 avec le tireur 4


-- Table PRATIQUER_ARME
INSERT INTO PRATIQUER_ARME (numeroLicenceE, idArme)
VALUES
-- EPEE DAMES U15
    (175387, 1),
    (17545, 1),
    (177583, 1),
    (185987, 1),
    (164751, 1),
    (168928, 1),
    (205331, 1),
    (224542, 1),
    (148250, 1),
    (228366, 1),

-- EPEE DAMES U17
    (129212, 1),
    (76700, 1),
    (147282, 1),
    (113544, 1),
    (113759, 1),
    (174028, 1),
    (161090, 1),
    (131480, 1),
    (175451, 1),
    (259042, 1),

-- EPEE DAMES U20
    (71982, 1),
    (98466, 1),
    (135870, 1),
    (31330, 1),
    (144492, 1),
    (129588, 1),
    (25072, 1),
    (42935, 1),
    (187363, 1),
    (149821, 1),

-- EPEE DAMES SENIORS
    (9918, 1),
    (38480, 1),
    (37514, 1),
    (30369, 1),
    (43182, 1),
    (49657, 1),
    (53830, 1),
    (59316, 1),
    (57866, 1),
    (59193, 1),

-- EPEE DAMES VETERANS 1
    (210895, 1),
    (20166, 1),
    (12231, 1),
    (38334, 1),
    (130778, 1),
    (238600, 1),
    (55799, 1),
    (6658, 1),
    (27812, 1),
    (64584, 1),

-- FLEURET DAMES U15
    (133478, 2),
    (169221, 2),
    (163749, 2),
    (116048, 2),
    (133493, 2),
    (182444, 2),
    (138405, 2),
    (190486, 2),
    (187370, 2),
    (215767, 2),

-- FLEURET DAMES U17
    (135555, 2),
    (109958, 2),
    (65718, 2),
    (100420, 2),
    (230041, 2),
    (67982, 2),
    (163748, 2),
    (167483, 2),
    (133479, 2),
    (191353, 2),

-- FLEURET DAMES U20
    (85977, 2),
    (106336, 2),
    (80966, 2),
    (15432, 2),
    (77431, 2),
    (83032, 2),
    (38749, 2),
    (51037, 2),
    (135556, 2),
    (82742, 2),

-- FLEURET DAMES SENIORS
    (49227, 2),
    (56061, 2),
    (9456, 2),
    (130899, 2),
    (45139, 2),
    (8799, 2),
    (32498, 2),
    (79731, 2),
    (5982, 2),
    (43387, 2),

-- FLEURET DAMES VETERANS 1
    (140691, 2),
    (21121, 2),
    (71384, 2),
    (208782, 2),
    (11005, 2),
    (131194, 2),
    (280152, 2),
    (278121, 2),
    (10914, 2),
    (66581, 2),

-- SABRE DAMES U15
    (132102, 3),
    (133470, 3),
    (149504, 3),
    (159059, 3),
    (116121, 3),
    (190876, 3),
    (162846, 3),
    (144957, 3),
    (293460, 3),
    (176510, 3),

-- SABRE DAMES U17
    (122357, 3),
    (156496, 3),
    (68547, 3),
    (143110, 3),
    (158514, 3),
    (133317, 3),
    (179739, 3),
    (178914, 3),
    (62604, 3),
    (133383, 3),

-- SABRE DAMES U20
    (112853, 3),
    (98376, 3),
    (65868, 3),
    (93138, 3),
    (181629, 3),
    (39305, 3),
    (155264, 3),
    (25795, 3),
    (105462, 3),
    (133399, 3),

-- SABRE DAMES SENIORS
    (2628, 3),
    (48804, 3),
    (50341, 3),
    (9036, 3),
    (66675, 3),
    (1054621, 3),
    (48067, 3),
    (4471, 3),
    (59330, 3),
    (37788, 3),

-- SABRE DAMES VETERANS 1
    (16205, 3),
    (713841, 3),
    (140901, 3),
    (213778, 3),
    (266339, 3),
    (6455, 3),
    (50031, 3),
    (23635, 3),
    (148227, 3),
    (262801, 3),

-- EPEE HOMME U15
    (130253, 1),
    (137222, 1),
    (107947, 1),
    (166382, 1),
    (118007, 1),
    (134485, 1),
    (173851, 1),
    (120367, 1),
    (221192, 1),
    (130475, 1),

-- EPEE HOMME U17
    (90309, 1),
    (222879, 1),
    (169495, 1),
    (118182, 1),
    (61872, 1),
    (106151, 1),
    (279693, 1),
    (61885, 1),
    (257151, 1),
    (161048, 1),

-- EPEE HOMME U20
    (165239, 1),
    (94004, 1),
    (17597, 1),
    (90018, 1),
    (112647, 1),
    (17604, 1),
    (90019, 1),
    (99410, 1),
    (282196, 1),
    (90020, 1),

-- EPEE HOMME SENIORS
    (117880, 1),
    (19208, 1),
    (80814, 1),
    (210708, 1),
    (106789, 1),
    (162029, 1),
    (156636, 1),
    (125678, 1),
    (157453, 1),
    (173822, 1),

-- EPEE HOMME VÉTÉRANS 1
    (27470, 1),
    (18978, 1),
    (14396, 1),
    (24113, 1),
    (14382, 1),
    (19774, 1),
    (13729, 1),
    (14078, 1),
    (25083, 1),
    (21772, 1),

    -- FLEURET HOMME U15
    (204893, 1),
    (130121, 1),
    (147259, 1),
    (185282, 1),
    (128872, 1),
    (142651, 1),
    (129422, 1),
    (127775, 1),
    (213592, 1),
    (142854, 1),

    -- FLEURET HOMME U17
    (110775, 1),
    (60894, 1),
    (89901, 1),
    (131989, 1),
    (71856, 1),
    (120674, 1),
    (141359, 1),
    (72695, 1),
    (112716, 1),
    (104342, 1),

    -- FLEURET HOMME U20
    (33, 1),
    (54795, 1),
    (129035, 1),
    (113331, 1),
    (5155, 1),
    (54796, 1),
    (223059, 1),
    (65877, 1),
    (84283, 1),
    (5226, 1),

    -- FLEURET HOMME SENIORS
    (45243, 1),
    (20840, 1),
    (53089, 1),
    (40845, 1),
    (37189, 1),
    (53998, 1),
    (54797, 1),
    (11795, 1),
    (5387, 1),
    (35524, 1),

    -- FLEURET HOMME VETERANS 1
    (5189, 1),
    (10913, 1),
    (560, 1),
    (4405, 1),
    (50233, 1),
    (77126, 1),
    (260817, 1),
    (209993, 1),
    (45939, 1),
    (57025, 1),

    -- SABRE HOMME U15
    (157156, 1),
    (136274, 1),
    (123412, 1),
    (183847, 1),
    (118849, 1),
    (134140, 1),
    (141230, 1),
    (156760, 1),
    (178798, 1),
    (183858, 1),

    -- SABRE HOMME U17
    (62092, 1),
    (161794, 1),
    (67340, 1),
    (128999, 1),
    (157322, 1),
    (86051, 1),
    (190335, 1),
    (209423, 1),
    (113671, 1),
    (92537, 1),

    -- SABRE HOMME U20
    (24526, 1),
    (71950, 1),
    (39689, 1),
    (67708, 1),
    (90728, 1),
    (103888, 1),
    (76530, 1),
    (27867, 1),
    (33726, 1),
    (673401, 1),

    -- SABRE HOMME SENIORS
    (46558, 1),
    (82843, 1),
    (5388, 1),
    (53630, 1),
    (39554, 1),
    (1240, 1),
    (45133, 1),
    (13262, 1),
    (33104, 1),
    (245261, 1),

    -- SABRE HOMME VETERANS 1
    (4032, 1),
    (4029, 1),
    (241387, 1),
    (23563, 1),
    (181398, 1),
    (114645, 1),
    (52892, 1),
    (223600, 1),
    (50032, 1),
    (130002, 1);
    
-- test escrimeurs pratiquer plusieurs armes
INSERT INTO PRATIQUER_ARME (numeroLicenceE, idArme)
VALUES
    -- EPEE DAMES U15
    (175387, 2),
    (17545, 2),
    (177583, 2),
    (185987, 2),
    (164751, 2),
    (168928, 2),
    (205331, 2),
    (224542, 2),
    (148250, 2),
    (228366, 2),

-- EPEE DAMES U17
    (129212, 2),
    (76700, 2),
    (147282, 2),
    (113544, 2),
    (113759, 2),
    (174028, 2),
    (161090, 2),
    (131480, 2),
    (175451, 2),
    (259042, 2),

-- EPEE DAMES U20
    (71982, 2),
    (98466, 2),
    (135870, 2),
    (31330, 2),
    (144492, 2),
    (129588, 2),
    (25072, 2),
    (42935, 2),
    (187363, 2),
    (149821, 2),

-- EPEE DAMES SENIORS
    (9918, 2),
    (38480, 2),
    (37514, 2),
    (30369, 2),
    (43182, 2),
    (49657, 2),
    (53830, 2),
    (59316, 2),
    (57866, 2),
    (59193, 2),

-- EPEE DAMES VETERANS 1
    (210895, 2),
    (20166, 2),
    (12231, 2),
    (38334, 2),
    (130778, 2),
    (238600, 2),
    (55799, 2),
    (6658, 2),
    (27812, 2),
    (64584, 2);

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
    (1, 1, 1, 1, 1, 8, '2024-04-15', '10:00:00', 0, 0, 0, 0),
    (1, 1, 1, 1, 2, 7, '2024-04-15', '10:30:00', 0, 0, 0, 0),
    (1, 1, 1, 1, 3, 6, '2024-04-15', '11:00:00', 0, 0, 0, 0),
    (1, 1, 1, 1, 4, 5, '2024-04-15', '11:30:00', 0, 0, 0, 0),

    (1, 2, 2, 2, 9, 16, '2024-04-15', '12:00:00', null, null, null, null),
    (1, 2, 2, 2, 10, 15, '2024-04-15', '12:30:00', null, null, null, null),
    (1, 2, 2, 2, 11, 14, '2024-04-15', '13:00:00', null, null, null, null),
    (1, 2, 2, 2, 12, 13, '2024-04-15', '13:30:00', null, null, null, null),

    (1, 3, 3, 3, 17, 24, '2024-04-15', '14:00:00', 0, 0, 0, 0),
    (1, 3, 3, 3, 18, 23, '2024-04-15', '14:30:00', 0, 0, 0, 0),
    (1, 3, 3, 3, 19, 22, '2024-04-15', '15:00:00', 0, 0, 0, 0),
    (1, 3, 3, 3, 20, 21, '2024-04-15', '15:30:00', 0, 0, 0, 0),

    (1, 4, 4, 4, 25, 32, '2024-04-15', '16:00:00', 0, 0, 0, 0),
    (1, 4, 4, 4, 26, 31, '2024-04-15', '16:30:00', 0, 0, 0, 0),
    (1, 4, 4, 4, 27, 30, '2024-04-15', '17:00:00', 0, 0, 0, 0),
    (1, 4, 4, 4, 28, 29, '2024-04-15', '17:30:00', 0, 0, 0, 0);


-- Table FEUILLE_MATCH
INSERT INTO FEUILLE_MATCH (idPoule, idComp, idTireur1, idTireur2, scoreTireur1, scoreTireur2)
VALUES
    (1, 1, 1, 8, null, null),
    (1, 1, 2, 7, null, null),
    (1, 1, 3, 6, null, null),
    (1, 1, 4, 5, null, null),

    (1, 2, 9, 16, null, null),
    (1, 2, 10, 15, null, null),
    (1, 2, 11, 14, null, null),
    (1, 2, 12, 13, null, null),

    (1, 3, 17, 24, null, null),
    (1, 3, 18, 23, null, null),
    (1, 3, 19, 22, null, null),
    (1, 3, 20, 21, null, null),

    (1, 4, 25, 32, null, null),
    (1, 4, 26, 31, null, null),
    (1, 4, 27, 30, null, null),
    (1, 4, 28, 29, null, null);