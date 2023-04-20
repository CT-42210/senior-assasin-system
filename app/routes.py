from flask import render_template, request, session
from app import app


@app.route('/')
@app.route('/index')
def index():
    session['username'] = "johannes"
    # session.clear()
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template("login.html")
