from .app import app, db
import math
from flask import render_template, url_for, redirect, request, flash
from .models import Arme, Categorie, Competition, Lieu, Saison, User, get_participants, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions, get_adherents, filtrer_adherent, Escrimeur, dernier_escrimeur_id
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import BooleanField, DateField, SelectField, StringField, PasswordField, SubmitField, TimeField
from hashlib import sha256
from flask_login import login_user, logout_user, current_user

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

class CompetitionForm(FlaskForm):
    titre = StringField('Titre', validators=[DataRequired()])
    organisateur = StringField('Organisateur', validators=[DataRequired()])
    lieu = StringField("Lieu", validators=[DataRequired()])
    date_deroulement = DateField('Date déroulement', format='%Y-%m-%d', validators=[DataRequired()])
    heure_debut = TimeField('Heure début', format='%H:%M', validators=[DataRequired()])
    arme = SelectField('Arme', choices=[('epee', 'Épée'), ('fleuret', 'Fleuret'), ('sabre', 'Sabre')])
    sexe = SelectField('Sexe', choices=[('homme', 'Homme'), ('femme', 'Femme')])
    categorie = SelectField('Categorie', choices=[('senior', 'Senior'), ('u13', 'U13'), ('cadet', 'Cadet'), ('u15', 'U15'), ('u17', 'U17'), ('u20', 'U20'), ('v1', 'V1'), ('v2', 'V2'), ('v3', 'V3'), ('v4', 'V4')])
    type_comp = SelectField('Type', choices=[('individuel', 'Individuel'), ('equipe', 'Équipe')])
    est_publie = BooleanField('Publier le tournoi')
    submit = SubmitField('Publier le tournoi')

class EditUserForm(FlaskForm):
    newpsswd = PasswordField("Nouveau mot de passe")
    confirm = PasswordField("Confirmez le nouveau mot de passe")
    username = StringField("Pseudonyme actuelle")
    password = PasswordField("Mot de passe actuelle")

@app.route("/appel/")
def jenesaispas():
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
        return redirect(url_for("home"))

@app.route("/login/", methods=["GET", "POST"])
def login():
    f = LoginForm()
    user = f.get_authenticated_user()
    if user:
        login_user(user)
        # return redirect(url_for("home_default"))
        return redirect(url_for("ajout_comp"))
    else:
        flash("Mot de passe incorrect", "error")
    return render_template("Login.html", form=f)

@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route('/home/<int:items>', methods=("GET","POST",))
def home_def(items):
    if request.method == "POST":
        page = int(request.form.get('page', 1))
        if 'next' in request.form:
            page += 1
        elif 'prev' in request.form:
            page -= 1
    else:
        page = request.args.get('page', 1, type=int)
    competitions = get_sample()
    categories = get_categories()
    armes = get_armes()
    nb_participants = {comp.idComp: get_nb_participants(comp.idComp) for comp in competitions}
    # récupere les selection du from
    categorie = request.form.get('categorie')
    arme = request.form.get('arme')
    sexe = request.form.get('sexe')
    statut = request.form.get('statut')
    print(sexe)
    # filtre pour les compet
    compet_filtre = filtrer_competitions(competitions, categorie, arme, sexe, statut)
    if len(compet_filtre) !=0:
        competitions = compet_filtre[(page - 1) * items:page * items]
    else:
        competitions = []
    print(categorie)
    return render_template(
    "competition.html",
    title="Compétitions ESCRIME",
    competitions=competitions,  # Pass the paginated competitions, not compet_filtre
    categories=categories,
    armes=armes,
    nb_participants=nb_participants,
    items=items,
    selec_arme=arme,
    selec_categorie=categorie,
    selec_sexe=sexe,
    selec_statut=statut,
    page=page,
    compet_filtre = compet_filtre
)

@app.route('/home/')
def home_default():
    return home_def(5)

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
        user = current_user
        if user.pseudoUser != form.username.data:
            form.username.errors.append("Pseudonyme erreur")
            return render_template("edit-user.html", form=form)

        if form.newpsswd.data != form.confirm.data:
            form.confirm.errors.append("Les mots de passe ne correspondent pas")
            return render_template("edit-user.html", form=form)

        password_hash = sha256()
        password_hash.update(form.password.data.encode())

        if user.mdpUser != password_hash.hexdigest():
            form.password.errors.append("Mot de passe incorrect")
            return render_template("edit-user.html", form=form)

        new_password_hash = sha256()
        new_password_hash.update(form.newpsswd.data.encode())

        user.mdpUser = new_password_hash.hexdigest()
        db.session.commit()

        return redirect(url_for("home"))
    return render_template("edit-user.html", form=form, name=name)

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
    competition = Competition.query.get(id_comp)
    if competition is not None:
        return render_template('gestion_poules.html', id_comp=id_comp, competition=competition)

@app.route('/adherent/')
def liste_adherents_def():
    return liste_adherents(5)
  
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
    role = request.form.get('statut')
    categorie = request.form.get('categorie')
    sexe = request.form.get('sexe')
    adherents = filtrer_adherent(adherents, categorie, sexe)
    if request.method == "POST":
        search_query = request.form.get('search')
        # recherche les adhérents en fonction du nom ou prénom
        if search_query:
            adherents = [adherent for adherent in adherents if search_query.lower() in adherent.Escrimeur.prenomE.lower() or search_query.lower() in adherent.Escrimeur.nomE.lower() or search_query.lower() in str(adherent.Escrimeur.numeroLicenceE)]            
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

@app.route('/ajout-comp', methods=['GET', 'POST'])
def ajout_comp():
    form = CompetitionForm()

    if form.validate_on_submit():
        lieu = Lieu.query.filter_by(nomLieu=form.lieu.data).first()

        if lieu is None:
            # si le lieu existe pas on le crée avec un id auto incrémenté et le reste des colonnes vides
            # à voir après si l'on gère ces colonnes avec de nouveaux champs ou une API qui autocomplète les 
            # champs en fonction du nom du lieu
            lieu = Lieu(nom_lieu=form.lieu.data, ville_lieu="", code_postal_lieu=0, adresse_lieu="")
            db.session.add(lieu)
            db.session.commit()
        competition = Competition(idLieu=lieu.idLieu, 
                                  idSaison=Saison.query.get(1).idSaison,
                                  idCat=getattr(Categorie.query.filter_by(nomCategorie=form.categorie.data).first(), 'idCat', None),
                                  idArme=getattr(Arme.query.filter_by(nomArme=form.arme.data).first(), 'idArme', None),
                                  nomComp=form.titre.data,
                                  descComp=f"Competition organisée par {form.organisateur.data}", 
                                  dateComp=form.date_deroulement.data,
                                  heureComp=form.heure_debut.data,
                                  sexeComp=form.sexe.data[:1],
                                  estIndividuelle=form.type_comp.data == 'individuel')
        db.session.add(competition)
        db.session.commit()
        flash('La compétition a été ajoutée') # à changer avec une popup
        return redirect(url_for('home'))
    return render_template('ajout-comp.html', form=form)

@app.route("/gestion_participants/<int:id_comp>", methods=("GET", "POST"))
def gestion_participants(id_comp):
    competition = Competition.query.get(id_comp)
    participants_blois = get_participants(id_comp, club="Club Blois")
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
    
@app.route('/delete_participant/<int:id>', methods=['POST'])
def delete_participant(id):
    participant = Escrimeur.query.get(id)
    if participant:
        db.session.delete(participant)
        db.session.commit()
    return redirect(url_for('gestion_participants', id_comp=request.form.get('id_comp')))

@app.route('/ajouter_escrimeur_competition/<int:id_comp>/', methods=['POST'])
def add_participant(id_comp):
    # à implémenter
    return redirect(url_for('gestion_participants', id_comp=id_comp))