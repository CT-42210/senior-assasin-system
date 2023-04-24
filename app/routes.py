from flask import render_template, request, session
from app import app
import test



# / | /index
#   home page of server
@app.route('/')
@app.route('/index')
def index():
    # session['username'] = "johannes"
    # session.clear()
    return render_template('index.html')


# /login page
#   if user already has an account they can log in here
@app.route('/login', methods=["GET", "POST"])
def login():
    # if request.method == "POST":
    #     username = request.form.get("username")
    #     print(username)
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

    if test.login(username, password) is True:
        session['team_name'] = test.teams(username)
        return username


# /signup
#   sign-up page for a user
@app.route("/signup", methods=["GET"])
def sign_up():
    return render_template("signup.html")


# /signup_check
#   creates a new USER --> gets put into database (AKA ".not.a.database.file" files)
#       Will verify that no other user's have the same username
@app.route("/signup_check", methods=["POST"])
def signup_check():

    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    return username
