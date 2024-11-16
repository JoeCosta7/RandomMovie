from flask import Blueprint, render_template

routes = Blueprint('main', __name__)

@routes.route('/')
def home():
    return "Hello World"