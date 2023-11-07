from .app import app
from flask import render_template

@app.route("/")
def home():
    return render_template("Login.html")

@app.route("/ajout-comp", methods=['POST'])
def ajout_comp_page():
    return render_template("ajout-comp.html")

@app.route("/test_popup/")
def test_popup():
    return render_template(
        "test_popup.html",
        title="Test")
