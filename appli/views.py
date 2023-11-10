from .app import app, db
from flask import render_template, url_for, redirect, request
from .models import User, get_sample, get_armes, get_categories, get_type_match, Competition
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TimeField
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField
from hashlib import sha256
from flask_login import login_user, logout_user

class CompetitionForm(FlaskForm):
    titre = StringField("Titre", validators=[DataRequired()])
    organisateur = StringField("Organisateur", validators=[DataRequired()])
    lieu = StringField("Lieu")
    date_deroulement = DateField("Date déroulement", format="%Y-%m-%d", validators=[DataRequired()])
    appt = TimeField("Heure début", validators=[DataRequired()])
    arme = SelectField("Arme", choices=[("fleuret", "Fleuret"), ("sabre", "Sabre"), ("epee", "Épée")])
    sexe = SelectField("Sexe", choices=[("homme", "Homme"), ("femme", "Femme")])
    categorie = SelectField("Catégorie", choices=[("V1", "V1")])
    type_match = SelectField("Type", choices=[("Match Poule", "Match Poule"), ("Match Elimination", "Match Elimination")])
  
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

@app.route("/ok")
def home():
    return render_template(
    "competitionsBS.html",
    title="Compétions ESCRIME",
    competitions=get_sample())

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

from datetime import datetime

@app.route("/", methods=["GET", "POST"])
def ajout_comp_page():
    form = CompetitionForm()

    if form.validate_on_submit():
        titre_f = form.titre.data
        organisateur_f = form.organisateur.data
        lieu_f = form.lieu.data
        date_deroulement_f = form.date_deroulement.data
        heure_debut_f = form.appt.data
        arme_f = form.arme.data
        sexe_f = form.sexe.data
        categorie_f = form.categorie.data
        type_match_f = form.type_match.data

        new_competition = Competition(
            nomComp=titre_f,
            descComp=organisateur_f,
            lieu=lieu_f,
            dateComp=date_deroulement_f,
            heureComp=heure_debut_f,
            arme=arme_f,
            categorie=categorie_f,
            sexeComp=sexe_f,
            estIndividuelle=True,
            )
        db.session.add(new_competition)
        db.session.commit()
    return render_template("ajout-comp.html", listeArmes=get_armes(), listeCategories=get_categories(), listeTypeMatch=get_type_match())
    