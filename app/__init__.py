from flask import Flask
from config import Config
# from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config.from_object(Config)
# csrf = CSRFProtect(app)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

from app import routes
