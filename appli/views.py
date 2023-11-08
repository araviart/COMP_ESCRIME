from .app import app
from flask import render_template, url_for, redirect, request
from .models import User, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions, get_adherents
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
def adherent_default():
    return liste_adherents(5)    
    
    
@app.route('/liste-adherent/<int:items>', methods=("GET","POST",))
def liste_adherents(items):
    adherents = get_adherents()
    categories = get_categories()
    adherents = adherents[:items]
    
    statut = request.form.get('statut')
    categorie = request.form.get('categorie')
    sexe = request.form.get('sexe')
    
    return render_template(
    "liste-adherents.html",
    title="Compétitions ESCRIME",
    categories=categories,
    selec_categorie=categorie,
    selec_sexe=sexe,
    selec_statut=statut,
    adherents = adherents,
    items=items)


    
@app.route('/ok')
def home_default():
    return home(5)


@app.route('/home/<int:items>', methods=("GET","POST",))
def home(items):
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
