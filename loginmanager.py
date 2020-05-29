# login-manager
from flask_login import LoginManager
from models import User
import views
from flask import Response, render_template

login_manager = LoginManager()
login_manager.remember_cookie_httponly = False
login_manager.login_view = 'login'
login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = "Session expired"

@login_manager.user_loader
def load_user(name):
    print("Entering the user loader with {0}".format(name))
    if name:
        user = User()
        user.id = name
        user.is_authenticated = True
        return user
    else:
        return

@login_manager.request_loader
def request_loader(request):
    print("Request {0}".format(request.form))
    name = request.form.get('name')
    if name == None:
        return
    print("Entering the rq loader with {0}".format(name))
    r = ''
    # get the user from the database and store in r the id
    if r != "":
        user = User()
        user.id = name
        user.uid = r
        user.is_authenticated = True
        return user
    else:
        return

@login_manager.unauthorized_handler
def unauthorized_handler():
    return Response(render_template('forbidden.html'))