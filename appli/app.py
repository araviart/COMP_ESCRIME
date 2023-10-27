from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coursimault:coursimault@servinfo-maria/DBcoursimault'
db = SQLAlchemy(app)

app. config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

login_manager = LoginManager(app)

app.config["SECRET_KEY"] = "2219f8a3-ca94-4312-a411-cb3d051a1238"