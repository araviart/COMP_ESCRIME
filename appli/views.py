from .app import app, db
import math
from flask import render_template, url_for, redirect, request, flash
from .models import User, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions, get_adherents, filtrer_adherent
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField
from hashlib import sha256
from flask_login import login_user, logout_user, current_user

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def get_authenticated_user(self):
        user = User.query.filter_by(emailUser=self.email.data).first()
        if user is None:
            return None

        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.mdpUser else None

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
  
class EditUserForm(FlaskForm):
    passwd = PasswordField("Nouveau mot de passe")
    confirm = PasswordField("Confirmez le nouveau mot de passe")
    username = StringField("Pseudonyme actuelle")
    password = PasswordField("Mot de passe actuelle")

@app.route("/ok")
def home():
    return render_template("Login.html")

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

@app.route('/home/')
def home_default():
    return home_def(5)

@app.route("/ajout-comp")
def ajout_comp_page():
    return render_template("ajout-comp.html")

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
        user = User.query.get(name)

        if user.username != form.username.data:
            form.username.errors.append("Pseudonyme erreur")
            return render_template("edit-user.html", form=form)

        if form.newpsswd.data != form.confirm.data:
            form.confirm.errors.append("Les mots de passe ne correspondent pas")
            return render_template("edit-user.html", form=form)

        password_hash = sha256()
        password_hash.update(form.password.data.encode())

        if user.password != password_hash.hexdigest():
            form.password.errors.append("Mot de passe incorrect")
            return render_template("edit-user.html", form=form)

        new_password_hash = sha256()
        new_password_hash.update(form.newpsswd.data.encode())

        user.password = new_password_hash.hexdigest()
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
def liste_adherents_def():
    return liste_adherents(5)
  
@app.route('/liste-adherent/<int:items>', methods=["GET", "POST"])
def liste_adherents(items):
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