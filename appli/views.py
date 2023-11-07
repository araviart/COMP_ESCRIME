from .app import app
from flask import render_template, url_for, redirect, request
from .models import User, get_sample, get_categories, get_armes, get_nb_participants
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
    
@app.route("/")
def home():
    competitions = get_sample()
    nb_participants = {comp.idComp: get_nb_participants(comp.idComp) for comp in competitions}
    return render_template(
    "competition.html",
    title="Compétitions ESCRIME",
    competitions=get_sample(),
    categories = get_categories(),
    armes = get_armes(),
    nb_participants = nb_participants)

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