import sqlite3
from flask import Flask, g


DATABASE = 'C:/Users/joedc/Movie/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def create_app():
    app = Flask(__name__)

    app.teardown_appcontext(close_connection)

    from .routes import routes
    app.register_blueprint(routes)

    return app
