from flask import Blueprint, render_template, request
from movie.forms import MovieForm

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/', methods=['GET', 'POST'])
def home():
    movie = MovieForm()
    return render_template("home.html", movie=movie)