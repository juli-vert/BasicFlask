from flask import Flask
from flask_cors import CORS
from datetime import timedelta
import blueprint

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "_50^1OR5Q2K=g7h4~l4R"

# Blueprints
app.register_blueprint(blueprint.bprint)

# Enable CORS
CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})

# application settings
app.config['DEBUG'] = False
app.config['SESSION_COOKIE_DOMAIN'] = 'domainname'
app.config['REMEMBER_COOKIE_NAME'] = "NAME"
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_DURATION'] = 6000
app.config['REMEMBER_COOKIE_REFRESH_EACH_REQUEST'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 6000
app.config['SESSION_REFRESH_EACH_REQUEST'] = True
app.config['SESSION_COOKIE_NAME'] = "NAME"
app.config['TEMPLATES_AUTO_RELOAD'] = True

import views

from loginmanager import login_manager
login_manager.init_app(app)
for bp in app.blueprints:
    print(bp)