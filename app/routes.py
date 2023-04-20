from flask import render_template, request, session
from app import app


# / | /index
#   home page of server
@app.route('/')
@app.route('/index')
def index():
    # session['username'] = "johannes"
    # session.clear()
    return render_template('index.html')


# /login page
#   if user already has an ccount they can log in here
@app.route('/login')
def login():
    return render_template("login.html")


# /login_check
#   checks if users are exist | are properly logging in, correct credentials
@app.route("/login_check", methods=["POST"])
def login_check():

    username = request.form.get("username")
    password = request.form.get("password")
    session['username'] = username

    print(username)
    print(password)
    return username


# /signup
#   sign-up page for a user