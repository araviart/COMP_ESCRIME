from .app import app
from flask import render_template,url_for, redirect, flash
from .models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, logout_user

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
        print(passwd)
        print(user.mdpUser)
        return user if passwd == user.mdpUser else None
    
@app.route("/")
def home():
    return render_template("Login.html")

@app.route("/ajout-comp")
def ajout_comp_page():
    return render_template("ajout-comp.html")

@app.route("/competition")
def competition_page():
    return render_template("competition.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
    f = LoginForm()
    user = f.get_authenticated_user()
    if user:
        login_user(user)
        return redirect(url_for("competition_page"))
    return render_template("Login.html", form=f)


@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route("/test_popup/")
def test_popup():
    return render_template(
        "test_popup.html",
        title="Test")
