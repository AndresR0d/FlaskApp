from xmlrpc.client import boolean
from flask import Blueprint, render_template    

#setting up Blueprint
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    #passing variables to html file
    return render_template("login.html", boolean=False)

@auth.route('/logout')
def logout():
    return "<p>Loginout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")