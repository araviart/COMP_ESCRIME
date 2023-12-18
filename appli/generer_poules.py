class Lieu:
    def __init__(self, nomLieu, villeLieu, codePostalLieu, adresseLieu):
        self.nomLieu = nomLieu
        self.villeLieu = villeLieu
        self.codePostalLieu = codePostalLieu
        self.adresseLieu = adresseLieu

class Arme:
    def __init__(self, nomArme):
        self.nomArme = nomArme

class Saison:
    def __init__(self, nomSaison, dateDebutSaison, dateFinSaison):
        self.nomSaison = nomSaison
        self.dateDebutSaison = dateDebutSaison
        self.dateFinSaison = dateFinSaison

class Categorie:
    def __init__(self, nomCategorie):
        self.nomCategorie = nomCategorie

class Club:
    def __init__(self, nomClub, villeClub):
        self.nomClub = nomClub
        self.villeClub = villeClub

class Competition:
    def __init__(self, idLieu, idSaison, idCat, idArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle):
        self.idLieu = idLieu
        self.idSaison = idSaison
        self.idCat = idCat
        self.idArme = idArme
        self.nomComp = nomComp
        self.descComp = descComp
        self.dateComp = dateComp
        self.heureComp = heureComp
        self.sexeComp = sexeComp
        self.estIndividuelle = estIndividuelle

class Piste:
    def __init__(self, idComp, nomPiste, estDispo):
        self.idComp = idComp
        self.nomPiste = nomPiste
        self.estDispo = estDispo

class TypeMatch:
    def __init__(self, nomTypeMatch, nbTouches):
        self.nomTypeMatch = nomTypeMatch
        self.nbTouches = nbTouches

class Escrimeur:
    def __init__(self, idCat, prenomE, nomE, dateNaissanceE, numeroLicenceE, sexeE, numTelE):
        self.idCat = idCat
        self.prenomE = prenomE
        self.nomE = nomE
        self.dateNaissanceE = dateNaissanceE
        self.numeroLicenceE = numeroLicenceE
        self.sexeE = sexeE
        self.numTelE = numTelE

class Tireur:
    def __init__(self, idClub, classement):
        self.idClub = idClub
        self.classement = classement
    def get_idClub(self):
        return self.idClub
    def get_classement(self):
        return self.classement
    def __repr__(self):
        return f"(Club: {self.idClub}, Classement: {self.classement})"

class Arbitre:
    def __init__(self, idArbitre):
        self.idArbitre = idArbitre

class PratiquerArme:
    def __init__(self, idEscrimeur, idArme):
        self.idEscrimeur = idEscrimeur
        self.idArme = idArme

class ClassementFinal:
    def __init__(self, idComp, idTireur, position):
        self.idComp = idComp
        self.idTireur = idTireur
        self.position = position

class Poule:
    def __init__(self, idComp, idPiste, idArbitre, nomPoule):
        self.idComp = idComp
        self.idPiste = idPiste
        self.idArbitre = idArbitre
        self.nomPoule = nomPoule

class ParticipantsPoule:
    def __init__(self, idPoule, idTireur):
        self.idPoule = idPoule
        self.idTireur = idTireur

class MatchPoule:
    def __init__(self, idTypeMatch, idPoule, idPiste, idArbitre, idTireur1, idTireur2, dateMatch, heureMatch, touchesRecuesTireur1, touchesDonneesTireur1, touchesRecuesTireur2, touchesDonneesTireur2):
        self.idTypeMatch = idTypeMatch
        self.idPoule = idPoule
        self.idPiste = idPiste
        self.idArbitre = idArbitre
        self.idTireur1 = idTireur1
        self.idTireur2 = idTireur2
        self.dateMatch = dateMatch
        self.heureMatch = heureMatch
        self.touchesRecuesTireur1 = touchesRecuesTireur1
        self.touchesDonneesTireur1 = touchesDonneesTireur1
        self.touchesRecuesTireur2 = touchesRecuesTireur2
        self.touchesDonneesTireur2 = touchesDonneesTireur2

class FeuilleMatch:
    def __init__(self, idPoule, idComp, idTireur1, idTireur2, scoreTireur1, scoreTireur2):
        self.idPoule = idPoule
        self.idComp = idComp
        self.idTireur1 = idTireur1
        self.idTireur2 = idTireur2
        self.scoreTireur1 = scoreTireur1
        self.scoreTireur2 = scoreTireur2

arme = Arme("Fleuret")
arbitre1 = Arbitre(1)
arbitre2 = Arbitre(2)
arbitre3 = Arbitre(3)
arbitre4 = Arbitre(4)
lieu = Lieu("Gymnase", "Paris", 75000, "Rue de Paris")
saison = Saison("Saison 1", "01/09/2020", "31/08/2021")
categorie = Categorie("Cadet")
club = Club("Club 1", "Paris")
piste = Piste(1, "Piste 1", True)
typeMatch = TypeMatch("Poule", 5)
tireur1 = Tireur(1, 1000)
tireur2 = Tireur(1, 1287)
tireur3 = Tireur(1, 1200)
tireur4 = Tireur(1, 1350)
tireur5 = Tireur(2, 897)
tireur6 = Tireur(2, 900)
tireur7 = Tireur(3, 700)
tireur8 = Tireur(3, 698)
tireur9 = Tireur(3, 650)
tireur10 = Tireur(5, 1111)
tireur11 = Tireur(6, 1900)
tireur12 = Tireur(5, 2000)
tireur13 = Tireur(5, 2340)
tireur14 = Tireur(4, 1548)
tireur15 = Tireur(4, 1589)
tireur16 = Tireur(4, 1676)
tireur17 = Tireur(6, 1290)
competition = Competition(1, 1, 1, 1, "Competition 1", "Description 1", "01/01/2021", "10:00", "M", True)

les_tireurs = [tireur1, tireur2, tireur3, tireur4, tireur5, tireur6, tireur7, tireur8, tireur9, tireur10, tireur11, tireur12, tireur13, tireur14, tireur15, tireur16, tireur17]
les_arbitres = [arbitre1, arbitre2, arbitre3, arbitre4]

def classer_tireurs(tireurs):
    return sorted(tireurs, key=lambda tireur: tireur.get_classement(), reverse=True)


def poules_fabriquables(tireurs, arbitres):
    return True if 3 <= len(tireurs) // len(arbitres) <= 7 and len(tireurs) > 3 else False


def nb_poules_fabriquables(arbitres):
    return [[] for _ in range(len(arbitres))]


def fabriquer_poules_selon_classement(tireurs, arbitres):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"
    liste_triee = classer_tireurs(tireurs)
    liste_poules = nb_poules_fabriquables(arbitres)
    tireurs_dans_poule = set()
    for i in range(len(liste_triee)):
        if liste_triee[i] not in tireurs_dans_poule:
            if len(liste_poules[i % len(arbitres)]) < 7:
                liste_poules[i % len(arbitres)].append(liste_triee[i])
                tireurs_dans_poule.add(liste_triee[i])
        if liste_triee[-i-1] not in tireurs_dans_poule:
            if len(liste_poules[i % len(arbitres)]) < 7:
                liste_poules[i % len(arbitres)].append(liste_triee[-i-1])
                tireurs_dans_poule.add(liste_triee[-i-1])    
    return liste_poules

def fabriquer_poules_decalage_club(tireurs, arbitres):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"
    liste_triee = classer_tireurs(tireurs)
    liste_poules = nb_poules_fabriquables(arbitres)
    num_poule = 0
    for i in range(len(liste_triee)):
        if len(liste_poules[i % len(arbitres)]) < 7:
            if liste_triee[i].get_idClub() not in liste_poules[i % len(arbitres)]:
                liste_poules[i % len(arbitres)].append(liste_triee[i])
            else:
                num_poule += 1
                if num_poule % len(arbitres) == 0:
                    liste_poules[i % len(arbitres)].append(liste_triee[i])
                    num_poule = 0
                else:
                    liste_poules[i % len(arbitres) + num_poule].append(liste_triee[i])
    return liste_poules
    

def fabriquer_poules(tireurs, arbitres, type_poule):
    if not poules_fabriquables(tireurs, arbitres):
        return "Les poules ne sont pas fabriquables"
    match type_poule:
        case "Classement":
            liste_poules = fabriquer_poules_selon_classement(tireurs, arbitres)
        case "Club":
            liste_poules = fabriquer_poules_decalage_club(tireurs, arbitres)
    for i in range(len(liste_poules)):
        print(f"Poule {i+1}: {liste_poules[i]}")
    return liste_poules

fabriquer_poules(les_tireurs, les_arbitres, "Classement")