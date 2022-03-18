from flask import Blueprint,render_template

#setting up BLueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    #Allows to render a template on our app :D
    return render_template("home.html")