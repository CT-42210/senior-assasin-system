from flask import render_template, request, session, redirect, url_for, flash
from app import app
import functions


def load_data(username):
    session['login'] = "True"
    session['team_name'] = functions.teams(username)
    target_list = functions.targets(username)
    session['target_team_name'] = target_list[0]
    session['target_user_name_1'] = target_list[1]
    session['target_user_name_2'] = target_list[2]
    session['teammate_health'] = "Dead"
    session['teammate_name'] = "functions"
    team_data_list = [3, 6, 2, 3]
    session['total_teams'] = str(team_data_list[0])
    session['remaining_teams'] = f"{team_data_list[2]}/{team_data_list[0]}"
    session['remaining_players'] = f"{team_data_list[3]}/{team_data_list[1]}"


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

        if functions.login(username, password) is True:
            load_data(username)

            return "True"
        else:
            return "False"

    return render_template("login.html")


# /signup
#   sign-up page for a user
@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        print("bruh")

        return "False"

    return render_template("signup_bootstrap.html")


# /logout
#   clears all session data from user, seemingly logging them out
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
