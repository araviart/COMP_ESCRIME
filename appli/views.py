import datetime
import random
from .app import app, db, mail
import logging
import math
from .ajout_bd import *
from flask import jsonify, render_template, session, url_for, redirect, request, flash
from .models import *
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField
from hashlib import sha256
from flask_login import login_user, logout_user, current_user
from flask_mail import Message
import datetime
# from flask import make_response
# from weasyprint import HTML

def send_verification_email(user_email, code):
    with app.app_context():
        msg = Message("Votre code de vérification", recipients=[user_email])
        msg.body = f"Votre code de vérification est : {code}"
        mail.send(msg)

def send_bienvenue_email(user_email, user_pseudo):
    with app.app_context():
        msg = Message("Bienvenue sur COMPETITION ESCRIME", recipients=[user_email])
        msg.body = f"Bonjour {user_pseudo},\n\nBienvenue sur COMPETITION ESCRIME !\n\nNous vous souhaitons une bonne navigation sur notre site.\n\nL'équipe COMPETITION ESCRIME"
        mail.send(msg)

logging.basicConfig(filename='debug.log', level=logging.DEBUG)
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

@app.context_processor
def inject_user_status():
    if current_user.is_authenticated:
        return {"user_status": current_user.statutUser}
    return {"user_status": None}

@app.route("/gestions_scores/<int:id_comp>/<int:id_match>/<int:id_type_match>", methods=["GET", "POST"])
def gestion_score_match(id_comp, id_match, id_type_match):
    match_actu = get_match_by_id(id_match)
    return render_template("page-score.html", id_comp=id_comp, id_match=id_match, match_actu=match_actu, id_type_match=id_type_match)

@app.route("/arbitrage/<int:id_comp>/<int:id_type_match>/", methods=["GET", "POST"])

def arbitrage(id_comp, id_type_match=1):
    poules = {}
    if id_type_match != 1:
        matches = Match.query.join(
            MatchCompetition, Match.idMatch == MatchCompetition.idMatch
        ).filter(
            MatchCompetition.idComp == id_comp,
            Match.idTypeMatch == id_type_match
        ).all()
        match_info = [{
            'idMatch': match.idMatch,
            'tireur1': {
                'nom': match.tireur1.escrimeur.nomE,
                'prenom': match.tireur1.escrimeur.prenomE,
                'score': match.touchesDonneesTireur1,
                'club': match.tireur1.club.nomClub,
                'touchesDonneesTireur1': match.touchesDonneesTireur1,
                'touchesRecuesTireur1': match.touchesRecuesTireur2
                },
            'tireur2': {
                'nom': match.tireur2.escrimeur.nomE,
                'prenom': match.tireur2.escrimeur.prenomE,
                'score': match.touchesDonneesTireur2,
                'club': match.tireur2.club.nomClub,
                'touchesDonneesTireur2': match.touchesDonneesTireur2,
                'touchesRecuesTireur2': match.touchesRecuesTireur1
            }
        } for match in matches]
        phase_name = get_phase_name(id_type_match)
        return render_template("arbitrage.html", match_info=match_info, phase_name=phase_name, id_type_match=id_type_match, id_comp=id_comp)
    else:
        liste_absents = []
        numsAbsent = []
        if request.method == "POST":
          absent = request.form.get('liste_absents', '')
          numsAbsent = absent.split(',')
          print("Liste absents: ", numsAbsent)
          poules = {}
        nb_poules = get_nb_poules(id_comp)
        for i in range(1, nb_poules+1):
            poules[i] = {}
            tireurs_club = {} # dict avec le tireur en clé et le nom du club en valeur
            for tireur in get_liste_tireurs_escrimeurs_poule(id_comp, i):
                tireurs_club[tireur] = get_club_tireur_escrimeur(tireur).nomClub
            poules[i]['tireurs'] = tireurs_club
            poules[i]['piste'] = get_piste_poule(id_comp, i)
            poules[i]["id_arbitre"] = get_id_arbitre_poule(id_comp, i)
            poules[i]["stats"] = get_poule_stats(i)
            poules[i]["matchs"] = get_matchs_poules(i, id_comp)
            poules[i]['arbitre'] = get_arbitre_escrimeur_poule(id_comp, i).nomE + " " + get_arbitre_escrimeur_poule(id_comp, i).prenomE
        for num_poule in range(1, nb_poules + 1):
            matches = get_matchs_poules(num_poule, id_comp)
            scores = {}
            print("avant")
            for match in matches:
                match_found = get_match(match.numeroLicenceE1, match.numeroLicenceE2, num_poule, id_comp)
                if match_found:
                    scores[(match_found.numeroLicenceE1, match_found.numeroLicenceE2)] = {
                        'touchesDonneesTireur1': match_found.touchesDonneesTireur1,                    
                        'touchesRecuesTireur2': match_found.touchesRecuesTireur2
                    }
                    scores[(match_found.numeroLicenceE2, match_found.numeroLicenceE1)] = {
                        'touchesDonneesTireur2': match_found.touchesDonneesTireur2,
                        'touchesRecuesTireur1': match_found.touchesRecuesTireur1
                    }
            poules[num_poule]['scores'] = scores
        if numsAbsent != ['']:
            for licence in numsAbsent:
                int_licence = int(licence)
                tireur = get_tireur_by_licence(int_licence)
                liste_absents.append(tireur.to_dict())
                liste_absents_dico = []
                if liste_absents != []:
                    for dict_tireur in liste_absents:
                        tireur = Tireur.query.get(dict_tireur['numeroLicenceE'])
                        if tireur is not None:
                            liste_absents_dico.append(tireur)
                            matches = Match.query.filter_by(numeroLicenceE1=tireur.numeroLicenceE).all()
                            for match in matches:
                                match.touchesDonneesTireur1 = 5
                                match.touchesRecuesTireur2 = 5
                                db.session.commit()
        return render_template("arbitrage-poule.html", poules=poules, id_comp=id_comp, id_type_match=id_type_match, list_absents=liste_absents)

# @app.route("/arbitrage/<int:id_comp>/<int:id_type_match>/", methods=["GET", "POST"])
# def arbitrage(id_comp, id_type_match=1):
#     if request.method == "POST":
#         absent = request.form.get('liste_absents', '')
#     if id_type_match == 1:
#         poules = {}
#         nb_poules = get_nb_poules(id_comp)
#         for i in range(1, nb_poules+1):
#             poules[i] = {}
#             tireurs_club = {} # dict avec le tireur en clé et le nom du club en valeur
#             for tireur in get_liste_tireurs_escrimeurs_poule(id_comp, i):
#                 tireurs_club[tireur] = get_club_tireur_escrimeur(tireur).nomClub
#             poules[i]['tireurs'] = tireurs_club
#             poules[i]['piste'] = get_piste_poule(id_comp, i)
#             poules[i]["id_arbitre"] = get_id_arbitre_poule(id_comp, i)
#             poules[i]["stats"] = get_poule_stats(i)
#             poules[i]["matchs"] = get_matchs_poules(i, id_comp)
#             poules[i]['arbitre'] = get_arbitre_escrimeur_poule(id_comp, i).nomE + " " + get_arbitre_escrimeur_poule(id_comp, i).prenomE
#         for num_poule in range(1, nb_poules + 1):
#             matches = get_matchs_poules(num_poule, id_comp)
#             scores = {}
#             print("avant")
#             for match in matches:
#                 match_found = get_match(match.numeroLicenceE1, match.numeroLicenceE2, num_poule, id_comp)
#                 if match_found:
#                     scores[(match_found.numeroLicenceE1, match_found.numeroLicenceE2)] = {
#            page-score             'touchesDonneesTireur1': match_found.touchesDonneesTireur1,                    
#                         'touchesRecuesTireur2': match_found.touchesRecuesTireur2
#                     }
#                     scores[(match_found.numeroLicenceE2, match_found.numeroLicenceE1)] = {
#                         'touchesDonneesTireur2': match_found.touchesDonneesTireur2,
#                         'touchesRecuesTireur1': match_found.touchesRecuesTireur1
#                     }
#             poules[num_poule]['scores'] = scores
#         liste_absents = []
#         numsAbsent = absent.split(',')
#         print("Liste absents: ", numsAbsent)
#         for licence in numsAbsent:
#             int_licence = int(licence)
#             tireur = get_tireur_by_licence(int_licence)
#             liste_absents.append(tireur.to_dict())
#             print(liste_absents)
#             liste_absents_dico = []
#             if liste_absents != []:
#                 for dict_tireur in liste_absents:
#                     tireur = Tireur.query.get(dict_tireur['numeroLicenceE'])
#                     if tireur is not None:
#                         liste_absents_dico.append(tireur)          
#     return render_template("arbitrage.html", poules=poules, id_comp=id_comp, id_type_match=id_type_match, list_absents=liste_absents)

    
@app.route("/gestion_score/<int:id_comp>/<int:id_type_match>/", methods=["GET", "POST"])
def gestion_score(id_comp, id_type_match=1): # par défaut renvoie à la phase des poules il faut vérifier ça
    # récuperer les infos des poules dans un dict avec le numéro de poule en clé et la liste des tireurs,le nom de la piste, le nom de l'arbitre en valeur
    liste_absents = []
    numsAbsent = []
    if request.method == "POST":
        absent = request.form.get('liste_absents', '')
        numsAbsent = absent.split(',')
        print("Liste absents: ", numsAbsent)
    if id_type_match == 1:
        poules = {}
        nb_poules = get_nb_poules(id_comp)
        for i in range(1, nb_poules+1):
            poules[i] = {}
            tireurs_club = {} # dict avec le tireur en clé et le nom du club en valeur
            for tireur in get_liste_tireurs_escrimeurs_poule(id_comp, i):
                tireurs_club[tireur] = get_club_tireur_escrimeur(tireur).nomClub
            poules[i]['tireurs'] = tireurs_club
            poules[i]['piste'] = get_piste_poule(id_comp, i)
            poules[i]["id_arbitre"] = get_id_arbitre_poule(id_comp, i)
            poules[i]["stats"] = get_poule_stats(i)
            poules[i]["matchs"] = get_matchs_poules(i, id_comp)
            poules[i]['arbitre'] = get_arbitre_escrimeur_poule(id_comp, i).nomE + " " + get_arbitre_escrimeur_poule(id_comp, i).prenomE
        for num_poule in range(1, nb_poules + 1):
            matches = get_matchs_poules(num_poule, id_comp)
            scores = {}
            print("avant")
            for match in matches:
                match_found = get_match(match.numeroLicenceE1, match.numeroLicenceE2, num_poule, id_comp)
                if match_found:
                    scores[(match_found.numeroLicenceE1, match_found.numeroLicenceE2)] = {
                        'touchesDonneesTireur1': match_found.touchesDonneesTireur1,                    
                        'touchesRecuesTireur2': match_found.touchesRecuesTireur2
                    }
                    scores[(match_found.numeroLicenceE2, match_found.numeroLicenceE1)] = {
                        'touchesDonneesTireur2': match_found.touchesDonneesTireur2,
                        'touchesRecuesTireur1': match_found.touchesRecuesTireur1
                    }
            poules[num_poule]['scores'] = scores
        if numsAbsent != ['']:
            for licence in numsAbsent:
                int_licence = int(licence)
                tireur = get_tireur_by_licence(int_licence)
                liste_absents.append(tireur.to_dict())
                print(liste_absents)
                liste_absents_dico = []
                if liste_absents != []:
                    for dict_tireur in liste_absents:
                        tireur = Tireur.query.get(dict_tireur['numeroLicenceE'])
                        if tireur is not None:
                            tireur.append(tireur)
                            liste_absents_dico.append(tireur)
        return render_template('gestion_score.html', poules=poules, id_comp=id_comp, id_type_match=1, list_absents=liste_absents)
    else:
        print("autre phases")

@app.route('/update_scores', methods=['POST'])
def update_scores():
    data = request.get_json()
    license = data['license']
    opponent_license = data['opponentLicense']
    score = data['score']
    id_poule = data['idPoule']
    id_piste = data['idPiste']
    id_comp = data['idCompetition']
    id_arbitre = data['idArbitre']
    id_type_match = data['idTypeMatch']
    print("license: ", license , "opponent_license: ", opponent_license, "score: ", score, "id_poule: ", id_poule, "id_piste: ", id_piste, "id_comp: ", id_comp, "id_arbitre: ", id_arbitre, "id_type_match: ", id_type_match)
    match1 = Match.query.filter_by(numeroLicenceE1=license, numeroLicenceE2=opponent_license).first()
    match2 = Match.query.filter_by(numeroLicenceE1=opponent_license, numeroLicenceE2=license).first()
    try:
        score = int(score)
    except ValueError:
        return 'OK'
    if match1:
        # mettre à jour le match
        print("Mise à jour du match")
        print("Avant: ", match1.touchesRecuesTireur1, match1.touchesDonneesTireur1, match1.touchesRecuesTireur2, match1.touchesDonneesTireur2)
        match1.touchesDonneesTireur1 = score
        match1.touchesRecuesTireur2 = score
        if score == 5:
            match1.gagnant = license
        db.session.commit()
        print("Après: ", match1.touchesRecuesTireur1, match1.touchesDonneesTireur1, match1.touchesRecuesTireur2, match1.touchesDonneesTireur2)
        print("Match mis à jour")
    elif match2:
        # mettre à jour le match
        print("Mise à jour du match")
        print("Avant: ", match2.touchesRecuesTireur1, match2.touchesDonneesTireur1, match2.touchesRecuesTireur2, match2.touchesDonneesTireur2)
        match2.touchesDonneesTireur2 = score
        match2.touchesRecuesTireur1 = score
        if score == 5:
            match2.gagnant = license
            
        db.session.commit()
        print("Après: ", match2.touchesRecuesTireur1, match2.touchesDonneesTireur1, match2.touchesRecuesTireur2, match2.touchesDonneesTireur2)
        print("Match mis à jour")
    else:
        # créer le match
        print("Création du match")
        match = Match(type_match=1, piste=id_piste, arbitre=id_arbitre,
                            tireur1=license, tireur2=opponent_license,
                            date_match=datetime.date.today(), heure_match=datetime.datetime.now().time().strftime("%H:%M:%S"),
                            touches_recues_tireur1=0, touches_donnees_tireur1=score,
                            touches_recues_tireur2=score, touches_donnees_tireur2=0)
        db.session.add(match)
        db.session.commit()
        print("Match créé")

    return 'OK'

@app.route('/update_score_match', methods=['POST'])
def update_score_match():
    data = request.get_json()
    match_id = data.get('matchId')
    score = data.get('score')
    tireur_number = data.get('tireurNumber')
    id_type_match = data.get('idTypeMatch')
    match = Match.query.get(match_id)
    print("match_id:", match_id)
    print("score:", score)
    print("tireur_number:", tireur_number)
    print("match:", match)
    if match:
        if tireur_number == 1:
            match.touchesDonneesTireur1 = score
            match.touchesRecuesTireur2 = score
            if score == 5 and id_type_match==1:
                match.gagnant = match.numeroLicenceE1;
            else:
                if score == 15:
                    match.gagnant = match.numeroLicenceE1;
        elif tireur_number == 2:
            match.touchesDonneesTireur2 = score
            match.touchesRecuesTireur1 = score
            if score == 5 and id_type_match==1:
                match.gagnant = match.numeroLicenceE2;
            else:
                if score == 15:
                    match.gagnant = match.numeroLicenceE2;
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Score mis à jour.'})
    else:
        return jsonify({'success': False, 'message': 'Match non trouvé.'}), 404

@app.route("/afficher-score-poule/<int:id_comp>/")
def afficher_score_poule(id_comp):
    competition = Competition.query.get_or_404(id_comp)
    scores = get_scores_for_competition(id_comp)
    return render_template('Affichage-score.html', data=scores, competition=competition)

def get_scores_for_competition(id_comp):
    classements = db.session.query(Classement, Escrimeur, Club).join(
        Tireur, Classement.numeroLicenceE == Tireur.numeroLicenceE
    ).join(
        Escrimeur, Tireur.numeroLicenceE == Escrimeur.numeroLicenceE
    ).join(
        Club, Tireur.idClub == Club.idClub
    ).filter(
        Classement.idComp == id_comp
    ).order_by(
        Classement.position
    ).all()
    
    scores = []
    for classement, escrimeur, club in classements:
        poules = Poule.query.filter_by(idComp=id_comp).subquery()

        victoires = db.session.query(Match).join(poules, Match.idPoule == poules.c.idPoule).filter(
            db.or_(
                db.and_(Match.numeroLicenceE1 == escrimeur.numeroLicenceE,
                        Match.touchesDonneesTireur1 > Match.touchesRecuesTireur1),
                db.and_(Match.numeroLicenceE2 == escrimeur.numeroLicenceE,
                        Match.touchesDonneesTireur2 > Match.touchesRecuesTireur2)
            )
        ).count()
        
        total_matchs = db.session.query(Match).join(poules, Match.idPoule == poules.c.idPoule).filter(
            db.or_(
                Match.numeroLicenceE1 == escrimeur.numeroLicenceE,
                Match.numeroLicenceE2 == escrimeur.numeroLicenceE
            )
        ).count()
        print(victoires, total_matchs)
        vm_ratio = (victoires / total_matchs) if total_matchs > 0 else "N/A"
        scores.append({
            'Classement': classement.position,
            'Prenom': escrimeur.prenomE,
            'Nom': escrimeur.nomE,
            'VM': vm_ratio,
            'Club': club.nomClub
        })
    
    return scores

# @app.route("/telecharger-pdf/<int:id_comp>/")
# def telecharger_pdf(id_comp):
#     scores = get_scores_for_competition(id_comp)
#     competition = Competition.query.get_or_404(id_comp)
#     rendered = render_template('score_table_pdf.html', data=scores)
#     pdf = HTML(string=rendered).write_pdf()
#     response = make_response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = f'attachment; filename=tableau_scores_{competition.nomComp}.pdf'
#     return response

@app.route("/arbre-competition")
def arbre():
    return render_template("arbre.html")

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
        u = User(pseudoUser=f.pseudo.data , mdpUser=m.hexdigest(), emailUser=f.email.data, statutUser="Utilisateur")
        db.session.add(u)
        db.session.commit()
        send_bienvenue_email(f.email.data, f.pseudo.data)
        return redirect(url_for("home"))

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

@app.route('/home/<int:items>', methods=("GET","POST",))
def home_def(items):
    categories = get_categories()
    total_pages = 0
    erreur_categorie = None
    erreur_sexe = None
    if request.method == "POST":
        page = int(request.form.get('page', 1))
        if 'next' in request.form:
            page += 1
        elif 'prev' in request.form:
            page -= 1
        # récupere les selection du from
        session['categorie'] = request.form.get('categorie')
        session['arme'] = request.form.get('arme')
        session['sexe'] = request.form.get('sexe')
        session['statut'] = request.form.get('statut')
        print("---------------------------------------")
        id_comp = request.form.get("id_comp")
        print(f"id comp : {id_comp}")
        categorie_comp = request.form.get("categorie_comp").strip() if request.form.get("categorie_comp") else None
        print(f"categorie : {categorie_comp}")
        sexe_comp = request.form.get("sexe_comp")
        if sexe_comp == "H":
            sexe_comp = "Homme"
        else:
            sexe_comp = "Dames"
        print(f"sexe : {sexe_comp}")
        escrimeur_inscrit = session.get("escrimeur_inscrit")
        print(f"escrimeur inscrit : {escrimeur_inscrit}")
        categorie_escrimeur = escrimeur_inscrit["categorie"].strip() if escrimeur_inscrit else None
        print(f"categorie escrimeur : {categorie_escrimeur}")
        ind_categorie_escrimeur = categories.index(categorie_escrimeur) if categorie_escrimeur else None
        print(f"ind categorie escrimeur : {ind_categorie_escrimeur}")
        ind_categorie_comp = categories.index(categorie_comp) if categorie_comp else None
        print(f"ind categorie comp : {ind_categorie_comp}")
        radio_selectionnee = request.form.get("role")
        print(f"role : {radio_selectionnee}")
        numero_licence = escrimeur_inscrit["numero_licence"] if escrimeur_inscrit else None
        print(f"numero licence : {numero_licence}")
        match radio_selectionnee:
            case "tireur":
                club = request.form.get("nom_club")
                print(f"club : {club}")
                classement = request.form.get("classement")
                print(f"classement : {classement}")
                if abs(ind_categorie_escrimeur - ind_categorie_comp) <= 2 and ind_categorie_escrimeur <= ind_categorie_comp:
                    erreur_categorie = False
                else:
                    erreur_categorie = True
                if escrimeur_inscrit["sexe"] == sexe_comp:
                    erreur_sexe = False
                else:
                    erreur_sexe = True
                print(erreur_sexe, erreur_categorie)
                if not erreur_categorie and not erreur_sexe:
                    if not session["tireur"]:
                        ajouter_tireur(numero_licence, club, classement)
                        session['tireur'] = {
                            "numero_licence": numero_licence,
                            "club": get_nom_club_by_id(club),
                            "classement": classement
                        }
                    print(ajouter_tireur(numero_licence, club, classement))
                    ajouter_participant(numero_licence, id_comp)
                    print(ajouter_participant(numero_licence, id_comp))
                    escrimeur_inscrit["liste_competitions"].append(int(id_comp))
                    print(escrimeur_inscrit["liste_competitions"])
                else:
                    print("On ne peut pas ajouter à la compétition")
            case "arbitre":
                ajouter_arbitre(numero_licence)
                session["arbitre"] = numero_licence
                print(ajouter_arbitre(numero_licence))
                escrimeur_inscrit["liste_competitions"].append(int(id_comp))
    else:
        page = request.args.get('page', 1, type=int)
        session['categorie'] = request.args.get('categorie', session.get('categorie'))
        session['arme'] = request.args.get('arme', session.get('arme'))
        session['sexe'] = request.args.get('sexe', session.get('sexe'))
        session['statut'] = request.args.get('statut', session.get('statut'))
    competitions = get_sample()
    armes = get_armes()
    nb_participants = {comp.idComp: get_nb_participants(comp.idComp) for comp in competitions}
    # filtre pour les compet
    compet_filtre = filtrer_competitions(competitions, session.get('categorie'), session.get('arme'), session.get('sexe'), session.get('statut'))
    compet_filtre_a_venir = filtrer_competitions(competitions, session.get('categorie'), session.get('arme'), session.get('sexe'), 'A venir')
    if len(compet_filtre) != 0:
        total_pages = math.ceil(len(compet_filtre) / items)
        competitions = compet_filtre[(page - 1) * items:page * items]
    else:
        competitions = []
    liste_club = get_all_club()
    inscription_possible = False
        
    return render_template(
        "competition.html",
        title="Compétitions ESCRIME",
        competitions=competitions, 
        categories=categories,
        armes=armes,
        nb_participants=nb_participants,
        items=items,
        selec_arme=session.get('arme'),
        selec_categorie=session.get('categorie'),
        selec_sexe=session.get('sexe'),
        selec_statut=session.get('statut'),
        page=page,
        compet_filtre = compet_filtre,
        total_pages=total_pages,
        compet_filtre_a_venir=compet_filtre_a_venir,
        liste_club=liste_club,
        erreur_categorie=erreur_categorie,
        erreur_sexe=erreur_sexe,
    )

    
@app.route('/home/')
def home_default():
    return home_def(5)
    
@app.route('/liste-adherent/<int:items>', methods=["GET", "POST"])
def liste_adherents(items):
    total_pages = 0
    dernier_id = dernier_escrimeur_id() + 1
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
    les_categories = get_all_categories()
    role = request.form.get('statut', session.get('statuta', ''))
    categorie = request.form.get('categorie', session.get('categoriea', ''))
    sexe = request.form.get('sexe', session.get('sexea', ''))
    print(sexe)
    
    adherents = filtrer_adherent(adherents, categorie, sexe)
    if request.method == "POST":
        search_query = request.form.get('search')
        # recherche les adhérents en fonction du nom ou prénom
        if search_query:
            adherents = [adherent for adherent in adherents if search_query.lower() in adherent.Escrimeur.prenomE.lower() or search_query.lower() in adherent.Escrimeur.nomE.lower() or search_query.lower() in str(adherent.Escrimeur.numeroLicenceE)]            
    session['statuta'] = role
    session['categoriea'] = categorie
    session['sexea'] = sexe 
    if len(adherents) !=0:
        total_pages = math.ceil(len(adherents) / items)
        adherents = adherents[(page - 1) * items:page * items]
    else:
        adherents = []

    
    return render_template(
        "liste-adherents.html",
        title="Compétitions ESCRIME",
        categories=categories,
        les_categories=les_categories,
        selec_categorie=categorie,
        selec_sexe=sexe,
        selec_statut=role,
        adherents=adherents,
        items=items,
        page=page,
        total_pages=total_pages,
        dernier_id=dernier_id)


    
@app.route('/annuler_comp', methods=['POST'])
def annuler_comp():
    # Rediriger vers l'URL d'origine
    return redirect(request.referrer or url_for('home_default'))

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
        print("Formulaire valide")
        user = current_user
        if user.pseudoUser != form.username.data:
            form.username.errors.append("Pseudonyme erreur")
            return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)

        if form.newpsswd.data != form.confirm.data:
            form.confirm.errors.append("Les mots de passe ne correspondent pas")
            return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)
        
        code = str(random.randint(1000, 9999))
        print(code)
        print(user.emailUser)
        send_verification_email(user.emailUser, code)
        print("Email envoyé")
        session['verification_code'] = code  # Stocker le code temporairement
        session['user_id'] = user.idUser
        session['new_password'] = form.newpsswd.data  # Stocker le nouveau mot de passe temporairement
        print("affichage popup")
        return render_template("edit-user.html", form=form, name=name, show_verification_popup=True)

    return render_template("edit-user.html", form=form, name=name, show_verification_popup=False)

@app.route("/verify-code/<name>", methods=["GET", "POST"])
def verify_code(name):
    if request.method == "POST":
        user_code = request.form['code']
        print(user_code)
        if user_code == session.get('verification_code'):
            # Récupérer l'utilisateur et les informations nécessaires
            user = User.query.get(session.get('user_id'))
            if not user:
                return "Utilisateur non trouvé", 404

            # Procéder à la mise à jour du mot de passe
            new_password = session.get('new_password')
            new_password_hash = sha256()
            new_password_hash.update(new_password.encode())

            user.mdpUser = new_password_hash.hexdigest()
            db.session.commit()

            # Nettoyer la session
            del session['verification_code']
            del session['user_id']
            del session['new_password']

            return redirect(url_for("home")) # "Mot de passe mis à jour avec succès!"
        else:
            flash("Code de vérification incorrect", "error")

    return render_template("edit-user.html", name=name, form=EditUserForm(), show_verification_popup=True)

@app.route('/ajouter_escrimeur/', methods=['GET', 'POST'])
def ajouter_un_escrimeur():
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
        sexe = request.form['sexe_e']
        print(sexe)
        if sexe == "Femme":
            sexe = "Dames"
        print(sexe)
        num_tel = request.form['numTelE'].replace(" ", "")
        num_tel = int(num_tel)
        print(num_tel)
        categorie = request.form['categorie_e'].strip()
        print(categorie)
        liste_noms_categories = [categorie.nomCategorie for categorie in get_all_categories()]
        print(f"toutes les catégiories : {liste_noms_categories}")
        ind_categorie = liste_noms_categories.index(categorie) + 1
        
        # creez un nouvel enregistrement d'adherent 
        nouvel_adherent = Escrimeur(numero_licence_e=numero_licence, categorie=ind_categorie, prenom_e=prenom, nom_e=nom, date_naissance_e=date_naissance, sexe_e=sexe, num_tel_e=num_tel)
        db.session.add(nouvel_adherent)
        db.session.commit()
        print("escrimeur ajouté")
        id_club_blois = Club.query.filter_by(nomClub="BLOIS CE").first().idClub
        print(id_club_blois)
        classement_tireur = 0 
        nouveau_tireur = Tireur(num_licence=numero_licence, club=id_club_blois, classement=classement_tireur)
        db.session.add(nouveau_tireur)
        db.session.commit()
        print("tireur ajouté")

        return redirect(url_for('liste_adherents_def'))
      
@app.route('/')
def home():
    return render_template('Login.html')

from flask import session

@app.route('/gestion_poules/<int:id_comp>', methods=["GET", "POST"])
def gestion_poules(id_comp):
    liste_poules = []
    nb_tireurs = get_nb_tireurs(id_comp)
    nb_arbitres = get_nb_arbitres(id_comp)
    nb_tireurs_par_poule = nb_tireurs // nb_arbitres
    liste_matchs = []
    if request.method == "POST":
        classement_checked = 'classement' in request.form
        club_checked = 'club' in request.form
        equilibrer_checked = 'equilibrer' in request.form
        nb_poules = request.form.get('nb_poules')
        nb_tireurs_poules_str = request.form.get('nb_tireurs/poules')
        if nb_tireurs_poules_str and nb_tireurs_poules_str.isdigit():
            nb_tireurs_poules = int(nb_tireurs_poules_str)
        liste_tireurs = get_liste_participants_competitions_tireurs(id_comp)
        liste_arbitres = get_liste_participants_competitions_arbitres(id_comp)
        liste_pistes = get_liste_pistes_selon_nb_arbitres(id_comp, nb_arbitres)
        i = len(liste_pistes)
        while i < nb_arbitres:
            nouvelle_piste = ajouter_piste(id_comp, f"Piste {i+1}", True)
            i += 1
        liste_pistes = get_liste_pistes_selon_nb_arbitres(id_comp, nb_arbitres)
        nb_tireurs_par_poule = nb_tireurs // nb_arbitres
        numero_licence_arbitre = request.form.get('numero_licence_arbitre')
        id_arbitre = get_id_arbitre_from_escrimeur(numero_licence_arbitre)
        if classement_checked:
            liste_tireurs = classer_tireurs(liste_tireurs)
            if poules_fabriquables(liste_tireurs, liste_arbitres):
                liste_poules = fabriquer_poules(liste_tireurs, liste_arbitres, liste_pistes, "Classement")
        elif club_checked:
            if poules_fabriquables(liste_tireurs, liste_arbitres):
                liste_poules = fabriquer_poules(liste_tireurs, liste_arbitres, liste_pistes, "Club")
        session["liste_poules"] = [ [escrimeur[0].numeroLicenceE for escrimeur in poule] for poule in liste_poules]
        session["liste_arbitres"] = [arbitre.numeroLicenceE for arbitre in liste_arbitres]
        session["liste_pistes"] = [piste.idPiste for piste in liste_pistes]
        return render_template('gestion_poules.html', id_comp=id_comp, nb_tireurs=get_nb_tireurs(id_comp), 
                               nb_arbitres=get_nb_arbitres(id_comp), liste_tireurs=liste_tireurs, liste_arbitres=liste_arbitres, 
                               liste_poules=liste_poules, nb_tireurs_par_poule=nb_tireurs_par_poule, liste_pistes=liste_pistes) 

    liste_tireurs = get_liste_participants_competitions_tireurs(id_comp)
    liste_arbitres = get_liste_participants_competitions_arbitres(id_comp)
    liste_pistes = get_liste_pistes_selon_nb_arbitres(id_comp, nb_arbitres)
    competition = Competition.query.get(id_comp)    
    if competition is not None:
        return render_template('gestion_poules.html', id_comp=id_comp, nb_tireurs=nb_tireurs, nb_arbitres=nb_arbitres, 
                               liste_tireurs=liste_tireurs, liste_arbitres=liste_arbitres, 
                               liste_poules=liste_poules, nb_tireurs_par_poule=nb_tireurs_par_poule, liste_pistes=liste_pistes)
        

@app.route("/appel/<int:id_comp>", methods=["GET", "POST"])
def appel(id_comp):
    rows_data = []
    participants_present = []
    if request.method == "POST":
        pistes = session.get("liste_pistes")
        arbitres = session.get("liste_arbitres")
        liste_poules = session.get("liste_poules")
        try:
            for i in range(len(liste_poules)):
                num_licence_arbitre = arbitres[i]
                id_arbitre = get_id_arbitre_from_escrimeur(num_licence_arbitre)
                nom_poule = f"Poule {i+1}"
                id_piste = pistes[i]
                ajouter_poule(id_comp, id_piste, id_arbitre, nom_poule)
                id_poule = get_id_poule(id_comp, id_piste, id_arbitre, nom_poule)
                for j in range(1, len(liste_poules[i])):
                    ajouter_participant_poule(id_poule, liste_poules[i][j], id_comp)
                    tireur = Tireur.query.get(liste_poules[i][j])
                    rows_data.append(tireur.to_dict())
            id_type_match = 1 # correspond a un match de poule
            date_match = datetime.date.today()
            date_match_str = date_match.strftime("%Y-%m-%d")
            heure_match = datetime.datetime.now().time().strftime("%H:%M:%S")
            
            for i in range(len(liste_poules)):
                poule = liste_poules[i]
                id_piste = pistes[i]
                id_arbitre = get_id_arbitre_from_escrimeur(arbitres[i])
                id_poule = get_id_poule(id_comp, id_piste, id_arbitre, f"Poule {i+1}")  # Move this line here
                
                for j in range(len(poule)):
                    for k in range(j+1, len(poule)):
                        numero_licence_e1 = poule[j]
                        numero_licence_e2 = poule[k]
                        match_id = ajouter_match(id_type_match, id_piste, id_arbitre, numero_licence_e1, numero_licence_e2, date_match_str, heure_match, 0, 0, 0, 0)
                        if match_id is not None:
                            contenir = Contenir(idPoule=id_poule, idComp=id_comp, idMatch=match_id)  
                            db.session.add(contenir)     
                db.session.commit()
            redirect(url_for('appel', id_comp=id_comp))
            competition = Competition.query.get(id_comp) 
            return render_template('appel.html', competition = competition, rows_data=rows_data, participants_present=participants_present)
        except Exception as e:
            print(e)
    competition = Competition.query.get(id_comp)  
    if competition is not None:
        rows_data = []
        participants_comp = get_liste_participants_competitions(id_comp)
        participants_comp = get_liste_participants_competitions(id_comp)
        for participant in participants_comp:
            dict_tireur = participant.tireur.to_dict()
            rows_data.append(dict_tireur)
        participants_present = []
        return render_template('appel.html', competition = competition, rows_data=rows_data, participants_present=participants_present)
    
    
@app.route('/adherent/')
def liste_adherents_def():
    return liste_adherents(5)
  

@app.route("/ajout-comp")
def ajout_comp_page():
    armes = get_armes()
    categories = get_categories()
    lieux = get_lieux()
    types = ["Individuelle", "Equipe"]
    return render_template("ajout-comp.html", listeArmes=armes, listeCategories=categories, listeTypeMatch=types, lieux=lieux)

@app.route('/ajout-comp/', methods=['POST'])
def ajout_comp():
    # Récupérez les données du formulaire
    nomLieu = request.form.get('nomLieu')
    adresseLieu = request.form.get('adresseLieu')
    villeLieu = request.form.get('villeLieu')
    cpLieu = request.form.get('codePostalLieu')
    nomSaison = "Saison 2023"  # Supposons que c'est fixe pour cet exemple
    nomCat = request.form.get('categorie')  # Assurez-vous que le nom correspond au champ dans le HTML
    nomArme = request.form.get('arme')  # Idem
    nomComp = request.form.get('titre')
    nomOrga = request.form.get('organisateur')
    descComp = f"Competition {nomComp} organisée par {nomOrga}" # Ajoutez un champ pour la description si nécessaire
    dateComp = request.form.get('date-deroulement')
    heureComp = request.form.get('appt')
    sexeComp = request.form.get('sexe')[:1].upper()
    estIndividuelle = request.form.get('type') == 'Individuelle'
    print(nomLieu,adresseLieu,villeLieu,cpLieu, nomSaison, nomCat, nomArme, nomComp, nomOrga, descComp, dateComp, heureComp, sexeComp, estIndividuelle)

    resultat = creer_competition(nomLieu,adresseLieu,villeLieu,cpLieu, nomSaison, nomCat, nomArme, nomComp, descComp, dateComp, heureComp, sexeComp, estIndividuelle)
    if isinstance(resultat, Competition):
        return redirect(url_for('gestion_participants', id_comp=resultat.idComp))
    else:
        return redirect(url_for('ajout_comp_page'))

# @app.route('/annuler_comp', methods=['POST'])
# def annuler_comp():
#     if lieu is None:
#         lieu = Lieu(nom_lieu=form.lieu.data, ville_lieu="", code_postal_lieu=0, adresse_lieu="")
#         db.session.add(lieu)
#         db.session.commit()
#         competition = Competition(idLieu=lieu.idLieu, 
#                                   idSaison=Saison.query.get(1).idSaison,
#                                   idCat=getattr(Categorie.query.filter_by(nomCategorie=form.categorie.data).first(), 'idCat', None),
#                                   idArme=getattr(Arme.query.filter_by(nomArme=form.arme.data).first(), 'idArme', None),
#                                   nomComp=form.titre.data,
#                                   descComp=f"Competition organisée par {form.organisateur.data}", 
#                                   dateComp=form.date_deroulement.data,
#                                   heureComp=form.heure_debut.data,
#                                   sexeComp=form.sexe.data[:1],
#                                   estIndividuelle=form.type_comp.data == 'individuel')
#         db.session.add(competition)
#         db.session.commit()
#         flash('La compétition a été ajoutée') # à changer avec une popup
#         return redirect(url_for('home'))

#     # Rediriger vers l'URL d'origine
#     return redirect(request.referrer or url_for('home_default'))

@app.route("/gestion_participants/<int:id_comp>", methods=("GET", "POST"))
def gestion_participants(id_comp):
    competition = Competition.query.get(id_comp)
    participants_blois = get_participants(id_comp, club="BLOIS CE")
    participants_other = get_participants(id_comp, club="!")
    participants_arb = get_arbitres(id_comp)
    nb_participants_blois = len(participants_blois)
    nb_participants_other = len(participants_other)
    nb_participants_arb = len(participants_arb)
    
    return render_template(
      "gestion-participants.html",
      title="Gestion des participants",
      participants_blois=participants_blois,
      nb_participants_blois=nb_participants_blois,
      participants_other=participants_other,
      nb_participants_other=nb_participants_other,
      competition=competition,
      participants_arb=participants_arb,
      nb_participants_arb=nb_participants_arb
  )

@app.route('/ajouter_arbitre_competition/<int:id_comp>', methods=['POST'])
def ajouter_arbitre_competition(id_comp):
        data = request.get_json()
        numeroLicenceE = data.get('numeroLicenceE')
        logging.debug(numeroLicenceE)
        arbitre = Arbitre(numeroLicenceE)
        db.session.add(arbitre)
        participant = ParticipantsCompetition(numeroLicenceE, id_comp)
        db.session.add(participant)

        db.session.commit()
        logging.debug("ça passe commit participant compet")

        return jsonify({'success': True, 'message': 'Arbitre ajouté avec succès'})

@app.route('/get_escrimeurs/<gender>/<int:id_comp>')
def get_escrimeurs_json(gender, id_comp):
    escrimeurs_to_display = []
    escrimeurs = None
    if gender == 'M': 
        escrimeurs = Escrimeur.query.all()
    elif gender == "H":
        gender = "Homme"
        escrimeurs = Escrimeur.query.filter_by(sexeE=gender).all()
    elif gender == "F":
        gender = "Femme"
        escrimeurs = Escrimeur.query.filter_by(sexeE=gender).all()

    registered_licence_numbers = set() 
    participants = get_liste_participants_competitions(id_comp)
    for participant in participants:
        registered_licence_numbers.add(participant.tireur.numeroLicenceE)
    escrimeurs_to_display = [e for e in escrimeurs if e.numeroLicenceE not in registered_licence_numbers]
    return jsonify([escrimeur.to_dict() for escrimeur in escrimeurs_to_display])

@app.route('/get_adherents/<gender>/<int:id_comp>')
def get_adherents_json(gender,id_comp):
    registered_licence_numbers = set()
    participants = get_liste_participants_competitions(id_comp)
    escrimeurs = get_adherents_adapte_json(gender)
    for participant in participants:
        registered_licence_numbers.add(participant.tireur.numeroLicenceE)
    escrimeurs_to_display = [e for e in escrimeurs if e.numeroLicenceE not in registered_licence_numbers]
    return jsonify([escrimeur.to_dict() for escrimeur in escrimeurs_to_display])


@app.route('/delete_participant/<int:id_comp>/<int:id>/', methods=['POST'])
def delete_participant(id, id_comp):
    participant = ParticipantsCompetition.query.filter_by(numeroLicenceE=id).first()

    if participant:
        db.session.delete(participant)
        db.session.commit()
    return redirect(url_for('gestion_participants', id_comp=id_comp))

@app.route('/ajouter_escrimeur_competition/<int:id_comp>/', methods=['POST'])
def add_participant(id_comp):
    if request.method == 'POST':
        tireur = request.get_json().get('numeroLicenceE')
        logging.debug(f'numerolicence_tireur: {tireur}')
        
        tireur = Tireur.query.get(tireur)
        
        logging.debug(f'tireur: {tireur}')

        competition = Competition.query.get(id_comp)
        logging.debug(f'competition: {competition}')
        getattr(competition, "idComp", None)
        if tireur and competition:
            participant = ParticipantsCompetition(numeroLicenceE=getattr(tireur, "numeroLicenceE", None), idComp=getattr(competition, "idComp", None))
            logging.debug('creation participant')
            db.session.add(participant)
            logging.debug('crash ?')
            try:
                db.session.commit()
                logging.debug('Commit successful')
            except Exception as e:
                db.session.rollback()
                logging.error(f'Error during commit: {str(e)}')
            logging.debug('Participant added successfully')
        else:
            logging.debug('Failed to add participant')
    return redirect(url_for('gestion_participants', id_comp=id_comp))

@app.route("/delete_arbitre/<int:id_comp>/<int:id_arbitre>/", methods=["POST"])
def delete_arbitre(id_comp, id_arbitre):
    arbitre = Arbitre.query.filter_by(idArbitre=id_arbitre).first()
    if arbitre:
        participant = ParticipantsCompetition.query.filter_by(
            numeroLicenceE=arbitre.numeroLicenceE, idComp=id_comp
        ).first()
        if participant:
            db.session.delete(participant)
        
        db.session.delete(arbitre)
        db.session.commit()
    return redirect(url_for("gestion_participants", id_comp=id_comp))

@app.route('/update_database', methods=['POST'])
def update_database():
    data = request.get_json()
    field = data.get('field')
    value = data.get('value')
    competition_id = data.get('competitionId')
    competition = Competition.query.get(competition_id)
    setattr(competition, field, value)
    db.session.commit()
    return 'OK'

@app.route('/competition/<int:id_comp>')
def actu_stat_comp(id_comp):
    competition = Competition.query.get_or_404(id_comp)
    state = get_competition_statut(competition)
    if state == 'participants':
        return redirect(url_for('gestion_participants', id_comp=id_comp))
    elif state == 'poule':
        return redirect(url_for('gestion_poules', id_comp=id_comp))
    elif state == 'appel':
        return redirect(url_for('appel', id_comp=id_comp))
    elif state == 'score':
        return redirect(url_for('gestion_score', id_comp=id_comp))
    else:
        return "les problèmes"


@app.route('/arbre/<int:id_comp>')
def classement_provisioire(id_comp):
    #
    #else :
    competition = Competition.query.get_or_404(id_comp)
    id_phase_en_cours = 1
    if est_terminer_phase_poule(id_comp):
        id_phase_en_cours = 2
        if est_termine_phase_huitieme(id_comp):
            id_phase_en_cours = 3
            if est_termine_phase_quart(id_comp):
                id_phase_en_cours = 4
                if est_termine_phase_demi(id_comp):
                    id_phase_en_cours = 5
    poules = Poule.query.filter_by(idComp=id_comp).all()
    nb_participants = get_nb_participants(id_comp)
    print(f'nb_participants: {nb_participants}')
    huitiemes = []
    quarts = []
    demis = []
    finale = []
    if est_terminer_phase_poule(id_comp) and not est_cree_huitieme(id_comp) and not est_cree_quart(id_comp) and not est_cree_demi(id_comp):
        etablir_classement_poule(id_comp)
        if nb_participants > 16:
            creer_huitiemes(id_comp)
        elif nb_participants > 8:
            creer_quarts(id_comp)
        elif nb_participants > 4:
            creer_demis(id_comp)
        elif nb_participants > 2 :
            return render_template('arbre.html', competition=competition, quarts=quarts, demis=demis, finale=finale, huitiemes = huitiemes)
    elif est_terminer_phase_poule(id_comp) and est_cree_huitieme(id_comp) and est_termine_phase_huitieme(id_comp) and not est_cree_quart(id_comp) and not est_cree_demi(id_comp):
        creer_quarts_apres_huitieme(id_comp)
    elif est_terminer_phase_poule(id_comp) and est_cree_quart(id_comp) and est_termine_phase_quart(id_comp) and not est_cree_demi(id_comp):
        creer_demis_apres_quart(id_comp)
    elif est_terminer_phase_poule(id_comp) and est_cree_demi(id_comp) and est_termine_phase_demi(id_comp) and not est_cree_finale(id_comp):
        creer_finale_apres_demi(id_comp)
    matchs = get_matchs_non_poule(id_comp)
    huitiemes, quarts, demis, finale = get_all_phase(id_comp)
    # Test avec le meme matchs pour toutes les phases
    semi = get_demis(id_comp)
    quart = get_quarts(id_comp)
    print(f'quart : {quart}')
    print(f'demi : {demis}')
    return render_template('arbre.html', competition=competition, quarts=quarts, demis=demis, finale=finale, huitiemes = huitiemes, type_match = id_phase_en_cours)

@app.route('/update_absents', methods=['POST'])
def update_absents():
    participants_absents = request.json['participants_absents']
    session['participants_absents'] = participants_absents
    return jsonify(success=True)
    troisieme =[]
    for poule in poules:
        matchs = Match.query.filter_by(idPoule=poule.idPoule).all()
        for match in matchs:
            if match.idTypeMatch == 2 :
                quarts.append(match.to_dict())
            elif match.idTypeMatch == 3 :
                demis.append(match.to_dict())
            elif match.idTypeMatch == 4 :
                finale.append(match.to_dict())
            elif match.idTypeMatch == 5 :
                troisieme.append(match.to_dict())
    return render_template('arbre.html', competition=competition, quarts=quarts, demis=demis, finale=finale, troisieme = troisieme)

@app.route("/inscription_escrimeur/", methods=["GET", "POST"])
def inscription_escrimeur():
    print("---------------------")
    liste_categories = get_all_categories()
    if request.method == "POST":
        categorie = request.form.get("categorie")
        print(f"categorie : {categorie}")
        nom = request.form.get("nom")
        print(f"nom : {nom}")
        prenom = request.form.get("prenom")
        print(f"prenom : {prenom}")
        sexe = request.form.get("sexes")
        if sexe == "Femme":
            sexe = "Dames"
        print(f"sexe : {sexe}")
        numero_licence = request.form.get("numero_licence")
        print(f"numero : {numero_licence}")
        date_naissance = request.form.get("date_naissance")
        print(f"date : {date_naissance}")
        telephone = request.form.get("telephone")
        telephone_sans_espace = telephone.replace(" ", "")
        telephone_int = int(telephone_sans_espace)
        print(f"tel : {telephone}")
        ajouter_escrimeur(categorie, prenom, nom, date_naissance, numero_licence, sexe, telephone_int)
        print(ajouter_escrimeur(categorie, prenom, nom, date_naissance, numero_licence, sexe, telephone_int))
        session["escrimeur_inscrit"] = {
            "categorie": categorie,
            "nom": nom,
            "prenom": prenom,
            "date_naissance": date_naissance,
            "numero_licence": numero_licence,
            "sexe": sexe,
            "telephone": telephone_int,
            "liste_competitions": []
        }
        if session.get("tireur"):
            session["tireur"] = None
        if session.get("arbitre"):
            session["arbitre"] = None
        print(f"escrimeur inscrit : {session['escrimeur_inscrit']}")
        return redirect(url_for('home_def', items=5))
    return render_template('inscription_escrimeur.html', liste_categories=liste_categories)

@app.context_processor
def inject_escrimeur_inscrit():
    escrimeur_inscrit = session.get('escrimeur_inscrit', None)
    return dict(escrimeur_inscrit=escrimeur_inscrit)

@app.context_processor
def inject_tireur():
    tireur = session.get('tireur', None)
    return dict(tireur=tireur)

@app.context_processor
def inject_arbitre():
    arbitre = session.get('arbitre', None)
    return dict(arbitre=arbitre)
