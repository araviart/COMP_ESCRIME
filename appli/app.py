from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
from flask_mail import Mail
#from flask_migrate import Migrate

# username = 'root'
# password = 'root'
# hote = '127.0.0.1:3306'   
# dataBase = 'COMP_ESCRIME'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://coursimault:coursimault@servinfo-maria/DBcoursimault'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/coupe_escrime2'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/comp_escrime'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:irvyn@localhost/coupe_escrime'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://raviart:raviart@servinfo-maria/DBraviart'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/coupe_escrime'

db = SQLAlchemy(app)

# Configuration de l'application Flask
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'competitionescrime@gmail.com'
app.config['MAIL_PASSWORD'] = 'cxgy uyis eohm twhu' # COMP_ESCRIME45*
app.config['MAIL_DEFAULT_SENDER'] = 'competitionescrime@gmail.com'
mail = Mail(app)
    
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap4(app)

login_manager = LoginManager(app)

app.config["SECRET_KEY"] = "2219f8a3-ca94-4312-a411-cb3d051a1238"
# migrate = Migrate(app, db)

print("Application running on http://127.0.0.1:5000/")