from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:irvyn@localhost/COUP_ESCRIME'
db = SQLAlchemy(app)