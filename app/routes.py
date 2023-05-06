import smtplib

from flask import render_template, request, session, redirect, url_for
from flask_wtf.csrf import CSRFError
from app import app
import functions
from flask_mail import Mail, Message

mail = Mail(app)
# instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nkjcgpt@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpwsarpxwwxfcrbe'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


def load_data(username):
    session['login'] = "True"

    team_data = functions.team_data(username)
    session['team_name'] = team_data[0]
    session['teammate_name'] = team_data[1]
    session['teammate_health'] = team_data[2]
    session['player_health'] = team_data[3]
    session['player_address'] = team_data[4]
    session['teammate_address'] = team_data[5]

    target_data = functions.targets(username)
    session['target_team_name'] = target_data[0]
    session['target_user_name_1'] = target_data[1]
    session['target_user_name_2'] = target_data[2]
    session['target_team_health'] = target_data[3]
    session['target_user_health_1'] = target_data[4]
    session['target_user_health_2'] = target_data[5]
    session['target_user_address_1'] = target_data[6]
    session['target_user_address_2'] = target_data[7]

    team_data_list = functions.total_team_data()
    session['total_teams'] = str(team_data_list[0])
    session['remaining_teams'] = f"{team_data_list[2]}/{team_data_list[0]}"
    session['remaining_players'] = f"{team_data_list[3]}/{team_data_list[1]}"


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")


@app.route('/rules')
def rules():
    return render_template('rules.html', title="Rules")


@app.route('/advanced')
def advanced():
    return render_template('advanced.html', title="Advanced")


@app.route('/settings', methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        team_name = request.form.get("team_name")
        user_address = request.form.get("user_address")

        if username != session['username']:
            print("username changed")
        if password1 != session['username']:
            print("password changed")
        if team_name != session['team_name']:
            print("team name changed")
        if user_address != session['player_address']:
            print("user_address changed")

        print(username, password1, password2, team_name, user_address)

    return render_template('settings.html', title="Settings")


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

    return render_template("login.html", title="Login")


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        try:
            msg = Message(
                f'hello {username}',
                sender=("SeniorAssasins", "nkjcgpt@gmail.com"),
                recipients=[f'{email}']
            )
            msg.body = 'Hello!'
            # msg.html = render_template('index.html', **kwargs)
            mail.send(msg)

            return "False"
        except smtplib.SMTPDataError:
            return "emailError"
        except smtplib.SMTPRecipientsRefused:
            return "FalseMail"

    return render_template("signup.html", title="Sign Up")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
