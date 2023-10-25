from .app import app
from flask import render_template
#from .models import get_sample

@app.route("/")
def home():
    return render_template(
    "base.html",
    title="COMPETITION ESCRIME")