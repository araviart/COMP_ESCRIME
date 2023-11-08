from .app import app
from flask import render_template, url_for, redirect, request
from .models import User, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from hashlib import sha256
from flask_login import login_user, logout_user


class LoginForm(FlaskForm):
    username = StringField ("Username")
    password = PasswordField("Password")
    def get_authenticated_user (self ):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256 ()
        m.update(self.password.data.encode ())
        passwd = m. hexdigest ()
        return user if passwd == user.password else None

@app.route('/')
def home_default():
    return home(5)


@app.route("/login/", methods =("GET","POST",))
def login():
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template(
        "login.html",
        form=f)

@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route("/test_popup/")
def test_popup():
    return render_template(
        "test_popup.html",
        title="Test")

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


@app.route('/home/<int:items>', methods=("GET","POST",))
def home(items):
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
    print(categorie)
    return render_template(
    "competition.html",
    title="Compétitions ESCRIME",
    competitions=compet_filtre,
    categories=categories,
    armes=armes,
    nb_participants=nb_participants,
    items=items,
    selec_arme=arme,
    selec_categorie=categorie,
    selec_sexe=sexe,
    selec_statut=statut
)
    
    
