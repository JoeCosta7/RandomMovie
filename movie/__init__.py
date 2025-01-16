
from flask import Flask, g
from .models import create_movie_table

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "AXCVBMOGHD"

    with app.app_context():
        create_movie_table()
        
    from .routes import routes
    app.register_blueprint(routes)

    return app
