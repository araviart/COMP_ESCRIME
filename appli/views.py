from .app import app, db
from flask import render_template,url_for, redirect, request
from .models import Book, get_sample, get_author, Author, get_nb_auteurs,User, get_author_by_book_name, get_last_id_book, get_last_id_author 
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, FileField
from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user, current_user, logout_user

# class LoginForm(FlaskForm):
#     email = StringField ("Email")
#     password = PasswordField("Password")
#     def get_authenticated_user (self ):
#         user = User.query.get(self.username.data)
#         if user is None:
#             return None
#         m = sha256 ()
#         m.update(self.password.data.encode ())
#         passwd = m. hexdigest ()
#         return user if passwd == user.password else None
    
@app.route("/")
def home():
    return render_template("Login.html")

@app.route("/ajout-comp")
def ajout_comp_page():
    return render_template("ajout-comp.html")

@app.route("/login/", methods =("GET","POST",))
def login():
    return redirect(url_for('ajout_comp_page'))

@app.route("/logout/")
def logout ():
    logout_user ()
    return redirect(url_for("home"))

@app.route("/test_popup/")
def test_popup():
    return render_template(
        "test_popup.html",
        title="Test")
