from flask import render_template, request, session, redirect, url_for, flash
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

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        session['username'] = username
        session['login'] = "False"

        print(username)
        print(password)

        if test.login(username, password) is True:
            session['login'] = "True"
            session['team_name'] = test.teams(username)
            target_list = test.targets(username)
            session['target_team_name'] = target_list[0]
            session['target_user_name_1'] = target_list[1]
            session['target_user_name_2'] = target_list[2]

            return "True"
        else:
            return "False"

    return render_template("login.html")

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

    return redirect(url_for('index'))


# /logout
#   clears all session data from user, seemingly logging them out
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
