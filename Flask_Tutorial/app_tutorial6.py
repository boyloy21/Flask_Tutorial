from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path

db = SQLAlchemy()
DB_NAME = "testdb.db"
def create_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from route import register_routes
    register_routes(app, db)
    # create_database(app)
   
    # migrate = Migrate(app, db)

    return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app)
#         print('Created Database!')