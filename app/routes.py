from flask import render_template, request, session
from app import app


@app.route('/')
@app.route('/index')
def index():
    session['username'] = "username"
    return render_template('index.html')
