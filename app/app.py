from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = Path(__file__).parent
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin@localhost:5432/temp_user"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sqUeUriWArysIANDAcENchReaDbuLair'
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db, directory=basedir / 'migrations')
