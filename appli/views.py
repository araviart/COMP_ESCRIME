from .app import app, db
from flask import flash, render_template, url_for, redirect, request
from .models import *
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField
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
    
class EditUserForm(FlaskForm):
    newpsswd = PasswordField("Nouveau mot de passe")
    confirm = PasswordField("Confirmez le nouveau mot de passe")
    username = StringField("Pseudonyme actuelle")
    password = PasswordField("Mot de passe actuelle")

@app.route("/appel/")
def jenesaispas():
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
        return redirect(url_for("home"))

@app.route("/login/", methods=["GET", "POST"])
def login():
    f = LoginForm()
    user = f.get_authenticated_user()
    if user:
        login_user(user)
        # return redirect(url_for("home_default"))
        return redirect(url_for("ajout_comp_page"))
    else:
        flash("Mot de passe incorrect", "error")
    return render_template("Login.html", form=f)

@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route('/home/')
def home_default():
    return home_def(5)

@app.route("/ajout-comp")
def ajout_comp_page():
    return render_template("ajout-comp.html", listeArmes=get_armes(), listeCategories=get_categories(), listeTypeMatch=get_type_match())

@app.route('/adherent/')
def adherent_default():
    return liste_adherents(5)    
      
@app.route('/liste-adherent/<int:items>', methods=["GET", "POST"])
def liste_adherents(items):
    adherents = get_adherents()
    categories = get_categories()
    role = request.form.get('statut')
    categorie = request.form.get('categorie')
    sexe = request.form.get('sexe')
    adherents = filtrer_adherent(adherents, categorie, sexe, role)

    if request.method == "POST":
        search_query = request.form.get('search')
        # recherche les adhérents en fonction du nom ou prénom
        if search_query:
            adherents = [adherent for adherent in adherents if search_query.lower() in adherent.Escrimeur.prenomE.lower() or search_query.lower() in adherent.Escrimeur.nomE.lower() or search_query.lower() in str(adherent.Escrimeur.numeroLicenceE)]            
    adherents = adherents[:items]
    
    return render_template(
        "liste-adherents.html",
        title="Compétitions ESCRIME",
        categories=categories,
        selec_categorie=categorie,
        selec_sexe=sexe,
        selec_statut=role,
        adherents=adherents,
        items=items)

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
    competitions = competitions[:items]

    # récupere les selection du from
    categorie = request.form.get('categorie')
    arme = request.form.get('arme')
    sexe = request.form.get('sexe')
    statut = request.form.get('statut')
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

@app.route('/ajouter_escrimeur', methods=['GET', 'POST'])
def ajouter_escrimeur():
    # sexes = db.session.query(Escrimeur.sexeE).distinct().all()
    # sexes = [s[0] for s in sexes] 
    if request.method == 'POST':
        nom = request.form.get('nom')
        prenom = request.form.get('prenom')
        date_naissance = request.form.get('date_naissance')
        numero_licence = request.form.get('numero_licence')
        sexe = request.form.get('sexe')

        # nouvel_escrimeur = Escrimeur(nomE=nom, prenomE=prenom, dateNaissanceE=date_naissance,
        #                             numeroLicenceE=numero_licence, sexeE=sexe)

        # db.session.add(nouvel_escrimeur)
        # db.session.commit()

        return redirect(url_for('ajouter_escrimeur'))
    return render_template('test_popup.html')

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


