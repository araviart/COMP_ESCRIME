from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
# from flask_migrate import Migrate

# username = 'root'
# password = 'root'
# hote = '127.0.0.1:3306'
# dataBase = 'COMP_ESCRIME'

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coursimault:coursimault@servinfo-maria/DBcoursimault'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/COUPE_ESCRIME'
db = SQLAlchemy(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap4(app)

login_manager = LoginManager(app)

app.config["SECRET_KEY"] = "2219f8a3-ca94-4312-a411-cb3d051a1238"
migrate = Migrate(app, db)
