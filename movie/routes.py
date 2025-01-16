from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import Movie
from .models import add_movie
import sqlite3

routes = Blueprint('routes', __name__, template_folder='templates')

@routes.route('/', methods=['GET', 'POST'])
def home():
    movie = Movie()
    if not movie.validate_on_submit():
        print(movie.errors)
    if request.method == 'POST': 
        if movie.validate_on_submit(): 
            hbo_max = movie.max.data
            netflix = movie.netflix.data
            hulu =  movie.hulu.data
            prime = movie.prime.data
            appletv = movie.appletv.data
            min_rating = float(movie.min_rating.data)
            max_rating = float(movie.max_rating.data)
            min_year = int(movie.min_year.data)
            max_year = int(movie.max_year.data)
            genre = movie.genre.data
    
            add_movie(hbo_max, netflix, hulu, prime, appletv, min_rating, max_rating, min_year, max_year, genre)
    
          
    return render_template("home.html", movie=movie)
