import datetime
import random
from .app import app, db, mail
import logging
import math
from .ajout_bd import creer_competition
from flask import jsonify, render_template, session, url_for, redirect, request, flash
from .models import Arme, Categorie, Competition, Lieu, MatchPoule, ParticipantsCompetition, Saison, Tireur, User, classer_tireurs, fabriquer_poules, get_arbitre_escrimeur_poule, get_club_tireur_escrimeur, get_id_arbitre_poule, get_lieux, get_liste_participants_competitions_arbitres, get_liste_participants_competitions_tireurs, get_liste_tireurs_escrimeurs_poule, get_nb_arbitres, get_nb_poules, get_nb_tireurs, get_participants, get_piste_poule, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions, get_adherents, filtrer_adherent, Escrimeur, dernier_escrimeur_id, poules_fabriquables
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField
from hashlib import sha256
from flask_login import login_user, logout_user, current_user
from flask_mail import Message

def send_verification_email(user_email, code):
    with app.app_context():
        msg = Message("Votre code de vérification", recipients=[user_email])
        msg.body = f"Votre code de vérification est : {code}"
        mail.send(msg)

def send_bienvenue_email(user_email, user_pseudo):
    with app.app_context():
        msg = Message("Bienvenue sur COMPETITION ESCRIME", recipients=[user_email])
        msg.body = f"Bonjour {user_pseudo},\n\nBienvenue sur COMPETITION ESCRIME !\n\nNous vous souhaitons une bonne navigation sur notre site.\n\nL'équipe COMPETITION ESCRIME"
        mail.send(msg)

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
class LoginForm(FlaskForm):
    email_username = StringField('email_username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def get_authenticated_user(self):
        user = User.query.filter_by(emailUser=self.email_username.data).first()
        if user is None:
            user = User.query.filter_by(pseudoUser=self.email_username.data).first()
            if user is None:
                return None
        m = sha256 ()
        m.update(self.password.data.encode ())
        passwd = m. hexdigest ()
        return user if passwd == user.mdpUser else None
    
class InscriptionForm(FlaskForm):
    pseudo = StringField('pseudo', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    comfirm_password = PasswordField('comfirm_password', validators=[DataRequired()])

class EditUserForm(FlaskForm):
    newpsswd = PasswordField("Nouveau mot de passe")
    confirm = PasswordField("Confirmez le nouveau mot de passe")
    username = StringField("Pseudonyme actuelle")
    password = PasswordField("Mot de passe actuelle")


@app.route("/gestion_score/<int:id_comp>")
def gestion_score(id_comp):

    # récuperer les infos des poules dans un dict avec le numéro de poule en clé et la liste des tireurs,le nom de la piste, le nom de l'arbitre en valeur
    poules = {}
    nb_poules = get_nb_poules(id_comp)
    for i in range(1, nb_poules+1):
        poules[i] = {}
        tireurs_club = {} # dict avec le tireur en clé et le nom du club en valeur
        for tireur in get_liste_tireurs_escrimeurs_poule(id_comp, i):
            tireurs_club[tireur] = get_club_tireur_escrimeur(tireur).nomClub
        poules[i]['tireurs'] = tireurs_club
        poules[i]['piste'] = get_piste_poule(id_comp, i)
        poules[i]["id_arbitre"] = get_id_arbitre_poule(id_comp, i)
        poules[i]['arbitre'] = get_arbitre_escrimeur_poule(id_comp, i).nomE + " " + get_arbitre_escrimeur_poule(id_comp, i).prenomE
    # Rendre le modèle HTML avec Flask
    return render_template('gestion_score.html', poules=poules, id_comp=id_comp)

@app.route('/update_scores', methods=['POST'])
def update_scores():
    data = request.get_json()

    license = data['license']
    opponent_license = data['opponentLicense']
    score = data['score']
    id_poule = data['idPoule']
    id_piste = data['idPiste']
    id_comp = data['idCompetition']
    id_arbitre = data['idArbitre']



    print("license: ", license , "opponent_license: ", opponent_license, "score: ", score, "id_poule: ", id_poule, "id_piste: ", id_piste, "id_comp: ", id_comp, "id_arbitre: ", id_arbitre)

    match = MatchPoule.query.filter_by(numeroLicenceE1=license, numeroLicenceE2=opponent_license).first()
    match2 = MatchPoule.query.filter_by(numeroLicenceE1=opponent_license, numeroLicenceE2=license).first()

    if match or match2:
        print("Match trouvé")
    else:
        # créer le match
        print("Création du match")
        match = MatchPoule(type_match=1, poule=id_poule, piste=id_piste, arbitre=id_arbitre,
                            tireur1=license, tireur2=opponent_license,
                            date_match=datetime.date.today(), heure_match=datetime.datetime.now().time().strftime("%H:%M:%S"),
                            touches_recues_tireur1=0, touches_donnees_tireur1=score,
                            touches_recues_tireur2=score, touches_donnees_tireur2=0)
        db.session.add(match)
        db.session.commit()
        print("Match créé")

    return 'OK'
    
@app.route("/appel/")
def appel():
    # Exemple de données à afficher dans chaque ligne
    rows_data = [
        {'Nom': 'Doe', 'Prenom': 'John', 'DateNaissance': '01/01/1990', 'Telephone': '123456789', 'Sexe': 'M', 'Club': 'Club A', 'Classement': 'A'},
        {'Nom': 'Smith', 'Prenom': 'Alice', 'DateNaissance': '02/02/1995', 'Telephone': '987654321', 'Sexe': 'F', 'Club': 'Club B', 'Classement': 'B'},
        {'Nom': 'Johnson', 'Prenom': 'Bob', 'DateNaissance': '03/03/1992', 'Telephone': '555555555', 'Sexe': 'M', 'Club': 'Club C', 'Classement': 'C'},
        {'Nom': 'Williams', 'Prenom': 'Emma', 'DateNaissance': '04/04/1988', 'Telephone': '111111111', 'Sexe': 'F', 'Club': 'Club D', 'Classement': 'D'}
    ]

    return render_template('appel.html', rows_data=rows_data)

@app.route("/inscription-form/")
def inscription_page():
    return render_template("Inscription.html", form = InscriptionForm())

@app.route("/inscription/", methods=["GET", "POST"])
def inscription():
    f = InscriptionForm()
    if(User.query.filter_by(pseudoUser=f.pseudo.data).first() is not None or User.query.filter_by(emailUser=f.email.data).first() is not None or f.password.data != f.comfirm_password.data):
        if(User.query.filter_by(pseudoUser=f.pseudo.data).first() is not None):
            flash("Pseudo déjà utilisé", "error")
        if(User.query.filter_by(emailUser=f.email.data).first() is not None):
            flash("Email déjà utilisé", "error")
        if(f.password.data != f.comfirm_password.data):
            flash("Les mots de passe ne correspondent pas", "error")
        return render_template("Inscription.html", form=f)
    else:
        m = sha256()
        m.update(f.password.data.encode())
        u = User(pseudoUser=f.pseudo.data , mdpUser=m.hexdigest(), emailUser=f.email.data)
        db.session.add(u)
        db.session.commit()
        send_bienvenue_email(f.email.data, f.pseudo.data)
        return redirect(url_for("home"))

@app.route("/login/", methods=["GET", "POST"])
def login():
    f = LoginForm()
    user = f.get_authenticated_user()
    if user:
        login_user(user)
        return redirect(url_for("home_default"))
    else:
        flash("Mot de passe incorrect", "error")
    return render_template("Login.html", form=f)

@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route('/home/<int:items>', methods=("GET","POST",))
def home_def(items):
    total_pages = 0
    if request.method == "POST":
        page = int(request.form.get('page', 1))
        if 'next' in request.form:
            page += 1
        elif 'prev' in request.form:
            page -= 1
        # récupere les selection du from
        session['categorie'] = request.form.get('categorie')
        session['arme'] = request.form.get('arme')
        session['sexe'] = request.form.get('sexe')
        session['statut'] = request.form.get('statut')
    else:
        page = request.args.get('page', 1, type=int)
        session['categorie'] = request.args.get('categorie', session.get('categorie'))
        session['arme'] = request.args.get('arme', session.get('arme'))
        session['sexe'] = request.args.get('sexe', session.get('sexe'))
        session['statut'] = request.args.get('statut', session.get('statut'))
    competitions = get_sample()
    categories = get_categories()
    armes = get_armes()
    nb_participants = {comp.idComp: get_nb_participants(comp.idComp) for comp in competitions}
    # filtre pour les compet
    compet_filtre = filtrer_competitions(competitions, session.get('categorie'), session.get('arme'), session.get('sexe'), session.get('statut'))
    if len(compet_filtre) !=0:
        total_pages = math.ceil(len(compet_filtre) / items)
        competitions = compet_filtre[(page - 1) * items:page * items]
    else:
        competitions = []
    return render_template(
        "competition.html",
        title="Compétitions ESCRIME",
        competitions=competitions, 
        categories=categories,
        armes=armes,
        nb_participants=nb_participants,
        items=items,
        selec_arme=session.get('arme'),
        selec_categorie=session.get('categorie'),
        selec_sexe=session.get('sexe'),
        selec_statut=session.get('statut'),
        page=page,
        compet_filtre = compet_filtre,
        total_pages=total_pages
    )
    
@app.route('/liste-adherent/<int:items>', methods=["GET", "POST"])
def liste_adherents(items):
    total_pages = 0
    if request.method == "POST":
        page = int(request.form.get('page', 1))
        if 'next' in request.form:
            page += 1
        elif 'prev' in request.form:
            page -= 1
    else:
        page = request.args.get('page', 1, type=int)
    adherents = get_adherents()
    categories = get_categories()
    role = request.form.get('statut', session.get('statuta', ''))
    categorie = request.form.get('categorie', session.get('categoriea', ''))
    sexe = request.form.get('sexe', session.get('sexea', ''))
    
    adherents = filtrer_adherent(adherents, categorie, sexe)
    if request.method == "POST":
        search_query = request.form.get('search')
        # recherche les adhérents en fonction du nom ou prénom
        if search_query:
            adherents = [adherent for adherent in adherents if search_query.lower() in adherent.Escrimeur.prenomE.lower() or search_query.lower() in adherent.Escrimeur.nomE.lower() or search_query.lower() in str(adherent.Escrimeur.numeroLicenceE)]            
    session['statuta'] = role
    session['categoriea'] = categorie
    session['sexea'] = sexe 
    if len(adherents) !=0:
        total_pages = math.ceil(len(adherents) / items)
        adherents = adherents[(page - 1) * items:page * items]
    else:
        adherents = []

    
    return render_template(
        "liste-adherents.html",
        title="Compétitions ESCRIME",
        categories=categories,
        selec_categorie=categorie,
        selec_sexe=sexe,
        selec_statut=role,
        adherents=adherents,
        items=items,
        page=page,
        total_pages=total_pages)

@app.route('/home/')
def home_default():
    return home_def(5)

    
@app.route('/annuler_comp', methods=['POST'])
def annuler_comp():
    # Rediriger vers l'URL d'origine
    return redirect(request.referrer or url_for('home_default'))

@app.route("/test_popup/")
def test_popup():
    return render_template(
        "test_popup.html",
        title="Test")

@app.route("/edit-user/<name>", methods=("GET","POST",))
def edit_user(name):
    form = EditUserForm()
    if not current_user.is_authenticated:
        next = "edit_user"
        return redirect(url_for("login", next=next))

    if form.validate_on_submit():
        print("Formulaire valide")
        user = current_user
        if user.pseudoUser != form.username.data:
            form.username.errors.append("Pseudonyme erreur")
            return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)

        if form.newpsswd.data != form.confirm.data:
            form.confirm.errors.append("Les mots de passe ne correspondent pas")
            return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)
        
        code = str(random.randint(1000, 9999))
        print(code)
        print(user.emailUser)
        send_verification_email(user.emailUser, code)
        print("Email envoyé")
        session['verification_code'] = code  # Stocker le code temporairement
        session['user_id'] = user.idUser
        session['new_password'] = form.newpsswd.data  # Stocker le nouveau mot de passe temporairement
        print("affichage popup")
        return render_template("edit-user.html", form=form, name=name, show_verification_popup=True)

    return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)

@app.route("/arbre-competition")
def arbre():
    return render_template("arbre.html")

@app.route("/verify-code/<name>", methods=["GET", "POST"])
def verify_code(name):
    if request.method == "POST":
        user_code = request.form['code']
        print(user_code)
        if user_code == session.get('verification_code'):
            # Récupérer l'utilisateur et les informations nécessaires
            user = User.query.get(session.get('user_id'))
            if not user:
                return "Utilisateur non trouvé", 404

            # Procéder à la mise à jour du mot de passe
            new_password = session.get('new_password')
            new_password_hash = sha256()
            new_password_hash.update(new_password.encode())

            user.mdpUser = new_password_hash.hexdigest()
            db.session.commit()

            # Nettoyer la session
            del session['verification_code']
            del session['user_id']
            del session['new_password']

            return redirect(url_for("home")) # "Mot de passe mis à jour avec succès!"
        else:
            flash("Code de vérification incorrect", "error")

    return render_template("edit-user.html", name=name, form=EditUserForm(), show_verification_popup=True)

@app.route('/ajouter_escrimeur/', methods=['GET', 'POST'])
def ajouter_escrimeur():
    if request.method == 'POST':
        id = dernier_escrimeur_id() + 1
        print(id)

        #recup donnees du formulaire
        nom = request.form['nom_e']
        print(nom)
        prenom = request.form['prenom_e']
        print(prenom)
        date_naissance = request.form['date_naissance_e']
        print(date_naissance)
        numero_licence = request.form['numero_licence_e']
        numero_licence = int(numero_licence)
        print(numero_licence)

        # sexe = request.form['sexe_e']
        sexe = 'H'
        print(sexe)
        # num_tel = request.form['num_tel_e']
        num_tel = '0648572519'
        print(num_tel)
        default_cat = 1
        
        # creez un nouvel enregistrement d'adherent
        nouvel_adherent = Escrimeur(idEscrimeur=id, idCat=default_cat, prenomE=prenom, 
                                nomE=nom, dateNaissanceE=date_naissance, 
                                numeroLicenceE=numero_licence, sexeE=sexe, numTelE=num_tel)
        db.session.add(nouvel_adherent)
        db.session.commit()
        return redirect(url_for('liste_adherents_def'))
      
@app.route('/')
def home():
    return render_template('Login.html')

@app.route('/gestion_poules/<int:id_comp>', methods=["GET", "POST"])
def gestion_poules(id_comp):
    liste_poules = []
    nb_tireurs = get_nb_tireurs(id_comp)
    nb_arbitres = get_nb_arbitres(id_comp)
    nb_tireurs_par_poule = nb_tireurs // nb_arbitres
    if request.method == "POST":
        classement_checked = 'classement' in request.form
        club_checked = 'club' in request.form
        equilibrer_checked = 'equilibrer' in request.form
        nb_poules = int(request.form.get('nb_poules'))
        nb_tireurs_poules = int(request.form.get('nb_tireurs/poules'))
        liste_tireurs = get_liste_participants_competitions_tireurs(id_comp)
        liste_arbitres = get_liste_participants_competitions_arbitres(id_comp)
        nb_tireurs_par_poule = nb_tireurs // nb_arbitres
        if classement_checked:
            liste_tireurs = classer_tireurs(liste_tireurs)
            if poules_fabriquables(liste_tireurs, liste_arbitres):
                liste_poules = fabriquer_poules(liste_tireurs, liste_arbitres, "Classement")
        elif club_checked:
            if poules_fabriquables(liste_tireurs, liste_arbitres):
                liste_poules = fabriquer_poules(liste_tireurs, liste_arbitres, "Club")
        return render_template('gestion_poules.html', id_comp=id_comp, nb_tireurs=get_nb_tireurs(id_comp), nb_arbitres=get_nb_arbitres(id_comp), liste_tireurs=liste_tireurs, liste_arbitres=liste_arbitres, liste_poules=liste_poules, nb_tireurs_par_poule=nb_tireurs_par_poule)
    liste_tireurs = get_liste_participants_competitions_tireurs(id_comp)
    liste_arbitres = get_liste_participants_competitions_arbitres(id_comp)
    competition = Competition.query.get(id_comp)
    
    if competition is not None:
        return render_template('gestion_poules.html', id_comp=id_comp, nb_tireurs=nb_tireurs, nb_arbitres=nb_arbitres, liste_tireurs=liste_tireurs, liste_arbitres=liste_arbitres, liste_poules=liste_poules, nb_tireurs_par_poule=nb_tireurs_par_poule)

@app.route('/adherent/')
def liste_adherents_def():
    return liste_adherents(5)
  

@app.route("/ajout-comp")
def ajout_comp_page():
    armes = get_armes()
    categories = get_categories()
    lieux = get_lieux()
    types = ["Individuelle", "Equipe"]
    return render_template("ajout-comp.html", listeArmes=armes, listeCategories=categories, listeTypeMatch=types, lieux=lieux)

@app.route('/ajout-comp/', methods=['POST'])
def ajout_comp():
    # Récupérez les données du formulaire
    nomLieu = request.form.get('nomLieu')
    adresseLieu = request.form.get('adresseLieu')
    villeLieu = request.form.get('villeLieu')
    cpLieu = request.form.get('codePostalLieu')
    nomSaison = "Saison 2023"  # Supposons que c'est fixe pour cet exemple
    nomCat = request.form.get('categorie')  # Assurez-vous que le nom correspond au champ dans le HTML
    nomArme = request.form.get('arme')  # Idem
    nomComp = request.form.get('titre')
    nomOrga = request.form.get('organisateur')
    descComp = f"Competition {nomComp} organisée par {nomOrga}" # Ajoutez un champ pour la description si nécessaire
    dateComp = request.form.get('date-deroulement')
    heureComp = request.form.get('appt')
    sexeComp = request.form.get('sexe')[:1].upper()
    estIndividuelle = request.form.get('type') == 'Individuelle'
    print(nomLieu,adresseLieu,villeLieu,cpLieu, nomSaison, nomCat, nomArme, nomComp, nomOrga, descComp, dateComp, heureComp, sexeComp, estIndividuelle)

    # Appeler la fonction pour créer la compétition
    resultat = creer_competition(nomLieu,adresseLieu,villeLieu,cpLieu, nomSaison, nomCat, nomArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle)
    print(resultat)
    # Gérer le résultat (par exemple, afficher un message à l'utilisateur)
    if 'succès' in resultat:
        # Redirige vers une page de confirmation ou la liste des compétitions
        return redirect(url_for('home_default'))
    else:
        # Gérer l'erreur (par exemple, afficher un message d'erreur sur la page actuelle)
        flash(resultat, 'error')
        return redirect(url_for('ajout_comp_page'))

@app.route("/gestion_participants/<int:id_comp>", methods=("GET", "POST"))
def gestion_participants(id_comp):
    competition = Competition.query.get(id_comp)
    participants_blois = get_participants(id_comp, club="ClubBlois")
    participants_other = get_participants(id_comp, club="!")
    nb_participants_blois = len(participants_blois)
    nb_participants_other = len(participants_other)
    
    return render_template(
      "gestion-participants.html",
      title="Gestion des participants",
      participants_blois=participants_blois,
      nb_participants_blois=nb_participants_blois,
      participants_other=participants_other,
      nb_participants_other=nb_participants_other,
      competition=competition
  )
    

@app.route('/delete_participant/<int:id_comp>/<int:id>/', methods=['POST'])
def delete_participant(id, id_comp):
    participant = ParticipantsCompetition.query.filter_by(idTireur=id).first()

    if participant:
        db.session.delete(participant)
        db.session.commit()
    return redirect(url_for('gestion_participants', id_comp=id_comp))

import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

@app.route('/ajouter_escrimeur_competition/<int:id_comp>/', methods=['POST'])
def add_participant(id_comp):
    if request.method == 'POST':
        tireur = request.get_json().get('idTireur')
        logging.debug(f'id_tireur: {tireur}')
        
        tireur = Tireur.query.get(tireur)
        
        logging.debug(f'tireur: {tireur}')

        competition = Competition.query.get(id_comp)
        logging.debug(f'competition: {competition}')
        getattr(competition, "idComp", None)
        if tireur and competition:
            participant = ParticipantsCompetition(idTireur=getattr(tireur, "idTireur", None), idComp=getattr(competition, "idComp", None))
            logging.debug('creation participant')
            db.session.add(participant)
            logging.debug('crash ?')
            try:
                db.session.commit()
                logging.debug('Commit successful')
            except Exception as e:
                db.session.rollback()
                logging.error(f'Error during commit: {str(e)}')
            logging.debug('Participant added successfully')
        else:
            logging.debug('Failed to add participant')
    return redirect(url_for('gestion_participants', id_comp=id_comp))

@app.route('/get_escrimeurs')
def get_escrimeurs():
    escrimeurs = Escrimeur.query.all()
    return jsonify([escrimeur.to_dict() for escrimeur in escrimeurs])

@app.route('/update_database', methods=['POST'])
def update_database():
    data = request.get_json()
    field = data.get('field')
    value = data.get('value')
    competition_id = data.get('competitionId')
    competition = Competition.query.get(competition_id)
    setattr(competition, field, value)
    db.session.commit()
    return 'OK'


