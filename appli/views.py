from .app import app, db
from flask import render_template, url_for, redirect, request, flash
from .models import User, get_sample, get_categories, get_armes, get_nb_participants,filtrer_competitions
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

@app.route("/")
def home():
    # Exemple de données à afficher dans chaque ligne
    rows_data = [
        {'Nom': 'Doe', 'Prenom': 'John', 'DateNaissance': '01/01/1990', 'Telephone': '07 86 97 48 35', 'Sexe': 'M', 'Club': 'Club A', 'Classement': 'A'},
        {'Nom': 'Smith', 'Prenom': 'Alice', 'DateNaissance': '02/02/1995', 'Telephone': '07 86 97 48 35', 'Sexe': 'F', 'Club': 'Club B', 'Classement': 'B'},
        {'Nom': 'Johnson', 'Prenom': 'Bob', 'DateNaissance': '03/03/1992', 'Telephone': '07 86 97 48 35', 'Sexe': 'M', 'Club': 'Club C', 'Classement': 'C'},
        {'Nom': 'Williams', 'Prenom': 'Emma', 'DateNaissance': '04/04/1988', 'Telephone': '07 86 97 48 35', 'Sexe': 'F', 'Club': 'Club D', 'Classement': 'D'}
    ]


    return render_template('Appel.html', rows_data=rows_data)

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
