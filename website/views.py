from flask import Blueprint,render_template

#setting up BLueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>HOME</h1>"