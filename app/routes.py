from flask import render_template, request, session, redirect, url_for, flash

import database
from app import app
import functions


def load_data(username):
    session['login'] = "True"

    team_data = functions.team_data(username)
    session['team_name'] = team_data[0]
    session['teammate_name'] = team_data[1]
    session['teammate_health'] = team_data[2]
    session['player_health'] = team_data[3]

    target_data = functions.targets(username)
    session['target_team_name'] = target_data[0]
    session['target_user_name_1'] = target_data[1]
    session['target_user_name_2'] = target_data[2]
    session['target_team_health'] = target_data[3]
    session['target_user_health_1'] = target_data[4]
    session['target_user_health_2'] = target_data[5]

    team_data_list = functions.total_team_data()
    session['total_teams'] = str(team_data_list[0])
    session['remaining_teams'] = f"{team_data_list[2]}/{team_data_list[0]}"
    session['remaining_players'] = f"{team_data_list[3]}/{team_data_list[1]}"


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/rules')
def rules():

    return render_template('rules.html')


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


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        print("bruh")

        return "False"

    return render_template("signup_bootstrap.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
