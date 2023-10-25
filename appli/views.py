from .app import app
from flask import render_template
from .models import Competition

# @app.route("/")
# def home():
#     return render_template(
#     "base.html",
#     title="COMPETITION ESCRIME")


@app.route('/')
def list_competitions():
    competitions = Competition.query.all()
    # 'competitions' contiendra une liste d'objets de modèle Competition
    return render_template('competitions.html', competitions=competitions)
